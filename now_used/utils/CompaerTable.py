"""
 TOPIC 表格对比
"""

import numpy as np

from now_used.utils.base import root_path


"""def get_air(save=True):
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
        with open(root_path + r'\data\output\air_cell', 'w') as w:
            for val in air_cell:
                w.write(f'{val}\n')

    return air_cell"""


"""def get_empty_hole(save=True):
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
        with open(root_path + r'\data\output\abnormal_cell', 'w') as w:
            for val in abnormal_cell:
                w.write(f'{val}\n')
    
    return abnormal_cell"""


def main(typeSuf):
    value_abnormal = []
    value_normal = []
    # with open(r'..\..\compare\data\output\res_tao_test_8_31_anneal','r') as r:
    # with open(r'..\..\compare\data\gongetidu_9_29','r') as r:

    # 内部异常区
    empty_hole=[]
    with open(root_path + r'\data\output\abnormal_cell', 'r') as r:
        while (r_line := r.readline()) != '':
            empty_hole.append(float(r_line))

    # 外部空气
    air_cell=[]
    with open(root_path + r'\data\output\air_cell', 'r') as r:
        while (r_line := r.readline()) != '':
            air_cell.append(float(r_line))

    # 将最终结果（所有的格子）传入
    # with open(r'..\..\data\output\final_need_you_1', 'r') as r:
    with open(r'..\..\data\output'+typeSuf, 'r') as r:
        index = 1
        while (r_line := r.readline()) != '':
            if index in empty_hole:
                # 异常区
                value_abnormal.append(float(r_line.strip().split()[0]))
            elif index not in air_cell:
                # 非异常区，除去空气
                value_normal.append(float(r_line.strip().split()[0]))
            index += 1

    # 减1、减2.65是为了二范数
    new_value_abnormal = [val - 1 for val in value_abnormal]
    new_value_normal = [val - 2.65 for val in value_normal]
    print(f'异常区 {np.linalg.norm(new_value_abnormal):.4}')
    print(f'非异常区 {np.linalg.norm(new_value_normal):.4}')



# main()
