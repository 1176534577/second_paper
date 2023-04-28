"""
 TOPIC 密度与数量图
"""

from math import log10

from matplotlib import pyplot as plt

from now_used.utils.base import root_path

fontsize = 50
length = 12
width = 9

amount = 200


def noise_free():
    ans = []
    with open(r'..\..\data\output\final_need_my_2', 'r') as r:
        while (line := r.readline()) != '':
            ans.append(float(line))
    max_val = max(ans)
    min_val = min(ans)

    length = max_val - min_val

    size = length / amount

    res = [0] * amount
    for i in ans:
        if i == max_val:
            res[-1] += 1
            continue
        index = int((i - min_val) // size)
        res[index] += 1
    return min_val, size, res


# another_ans=[2]*24+[2.65]*1296
def noise_constant():
    another_ans = []
    with open(root_path+r'\data\output\final_need_my_2', 'r') as r:
        while (line := r.readline()) != '':
            another_ans.append(float(line))
    max_val = max(another_ans)
    min_val = min(another_ans)

    lenngth = max_val - min_val
    size = lenngth / 100

    another_res = [0] * 100
    for i in another_ans:
        if i == max_val:
            another_res[-1] += 1
            continue
        index = int((i - min_val) // size)
        another_res[index] += 1
    return min_val, size, another_res


# 随机噪声
def noise_random():
    noise_random_ans = []
    with open(r'..\..\data\output\final_need_my_2', 'r') as r:
        while (line := r.readline()) != '':
            noise_random_ans.append(float(line))
    max_val = max(noise_random_ans)
    min_val = min(noise_random_ans)

    lenngth = max_val - min_val
    size = lenngth / 100

    noise_random_res = [0] * 100
    for i in noise_random_ans:
        if i == max_val:
            noise_random_res[-1] += 1
            continue
        index = int((i - min_val) // size)
        noise_random_res[index] += 1
    return min_val, size, noise_random_res


def plot(min_val, size, res, name):
    # 横坐标
    abscissa = [0.0] * amount
    for i in range(amount):
        abscissa[i] = min_val + (0.5 + i) * size

    res1 = [log10(val) if val > 0 else val for val in res]
    # another_res1=[log10(val) if val>0 else val for val in another_res]
    # noise_random_res1=[log10(val) if val>0 else val for val in noise_random_res]
    # 设置图片大小
    plt.figure(figsize=(length, width))

    plt.rcParams['font.family'] = ['STFangsong']
    plt.xlabel("密度(g/cm$^3$)", fontsize=fontsize)
    plt.ylabel("log$_{10}$数量", fontsize=fontsize)
    # 坐标轴刻度大小
    plt.tick_params(labelsize=fontsize)
    # plt.plot(abscissa, res)
    # plt.plot(abscissa, res1,label='无噪声')
    # plt.plot(abscissa, res,'o',mfc='w',label='无噪声')
    plt.plot(abscissa, res1, label=name)
    # plt.plot(abscissa,another_res,'+',label='恒定噪声')
    plt.axvline(2.65, ls='--', c='orange', label='参考值2.65')
    # plt.axvline(2.65, ls='--', c='r',label='参考值2.65')
    plt.legend(loc="upper left", fontsize=fontsize)
    # plt.plot(abscissa, another_res1)

    plt.tight_layout()
    # VITAL 保存矢量图到文件
    # plt.savefig(name + '.svg', dpi=600, format='svg')
    plt.show()


def main(flag_free, flag_cosntant, free_random):
    if flag_free:
        min_val, size, res = noise_free()
        plot(min_val, size, res, '无噪声')
    if flag_cosntant:
        min_val, size, res = noise_constant()
        plot(min_val, size, res, '恒定噪声')
    if free_random:
        min_val, size, res = noise_random()
        plot(min_val, size, res, '随机噪声')

# 1执行，0不执行
main(1,0,0)