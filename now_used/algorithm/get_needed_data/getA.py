﻿# import sympy

from numpy import zeros, array, matrix
# from numpy.linalg import matrix_rank
import numpy as np

from now_used.utils.base import root_path
from now_used.algorithm.get_needed_data.AddGetA import getpinghua


class getA:
    __a = None

    def __init__(self, my, mx, mz):
        self.__air_cell = None
        self.__row = None
        self.__col = None  # 也就是未知数的个数
        self.__m = None
        self.__cell_total = None
        self.__oldtonew_row = None
        self.__oldtonew_col = None
        self.__my = my
        self.__mx = mx
        self.__mz = mz
        self.__get_air_cell()
        self.__calculate_A()
        # self.real_m()

    def __get_air_cell(self):
        """
        前、后、左、右分别加了一个格子，为了确保探测器在mesh内部
        xcel = x * my * mz + y * mz + z + 1

        :return:
        """
        air_cell = set()
        my = self.__my
        mx = self.__mx
        mz = self.__mz
        # 最上层z=0,x,y随意
        # for x in range(mx):
        #     for y in range(my):
        #         air_cell.add(x * my * mz + y * mz + 1)
        # 最左层y=0
        for x in range(mx):
            for z in range(mz):
                air_cell.add(x * my * mz + z + 1)
        # 最右层y=my-1
        for x in range(mx):
            for z in range(mz):
                air_cell.add(x * my * mz + (my - 1) * mz + z + 1)
        # 最前层x=0
        for y in range(my):
            for z in range(mz):
                air_cell.add(y * mz + z + 1)
        # 最后层x=mx-1
        for y in range(my):
            for z in range(mz):
                air_cell.add((mx - 1) * my * mz + y * mz + z + 1)

        with open(root_path + r'\data\output\air_cell', 'w') as w:
            for air in air_cell:
                w.write(f'{air}\n')

        self.__air_cell = air_cell

    def __calculate_A(self):
        """
        row是按序的，col是乱序的

        :return:
        """
        # row=23592
        # col=18144
        air_cell = self.__air_cell
        # with open(abspath + r'..\data\output\ijg', 'r') as d:
        #     while (d_line:=d.readline())!='\n':
        #         row,col,value=d_line.strip().split()
        #         m[int(row)][int(col)]=float(value)
        col_set = set()

        # 压缩行、列  todo 列不是有序的，乱序的，需要更改
        # abspath=os.path.abspath('.')
        path = root_path + r'\data\output\new_ijg'
        with open(path, 'r') as d:
            self.__cell_total = int(d.readline().strip().split()[1])
            oldtonew_row = {}
            oldtonew_col = {}
            new_row = 0
            # new_col = 0
            while (d_line := d.readline()) != '':
                shuzu = d_line.strip().split()
                row, col = int(shuzu[0]), int(shuzu[1])
                if row not in oldtonew_row.keys():
                    oldtonew_row[row] = new_row
                    new_row += 1
                if col not in oldtonew_col.keys() and col not in air_cell:
                    col_set.add(col)
                    # oldtonew_col[col] = new_col
                    # new_col += 1
        new_col = 0
        col_list = list(col_set)
        col_list.sort()
        for val in col_list:
            oldtonew_col[val] = new_col
            new_col += 1
        # row = len(oldtonew_row)
        # col = len(oldtonew_col)
        m = zeros((new_row, new_col))
        # m = [[0] * col for _ in range(row)]

        # 填入矩阵
        with open(path, 'r') as d:
            d.readline()
            while (d_line := d.readline()) != '':
                shuzu = d_line.strip().split()
                row, col, value = int(shuzu[0]), int(shuzu[1]), float(shuzu[2])
                if col not in air_cell:
                    m[oldtonew_row[row], oldtonew_col[col]] = value

        # mrank=matrix_rank(m)
        # print(f'方程的秩:{mrank}')
        # if mrank<new_col:
        #     print("有无数个解")

        self.__row = new_row
        self.__col = new_col
        self.__m = m
        self.__oldtonew_row = oldtonew_row
        self.__oldtonew_col = oldtonew_col
        print()

    @staticmethod
    def get_instance(my, mx, mz):
        if getA.__a is None:
            getA.__a = getA(my, mx, mz)
        return getA.__a

    def return_A(self):
        copym = matrix(self.__m)
        # 增加平滑性
        pinghuaxing = 0.85 * np.eye(self.__col) - getpinghua()
        copym = np.vstack((copym, pinghuaxing))
        # for i in range(self.__col):
        #     copym[i,i] += 0.5
        self.__row += self.__col
        return copym

    def return_A_test(self):
        copym = matrix([[1, 2, 3], [4,5,6]])
        # 增加平滑性

        self.__row = copym.shape[0]
        self.__col = copym.shape[1]
        return copym

    def return_A_normal(self):
        return self.__m

    def return_row(self):
        return self.__row

    def return_col(self):
        return self.__col

    def return_oldtonew_row(self):
        return self.__oldtonew_row

    def return_oldtonew_col(self) -> dict:
        return self.__oldtonew_col

    def return_oldcol(self):
        return self.__oldtonew_col.keys()

    def return_newtoold_col(self):
        newtoold_col = {}
        for key, value in self.__oldtonew_col.items():
            newtoold_col[value] = key
        return newtoold_col

    def return_newtoold_row(self):
        newtoold_row = {}
        for key, value in self.__oldtonew_row.items():
            newtoold_row[value] = key
        return newtoold_row

    def return_cell_total(self):
        return self.__cell_total

    def real_m(self):
        li = self.suo()
        self.__m = np.delete(self.__m, li, axis=0)
        self.__row = self.__m.shape[0]
        self.__col = self.__m.shape[1]

    def suo(self):
        li = []
        for no, i in enumerate(self.__m):
            if search_no_zero(i) in {1, 2}:
                li.append(no)
                # print(search_location(i))
        return li


def count_less_and_equal_num(m, num):
    li = []
    for no, i in enumerate(m):
        if search_no_zero(i) <= num:
            li.append(no)
    print(f"共有{len(li)}个射线少于等于{num}个的")
    return li


def search_no_zero(a):
    count = 0
    for i in a:
        if i != 0:
            count += 1
    return count


def search_location(a):
    li = []
    for no, i in enumerate(a):
        if i != 0:
            li.append(no)
    return li


if __name__ == '__main__':
    my, mx, mz = 13, 14, 10
    a = getA.get_instance(my, mx, mz)
    m = a.return_A()
    key = a.return_oldtonew_col().keys()

    ylist = [7, 8, 9]
    xlist = [5, 6, 7, 8]
    zlist = [3, 4]

    empty_hole = []

    for y in ylist:
        for x in xlist:
            for z in zlist:
                empty_hole.append(x * my * mz + y * mz + z + 1)

    solve = []
    for i in key:
        if i in empty_hole:
            solve.append(2)
        else:
            solve.append(2.65)

    val = matrix(solve).T
    y = m * val
    with open(root_path + r'\data\output\duibi', 'w') as w:
        for i in array(y):
            w.write(f'{str(i[0])}\n')

    # print(count_less_num(m))
    # print(suo(m))
