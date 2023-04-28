"""
 TOPIC 从求解结果到最终所有格子的结果
"""



from now_used.algorithm.get_needed_data.getA import getA
from now_used.utils.base import root_path

my, mx, mz = 13, 14, 10

a = getA(13, 14, 10)
ans = [2.65] * a.return_cell_total()

# 空气
with open(root_path + r'\data\output\air_cell', 'r') as r:
    while (r_line := r.readline()) != '':
        ans[int(r_line.strip().split()[0]) - 1] = 0

ss = a.return_newtoold_col()

sss = list(a.return_oldtonew_col().keys())
col = a.return_col()

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

index = 0
type = 1
if type == 1:
    noise_type = r'\no_noise'
elif type == 2:
    noise_type = r'\constant_noise'
else:
    noise_type = r'\noise_random'

suf = r'\3_11_18_56_14_0.2_0'
with open(root_path + r'\data\compare' + noise_type + suf, 'r') as r:
    while (line := r.readline()) != '':
        val = float(line.strip().split()[0])
        ans[ss[index] - 1] = val
        index += 1
with open(root_path + r'\data\output' + noise_type + r'\res_' + suf[1:], 'w') as w:
    for value in ans:
        w.write(f'{value}\n')
