"""
 TOPIC 计算空气格子和异常区格子编号，从1开始
"""
from now_used.utils.base import air_cell_path, abnormal_cell_path


def get_air(save=True):
    # 空气
    air_cell = set()

    # with open(r'..\data\output\air_cell','r') as r:
    #     while (line:=r.readline())!='':
    #         air_cell.add(int(line))
    # my, mx, mz = 17,22,10
    my, mx, mz = 13, 14, 10
    # 为了满足探测器的需求，周围一圈是空气格子，探测器位于空气格子之中
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

    # 存入文件，下次不需要再读 以下代码还未改
    if save:
        with open(air_cell_path, 'w') as w:
            for val in air_cell:
                w.write(f'{val}\n')

    # return air_cell


def get_empty_hole(save=True):
    my, mx, mz = 13, 14, 10

    ylist = [7, 8, 9]
    xlist = [5, 6, 7, 8]
    zlist = [3, 4]

    # 空洞的编号，叫做密度异常体更合适些
    abnormal_cell = []

    for y in ylist:
        for x in xlist:
            for z in zlist:
                abnormal_cell.append(x * my * mz + y * mz + z + 1)

    if save:
        with open(abnormal_cell_path, 'w') as w:
            for val in abnormal_cell:
                w.write(f'{val}\n')

    # return abnormal_cell
