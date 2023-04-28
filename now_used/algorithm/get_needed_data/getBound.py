from now_used.algorithm.get_needed_data.getA import getA
from numpy import matrix

def get_Bound(my, mx, mz, dadengyu, xiaodengyu):
    """
    根据格子编号的顺序来写入bounds,四棱柱的约束是[0,2.75]

    :return:
    """
    a=getA.get_instance(my,mx,mz)
    col=a.return_col()
    down_limit= [dadengyu] * col
    up_limit= [xiaodengyu] * col
    return matrix(down_limit).T,matrix(up_limit).T




