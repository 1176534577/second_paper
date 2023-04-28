# import sympy
# import os

# from numpy import zeros
# from numpy.linalg import matrix_rank
from sympy import zeros

from now_used.utils.base import root_path


class getA:
    __a = None

    def __init__(self):
        self.__air_cell = None
        self.__row = None
        self.__col = None
        self.__m = None
        self.__cell_total=None
        self.__oldtonew_row = None
        self.__oldtonew_col = None
        self.__get_air_cell()
        self.__calculate_A()

    def __get_air_cell(self):
        """
        前、后、左、右、上分别加了一个格子，为了确保探测器在mesh内部
        xcel = x * my * mz + y * mz + z + 1

        :return:
        """
        air_cell = set()
        my, mx, mz = 28, 24, 27
        # 最上层z=0,x,y随意
        for x in range(mx):
            for y in range(my):
                air_cell.add(x * my * mz + y * mz + 1)
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

        # 压缩行、列
        # abspath=os.path.abspath('.')
        with open(root_path + r'\data\output\ijg', 'r') as d:
            self.__cell_total=int(d.readline().strip().split()[1])
            oldtonew_row = {}
            oldtonew_col = {}
            new_row = 0
            new_col = 0
            while (d_line := d.readline()) != '':
                shuzu = d_line.strip().split()
                row, col = int(shuzu[0]), int(shuzu[1])
                if row not in oldtonew_row.keys():
                    oldtonew_row[row] = new_row
                    new_row += 1
                if col not in oldtonew_col.keys() and col not in air_cell:
                    oldtonew_col[col] = new_col
                    new_col += 1
        # row = len(oldtonew_row)
        # col = len(oldtonew_col)
        m = zeros(new_row, new_col)
        # m = [[0] * col for _ in range(row)]

        # 填入矩阵
        with open(root_path + r'\data\output\ijg', 'r') as d:
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

    @staticmethod
    def get_instance():
        if getA.__a is None:
            getA.__a = getA()
        return getA.__a

    def return_A(self):
        return self.__m

    def return_row(self):
        return self.__row

    def return_col(self):
        return self.__col

    def return_oldtonew_row(self):
        return self.__oldtonew_row

    def return_oldtonew_col(self):
        return self.__oldtonew_col

    def return_oldcol(self):
        return self.__oldtonew_col.keys()

    def return_newtoold_col(self):
        newtoold_col = {}
        for key, value in self.__oldtonew_col.items():
            newtoold_col[value] = key
        return newtoold_col

    def return_cell_total(self):
        return self.__cell_total