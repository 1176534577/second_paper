import math
from random import random, randint

import numpy as np

from now_used.algorithm.get_needed_data import getabc, getb
from now_used.algorithm.get_needed_data.AddGetA import getypinghua, getxpinghua, getzpinghua
from now_used.algorithm.get_needed_data.getA import getA
from now_used.algorithm.Algorithm import Algorithm
# x为公式里的x1,y为公式里面的x2
from now_used.utils.base import SA_all_res


class SA(Algorithm):
    def __init__(self, iter=100, T0=100, Tf=0.01, alpha=0.99):
        my, mx, mz = getabc.getabc()
        instance = getA.get_instance(my, mx, mz)
        self.A = instance.return_A_normal()
        col = instance.return_col()
        self.B = getb.return_b_normal()
        self.Xref = np.matrix([2.65] * col).T
        self.y_matrix = getypinghua()
        self.x_matrix = getxpinghua()
        self.z_matrix = getzpinghua()
        self.col = col
        # self.func = func
        self.iter = iter  # 内循环迭代次数,即为L =100
        self.alpha = alpha  # 降温系数，alpha=0.99
        self.T0 = T0  # 初始温度T0为100
        self.Tf = Tf  # 温度终值Tf为0.01
        self.T = T0  # 当前温度
        # self.x = [random() * 11 - 5 for i in range(iter)]  # 随机生成100个x的值
        # self.y = [random() * 11 - 5 for i in range(iter)]  # 随机生成100个y的值
        self.X = np.matrix([2.65] * 1320).T
        self.most_best = []
        """
        random()这个函数取0到1之间的小数
        如果你要取0-10之间的整数（包括0和10）就写成 (int)random()*11就可以了，11乘以零点多的数最大是10点多，最小是0点多
        该实例中x1和x2的绝对值不超过5（包含整数5和-5），（random() * 11 -5）的结果是-6到6之间的任意值（不包括-6和6）
        （random() * 10 -5）的结果是-5到5之间的任意值（不包括-5和5），所有先乘以11，取-6到6之间的值，产生新解过程中，用一个if条件语句把-5到5之间（包括整数5和-5）的筛选出来。
        """
        # self.history = {'f': [], 'T': []}

    def func(self, X):  # 函数优化问题
        res = pow(np.linalg.norm(self.A * X - self.B), 2) + 0.05 * (
                10 * pow(np.linalg.norm(X - self.Xref), 2) + 1 * pow(np.linalg.norm(X - self.y_matrix * X),
                                                                     2) + 1 * pow(
            np.linalg.norm(
                X - self.x_matrix * X), 2) + 5 * pow(np.linalg.norm(X - self.z_matrix * X), 2))
        return res

    def randint_generation(self, min, max, mount):
        list = []
        while len(list) != mount:
            unit = randint(min, max)
            if unit not in list:
                list.append(unit)
        return list

    def generate_new(self, x):  # 扰动产生新解的过程
        # while True:
        # x_new = x + self.T * np.matrix([random() - random() for _ in range(1320)]).T
        addx = 0.1 * np.matrix([random() - random() for _ in range(1320)]).T
        # randint(a, b)   用来生成[a,b]之间的随意整数，包括两个边界值。
        rand = self.randint_generation(0, 1319, 1000)
        addx[rand] = 0
        x_new = x + addx
        for index, i in enumerate(x_new):
            if i < 0:
                x_new[index] = 0
            elif i > 3:
                x_new[index] = 3
            # if all(0 <= x_new) and all(x_new <= 3):
            #     break  # 重复得到新解，直到产生的新解满足约束条件
        return x_new

    def Metrospolis(self, f, f_new):  # Metropolis准则
        if f_new <= f:
            return 1
        else:
            p = math.exp((f - f_new) / self.T)
            if random() < p:
                return 1
            else:
                return 0

    def best(self):  # 获取最优目标函数值
        f_list = []  # f_list数组保存每次迭代之后的值
        for i in range(self.iter):
            f = self.func(self.X)
            f_list.append(f)
        f_best = min(f_list)

        idx = f_list.index(f_best)
        return f_best, idx  # f_best,idx分别为在该温度下，迭代L次之后目标函数的最优解和最优解的下标

    def run(self, suf):
        count = 0
        # 外循环迭代，当前温度小于终止温度的阈值
        while self.T > self.Tf:

            # 内循环迭代100次
            for i in range(self.iter):
                f = self.func(self.X)  # f为迭代一次后的值
                x_new = self.generate_new(self.X)  # 产生新解
                f_new = self.func(x_new)  # 产生新值
                if self.Metrospolis(f, f_new):  # 判断是否接受新值
                    self.X = x_new  # 如果接受新值，则把新值的x,y存入x数组和y数组

            print(self.func(self.X))
            # 迭代L次记录在该温度下最优解
            # ft, _ = self.best()
            # self.history['f'].append(ft)
            # self.history['T'].append(self.T)
            # 温度按照一定的比例下降（冷却）
            self.T = self.T * self.alpha
            count += 1

            # 得到最优解
        # f_best, idx = self.best()
        # print(f"F={f_best}, x={self.x[idx]}, y={self.y[idx]}")
        print(f"F={self.func(self.X)}")
        with open(SA_all_res + suf, 'w') as w:
            for val in self.X:
                w.write(f'{val[0, 0]}\n')

    def main(self, suf):
        self.run(suf)

# plt.plot(sa.history['T'], sa.history['f'])
# plt.title('SA')
# plt.xlabel('T')
# plt.ylabel('f')
# plt.gca().invert_xaxis()
# plt.show()
