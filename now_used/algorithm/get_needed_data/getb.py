# from sympy import Matrix

from numpy import matrix

# from Paper.getA_temp import getA, count_less_and_equal_num
# from now_used.config import ray_way_j
from now_used.config_new import Config


def return_b(col):
    """
    加平滑性的，自己的算法（无噪声、恒定噪声、随机噪声）使用

    [h;a]
    :param col:
    :return:
    """
    # a = getA.get_instance(my, mx, mz)
    # li = count_less_and_equal_num(a.return_A(), 10)
    #

    # index = 0
    m = []
    with open(Config.ray_way_j, 'r') as d:
        while (d_line := d.readline()) != '':
            # 增加平滑性
            # value = float(d_line.strip())
            # if index < col:
            #     value += 1.325
            #     index += 1
            m.append(float(d_line.strip()))
    # m=numpy.delete(m,li,axis=0)
    for i in range(col):
        m.append(1.325)
    return matrix(m).T


def return_b_test():
    return matrix([[14], [32]])


def return_b_normal():
    """
    不加平滑性的，共轭梯度法、遗传算法、模拟退火法使用
    :return:
    """
    # a = getA.get_instance(my, mx, mz)
    # li = count_less_and_equal_num(a.return_A(), 10)
    #
    m = []
    with open(Config.ray_way_j, 'r') as d:
        while (d_line := d.readline()) != '':
            # 增加平滑性
            m.append(float(d_line.strip()))
    # m=numpy.delete(m,li,axis=0)
    return matrix(m).T

# class a:
#     def __new__(cls, *args, **kwargs):
#         pass
