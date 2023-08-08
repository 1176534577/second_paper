"""
 TOPIC 从求解结果到最终所有格子的结果
"""

from now_used.algorithm.get_needed_data.getA import getA
from now_used.config import air_cell_path, MA_free, MA_constant, MA_random


# ylist = [7, 8, 9]
# xlist = [5, 6, 7, 8]
# zlist = [3, 4]

# region 空洞，即异常区坐标
# empty_hole = []
# for y in ylist:
#     for x in xlist:
#         for z in zlist:
#             empty_hole.append(x * my * mz + y * mz + z + 1)
# endregion

# count=0
# for i in empty_hole:
#     if i not in sss:
#         print(i)
#         count+=1

# print('======')
# print(len(empty_hole))
# print(count)


def main(type, suf):
    """

    :param type: 1为无噪声，2为常亮噪声，3为随机噪声
    :return:
    """

    my, mx, mz = 13, 14, 10

    a = getA(my, mx, mz)
    ans = [2.65] * a.return_cell_total()
    ans_without_outside = [2.65] * a.return_cell_total()

    # 外部空气
    with open(air_cell_path, 'r') as r:
        while (r_line := r.readline()) != '':
            ans[int(r_line.strip().split()[0]) - 1] = 0
            ans_without_outside[int(r_line.strip().split()[0]) - 1] = -2

    ss = a.return_newtoold_col()

    # sss = list(a.return_oldtonew_col().keys())
    # col = a.return_col()

    if type == 1:
        path = MA_free
    elif type == 2:
        path = MA_constant
    elif type == 3:
        path = MA_random
    else:
        raise ValueError('type只能是1，2，3')
    path += '\\'
    # now_time = datetime.now()

    # suf = r'\3_11_18_56_14_0.2_0'

    # 将压缩后的体素的编号还原为压缩前的编号
    with open(path + suf + r'\res', 'r') as r:
        index = 0
        while (line := r.readline()) != '':
            val = float(line.strip().split()[0])
            ans[ss[index] - 1] = val
            ans_without_outside[ss[index] - 1] = val
            index += 1

    # 每个体素的密度写入文件
    with open(path + suf + r'\all_res', 'w') as w:
        for value in ans:
            w.write(f'{value}\n')

    # 除去外部空气的每个体素的密度写入文件
    with open(path + suf + r'\res_without_air', 'w') as w:
        for value in ans_without_outside:
            if value != -2:
                w.write(f'{value}\n')

# main(1)
