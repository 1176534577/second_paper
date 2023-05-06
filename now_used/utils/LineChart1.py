"""
 topic 迭代次数与二范数
"""

from matplotlib import pyplot as plt

# plt.rc('font',size=7)
from now_used.utils.base import root_path

fontsize = 50
length = 12
width = 9


def noise_free(fileName):
    k = 1000
    ans = []
    with open(root_path + r'\data\compare\noise_free' + fileName, 'r') as r:
        while (line := r.readline()) != '':
            ans.append(float(line))
    return k, ans


def noise_constant(fileName):
    k = 1000
    another_ans = []
    with open(root_path + r'\data\compare\noise_constant' + fileName, 'r') as r:
        while (line := r.readline()) != '':
            another_ans.append(float(line))
    return k, another_ans


def noise_random(fileName):
    k = 2000
    noise_random = []
    with open(root_path + r'\data\compare\noise_random' + fileName, 'r') as r:
        while (line := r.readline()) != '':
            noise_random.append(float(line))
    return k, noise_random


def plot(k, array, name):
    tao = 0.1

    timee = [val * tao for val in range(k + 1)]

    # 设置图片大小
    plt.figure(figsize=(length, width))

    ax = plt.gca()
    ax.yaxis.get_offset_text().set(size=fontsize)  # 左上角
    # plt.rcParams['font.family'] = ['STFangsong']
    plt.rcParams['font.sans-serif'] = ['STFangsong']
    plt.xlabel('迭代次数$k$', fontsize=fontsize)
    plt.ylabel(r'$||\varepsilon_k||_2$', fontsize=fontsize)
    plt.tick_params(labelsize=fontsize)

    plt.plot(timee, array, label=name)
    plt.tight_layout()
    plt.savefig(name + '.svg', dpi=600, format='svg')

    # plt.plot(timee,ans)

    # plt.plot(timee,another_ans,label='恒定噪声右')
    # plt.savefig('恒定噪声右.svg', dpi=600, format='svg')
    #
    # plt.plot(timee, noise_random,label='随机噪声右')
    # plt.savefig('随机噪声右.svg', dpi=600, format='svg')

    # plt.legend(loc="upper right")
    plt.show()


def main(type, suf):
    fileName = r'\small_norm_' + suf
    if type == 1:
        k, array = noise_free(fileName)
        plot(k, array, '无噪声右')
    elif type == 2:
        k, array = noise_constant(fileName)
        plot(k, array, '恒定噪声右')
    elif type == 3:
        k, array = noise_random(fileName)
        plot(k, array, '随机噪声右')
    else:
        raise ValueError('type只能是1，2，3')

# 1执行，0不执行
# main(1,0,0)
