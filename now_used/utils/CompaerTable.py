"""
 TOPIC 表格对比，改这里就行了
"""

import numpy as np

from now_used.config import abnormal_cell_path, air_cell_path, MA_free, MA_constant, MA_random, CG_all_res, \
    GA_all_res, SA_all_res

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


def main(type, suf):
    value_abnormal = []
    value_normal = []
    # with open(r'..\..\compare\data\output\res_tao_test_8_31_anneal','r') as r:
    # with open(r'..\..\compare\data\gongetidu_9_29','r') as r:

    # 内部异常区
    empty_hole = []
    with open(abnormal_cell_path, 'r') as r:
        while (r_line := r.readline()) != '':
            empty_hole.append(float(r_line))

    # 外部空气
    air_cell = []
    with open(air_cell_path, 'r') as r:
        while (r_line := r.readline()) != '':
            air_cell.append(float(r_line))

    if type == 1:
        path = MA_free
    elif type == 2:
        path = MA_constant
    elif type == 3:
        path = MA_random
    elif type == 4:
        path = CG_all_res
    elif type == 5:
        path = GA_all_res
    elif type == 6:
        path = SA_all_res
    else:
        raise ValueError('type值只能说1-6')

    ans_normal = []
    ans_abnormal = []

    n = 10
    for _ in range(n):
        # todo 更改以下部分
        # 将最终结果（所有的格子）传入
        # with open(r'..\..\data\output\final_need_you_1', 'r') as r:
        with open(path + suf + r'\all_res', 'r') as r:
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

        ans_normal.append(np.linalg.norm(new_value_normal))
        ans_abnormal.append(np.linalg.norm(new_value_abnormal))

    # 保留四位小数
    print(f'非异常区 {sum(ans_normal) / n:.4}')
    print(f'异常区 {sum(ans_abnormal) / n:.4}')

# main()
