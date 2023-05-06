import time
from datetime import datetime
import random

from matplotlib import pyplot as plt
from numpy import zeros, matrix, eye, hstack, vstack, array
from numpy.linalg import pinv, norm

from now_used.algorithm.get_needed_data.getA import getA
from now_used.algorithm.get_needed_data.getBound import get_Bound
from now_used.algorithm.get_needed_data.getb import return_b
from now_used.utils.base import root_path


class rnn:
    def __init__(self, my, mx, mz):

        self.H_A = None
        self.b = None
        aa = getA.get_instance(my, mx, mz)
        # 目前需要在row的前面，因为在下面方法里面会更新row，可以防止col的后面
        # todo 更改此处low,up,A的值
        self.low = 0
        self.up = 3
        self.a = aa.return_A()
        # self.a = aa.return_A_test()

        self.row = aa.return_row()
        self.col = aa.return_col()

        # todo 修改此处
        self.bb = return_b(self.col)
        # self.bb = return_b_test()
        self.new_to_old_col = aa.return_newtoold_col()
        self.cell_total = aa.return_cell_total()
        self.l(my, mx, mz)
        self.initH_A()

    def initH_A(self):
        row = self.row
        col = self.col

        m1 = self.a
        m2 = hstack((m1, zeros((row, 2 * col))))
        m3 = vstack((-eye(col), eye(col)))
        m4 = hstack((m3, zeros((2 * col, 2 * col))))
        self.H_A = matrix(vstack((m2, m4)))

    def H(self, d):
        """

        :param d:
        :type:
        :return:
        :rtype:sympy.Matrix
        """
        row = self.row
        col = self.col
        for i in range(2 * col):
            self.H_A[row + i, col + i] = 2 * d[0, i]

        return self.H_A

    def A(self, d):
        """

        :param p:
        :param d:
        :type:
        :return:
        :rtype:sympy.Matrix
        """
        row = self.row
        col = self.col
        for i in range(2 * col):
            self.H_A[row + i, col + i] = d[0, i]
        return self.H_A

    def l(self, my, mx, mz):
        """
        常数

        :return:
        :rtype: sympy.Matrix
        """
        xiajie, shangjie = get_Bound(my, mx, mz, self.low, self.up)
        self.b = vstack((vstack((self.bb, -xiajie)), shangjie))

    def solver(self, init_value=0.0, outer_layer_cycle=10, inner_layer_cycle=10, number=0):
        start = time.time()
        low = self.low
        up = self.up
        row = self.row
        col = self.col
        print(f'小矩阵：{row}行{col}列')
        print(f'大矩阵：{row + 3 * col}行{3 * col}列')

        w = matrix(zeros((outer_layer_cycle * inner_layer_cycle + 1, 3 * col)))

        t = 0

        init_value1 = [random.random() for _ in range(2 * col)]
        # init_value1 = [2.65] * 2 * col
        initd = matrix(init_value1)

        # 第一次，即初始值,t=0对应的
        # 初始值
        # todo 修改
        # w[0, :] = matrix([[1, 2, 3] + init_value1])
        w[0, :] = matrix([[2.65] * col + init_value1])

        pinAk = pinv(self.A(initd))

        Ak = self.A(initd)

        lk = self.b
        integral = zeros((row + 2 * col, 1))
        tao = 0.2
        # 0到1之间，rou*tao*tao=ρτ^2
        gama = 0.0001

        ee = [0.0] * (outer_layer_cycle * inner_layer_cycle + 1)
        eexiao = [0.0] * (outer_layer_cycle * inner_layer_cycle + 1)
        print("初始化工作完成")

        k = 0
        # region 目前用不到
        # 第二次和第三次
        # for k in range(2):
        #     # 积分项部分
        #     # common=Ak * w[k, :].T - lk
        #     ee[k] = norm(Ak[:row, :col] * w[k, :col].T - lk[:row, :])
        #     integral += (Ak * w[k, :].T - lk)
        #
        #     val = pinAk * (-h * (Ak * w[k, :].T - lk))
        #     w[k + 1, :] = w[k, :] + val.T
        #     d = w[k, col:3 * col]
        #     t += tao
        #     print(t)
        #
        #     count = 0
        #     for val in w[k + 1, :col].tolist()[0]:
        #         if val < 0 or val > 2.75:
        #             count += 1
        #     print(f'{count}个格子不在约束范围内，占比为{count / col * 100:.2f}%\n')
        #     # Hk = self.H(d)
        #     Ak = self.A(d)
        #     lk = self.b
        #     pinAk = pinv(self.H(d))

        # for k in range(total - 1):
        #     # 积分项
        #     ee[k] = norm(Ak[:row, :col] * w[k, :col].T - lk[:row, :])
        #     integral += (Ak * w[k, :].T - lk)
        #
        #     # val = pinAk * (- h * (Ak * w[k, :].T - lk) - r * tao * integral)
        #     val = pinAk * tao * (- lamda * (Ak * w[k, :].T - lk) - gama * (Ak * w[k, :].T - lk + lamda * integral))
        #
        #     w[k + 1, :] = w[k, :] + val.T
        #     d = w[k+1, col:3 * col]
        #
        #     t += tao
        #     print(t)
        #
        #     count = 0
        #     for val in w[k + 1, :col].tolist()[0]:
        #         if val < 0 or val > 2.75:
        #             count += 1
        #     print(f'{count}个格子不在约束范围内，占比为{count / col * 100:.2f}%\n')
        #     # Hk = self.H(d)
        #     Ak = self.A(d)
        #     lk = self.b
        #     pinAk = pinv(self.H(d))
        # endregion
        old_norm = 0

        # 循环开始
        for i in range(outer_layer_cycle):
            for j in range(inner_layer_cycle):
                k = i * inner_layer_cycle + j

                # 积分项
                ee[k] = norm(Ak * w[k, :].T - lk)
                eexiao[k] = norm(Ak[:row, :col] * w[k, :col].T - lk[:row, :])
                integral += (Ak * w[k, :].T - lk)

                # 后半部分
                val = pinAk * ((Ak * w[k, :].T - lk) - gama * integral)
                # 组合
                w[k + 1, :] = w[k, :] - val.T

                t += tao
                # print(t)

                # region 在内部强制限制一下
                # for no, limit_value in enumerate(array(w[k + 1, :col])[0]):
                #     if limit_value < 0:
                #         w[k + 1, no] = 0
                #     elif limit_value > up:
                #         w[k + 1, no] = up
                # endregion

            # region 打印区间范围内的格子数目
            # count = 0
            # for i in array(w[k+1, :col])[0]:
            #     if 0 <= int(i) <= up:
            #         count += 1
            #     else:
            #         print(i)
            # print("数目:", count, "总数：", col)
            # print("两者是否相等:", count == col)
            # endregion

            # 每次结果的c要更新结果的d
            d = w[k + 1, col:3 * col]
            Ak = matrix(self.A(d))
            pinAk = pinv(self.A(d))

            # 整体的二范数
            print("二范数：", norm(Ak * w[k + 1, :].T - lk))

            # 只针对最原始的数据（基本+平滑性）的二范数
            new_norm = norm(Ak[:row, :col] * w[k + 1, :col].T - lk[:row, :])
            print("小二范数：", new_norm)
            # todo 暂时注释
            # 如果满足两次结果差值在1e-6内，则提前退出循环
            if abs(old_norm - new_norm) < 1e-6:
                print("两次误差小于1e-6,退出")
                break

            # region 疑似是空洞的数目
            # count = 0
            # for i in array(w[k + 1, :col])[0]:
            #     if 1.1 <= int(i) <= 2.5:
            #         count += 1
            #     else:
            #         print(i)
            # print("疑似是空洞的数目:", count)
            # endregion

        k += 1
        print("运行了", k, "次")

        # 记录最后一次的数据
        ee[k] = norm(Ak * w[k, :].T - lk)
        eexiao[k] = norm(Ak[:row, :col] * w[k, :col].T - lk[:row, :])

        # 循环结束（这里是指最后一次的数据也记录完了）
        # region 此处删除不需要的大数据
        del Ak, pinAk, lk
        # endregion

        # 记录数据
        # 使用时间信息来创建文件，以使文件名是唯一
        now_time = datetime.now()
        with open(
                root_path + r'\data\compare\no_noise\big_norm_' + now_time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + str(
                    tao), 'w') as wda, open(
            root_path + r'\data\compare\no_noise\small_norm_' + now_time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + str(
                tao), 'w') as wxiao:
            for value_da, value_xiao in zip(ee[:k + 1], eexiao[:k + 1]):
                wda.write(f'{value_da}\n')
                wxiao.write(f'{value_xiao}\n')

        try:
            with open(root_path + r'\data\compare\no_noise\\' + now_time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + str(
                    tao), 'w') as d:
                for value in array(w[k, :col])[0]:
                    d.write(f'{value}\n')
        except Exception as e:
            print(e)

        print("最终二范数:", ee[k])
        print("最终小二范数:", eexiao[k])
        count = 0
        for i in array(w[k, :col])[0]:
            if low <= float(i) <= up:
                count += 1
        print("数目:", count, "总数：", col)
        print("两者是否相等:", count == col)

        # region 此处删除不需要的大数据
        del w
        # endregion

        timee = [val * tao for val in range(k + 1)]
        plt.rcParams['font.family'] = ['STFangsong']
        plt.subplot(2, 1, 1)
        plt.title(f"二范数 tao={tao}")
        plt.xlabel("时间")
        plt.ylabel("误差的二范数")
        plt.plot(timee, ee[:k + 1])
        plt.subplot(2, 1, 2)
        plt.title(f"二范数 tao={tao}")
        plt.xlabel("时间")
        plt.ylabel("误差的二范数")
        plt.plot(timee, eexiao[:k + 1])
        plt.show()

        end = time.time()
        print("用时：", end - start)


def main():
    with open(root_path + r'\data\input\mesh1_copy.txt', 'r') as r:
        line = r.readline().strip().split()
        a, b, c = [int(i) for i in line]
    r = rnn(a, b, c)
    number = 0
    # for init_value in [0.0, -1000.0, 1000.0, ]:
    for init_value in [0.0]:
        r.solver(init_value, 50, 20, number)
        number += 1


# r.solver(0.1, 1, 2)

main()
