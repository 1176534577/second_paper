import random

import numpy as np
from numpy import matrix

from now_used.algorithm.Algorithm import Algorithm
from now_used.algorithm.get_needed_data.AddGetA import getypinghua, getxpinghua, getzpinghua
from now_used.algorithm.get_needed_data.getA import getA
from now_used.algorithm.get_needed_data.getabc import getabc
from now_used.algorithm.get_needed_data.getb import return_b_normal
from now_used.utils.base import CG_all_res


class CG(Algorithm):

    def __init__(self):

        a, b, c = getabc()
        instance = getA.get_instance(a, b, c)
        self.A = matrix(instance.return_A_normal())
        col = instance.return_col()
        self.B = return_b_normal()
        # xref = matrix([2.65] * col).T
        Xref = np.array([2.65] * col)
        self.XXref = np.matrix(Xref).T

        y_matrix = getypinghua()
        x_matrix = getxpinghua()
        z_matrix = getzpinghua()

        self.y_matrix = np.eye(col) - y_matrix
        self.x_matrix = np.eye(col) - x_matrix
        self.z_matrix = np.eye(col) - z_matrix
        self.col = col
        self.Xref = Xref

    def goldsteinsearch(self, f, df, d, x, alpham, rho, t):
        '''
        线性搜索子函数
        数f，导数df，当前迭代点x和当前搜索方向d，t试探系数>1，
        '''
        flag = 0

        a = 0
        b = alpham
        fk = f(x)
        gk = df(x)

        phi0 = fk
        dphi0 = np.dot(gk.T, d)
        alpha = b * random.uniform(0, 1)

        while (flag == 0):
            newfk = f(x + alpha * d)
            phi = newfk
            # print(phi,phi0,rho,alpha ,dphi0)
            if (phi - phi0) <= (rho * alpha * dphi0):
                if (phi - phi0) >= ((1 - rho) * alpha * dphi0):
                    flag = 1
                else:
                    a = alpha
                    b = b
                    if b < alpham:
                        alpha = (a + b) / 2
                    else:
                        alpha = t * alpha
            else:
                a = a
                b = alpha
                alpha = (a + b) / 2
        return alpha

    # def Wolfesearch(f, df, d, x, alpham, rho, t):
    #     '''
    #     线性搜索子函数
    #     数f，导数df，当前迭代点x和当前搜索方向d
    #     σ∈(ρ,1)=0.75
    #     '''
    #     sigma = 0.75
    #
    #     flag = 0
    #
    #     a = 0
    #     b = alpham
    #     fk = f(x)
    #     gk = df(x)
    #
    #     phi0 = fk
    #     dphi0 = np.dot(gk, d)
    #     alpha = b * random.uniform(0, 1)
    #
    #     while (flag == 0):
    #         newfk = f(x + alpha * d)
    #         phi = newfk
    #         # print(phi,phi0,rho,alpha ,dphi0)
    #         if (phi - phi0) <= (rho * alpha * dphi0):
    #             # if abs(np.dot(df(x + alpha * d),d))<=-sigma*dphi0:
    #             if (phi - phi0) >= ((1 - rho) * alpha * dphi0):
    #                 flag = 1
    #             else:
    #                 a = alpha
    #                 b = b
    #                 if (b < alpham):
    #                     alpha = (a + b) / 2
    #                 else:
    #                     alpha = t * alpha
    #         else:
    #             a = a
    #             b = alpha
    #             alpha = (a + b) / 2
    #     return alpha

    def main(self, suf):
        # 包装一层
        x = self.frcg(self.fun, self.gfun, self.Xref)
        with open(CG_all_res + suf, 'w') as w:
            for value in x[0]:
                w.write(f'{value}\n')

    def frcg(self, fun, gfun, x0):
        # x0是初始点，fun和gfun分别是目标函数和梯度
        # x,val分别是近似最优点和最优值，k是迭代次数
        # dk是搜索方向，gk是梯度方向
        # epsilon是预设精度，np.linalg.norm(gk)求取向量的二范数
        maxk = 200
        rho = 0.6
        sigma = 0.4
        k = 0
        epsilon = 1e-5
        n = np.shape(x0)[0]
        itern = 0
        W = np.zeros((self.col, 20000))

        f = open("共轭.txt", 'w')

        while k < maxk:
            W[:, k] = x0
            gk = gfun(x0)
            itern += 1
            itern %= n
            if itern == 1:
                dk = -gk
            else:
                beta = 1.0 * np.dot(gk, gk) / np.dot(g0, g0)
                dk = -gk + beta * d0
                gd = np.dot(gk, dk)
                if gd >= 0.0:
                    dk = -gk
            if np.linalg.norm(gk) < epsilon:
                break

            alpha = self.goldsteinsearch(fun, gfun, dk, x0, 1, 0.1, 2)
            # alpha=Wolfesearch(fun,gfun,dk,x0,1,0.1,2)
            x0 += alpha * dk
            gk_norm = np.linalg.norm(gk)
            f.write(str(k) + '  ' + str(gk_norm) + "\n")
            print(k, alpha, gk_norm)
            g0 = gk
            d0 = dk
            k += 1

        W = W[:, 0:k]  # 记录迭代点
        return [x0, fun(x0), k, W]

    def fun(self, X):
        X = np.matrix(X).T
        return pow(np.linalg.norm(self.A * X - self.B), 2) + 0.05 * (
                10 * pow(np.linalg.norm(X - self.XXref), 2) + 1 * pow(np.linalg.norm(self.y_matrix * X), 2) + 1 * pow(
            np.linalg.norm(self.x_matrix * X), 2) + 5 * pow(np.linalg.norm(self.z_matrix * X), 2))

    def gfun(self, X):
        X = np.matrix(X).T
        res = 2 * (self.A.T * (
                self.A * X - self.B) + X - self.XXref + self.y_matrix.T * self.y_matrix * X + self.x_matrix.T * self.x_matrix * X + self.z_matrix.T * self.z_matrix * X)

        return np.array(res).reshape(self.col, )


if __name__ == "__main__":
    # X1 = np.arange(-1.5, 1.5 + 0.05, 0.05)
    # X2 = np.arange(-3.5, 4 + 0.05, 0.05)
    # [x1, x2] = np.meshgrid(X1, X2)
    # f = 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2  # 给定的函数
    # plt.contour(x1, x2, f, 20)  # 画出函数的20条轮廓线

    # x0 = np.array([-1.2, 1])
    pass
    # x = frcg(fun, gfun, Xref)
    # with open(r'.\data\gongetidu', 'w') as w:
    #     for value in x[0]:
    #         w.write(f'{value}\n')
    # print(x[0], x[2])
    # [1.00318532 1.00639618]
    # W = x[3]
    # print(W[:, :])
    # plt.plot(W[0, :], W[1, :], 'g*-')  # 画出迭代点收敛的轨迹
    # plt.show()
