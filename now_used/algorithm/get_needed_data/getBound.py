from numpy import matrix

from now_used.algorithm.get_needed_data.getA import getA


def get_Bound(my, mx, mz, dadengyu, xiaodengyu):
    """
    根据格子编号的顺序来写入bounds,四棱柱的约束是[0,3]

    :return:
    """
    # 单例
    a=getA.get_instance(my,mx,mz)
    # 被射线穿过的体素数量
    col=a.return_col()
    # 下限
    down_limit= [dadengyu] * col
    # 上限
    up_limit= [xiaodengyu] * col
    return matrix(down_limit).T,matrix(up_limit).T




