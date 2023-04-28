import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

# 定义编码长度
from Paper import getabc, getb
from Paper.AddGetA import getypinghua, getxpinghua, getzpinghua
from Paper.getA import getA

DNA_SIZE = 20
# 定义种群容量 即个体数量
POP_SIZE = 200
# 定义交叉概率，范围一般是0.6~1
CROSSOVER_RATE = 0.8
# 突变常数（又称为变异概率），通常是0.1或者更小。
MUTATION_RATE = 0.005
# 迭代次数
N_GENERATIONS = 1000
# x1,x2取值范围
# x_bound = [0, 5]
# y_bound = [0, 5]
bound = [0, 3]
# old=0

my, mx, mz = getabc.getabc()
instance = getA.get_instance(my, mx, mz)
A = instance.return_A_normal()
col = instance.return_col()
B = getb.return_b_normal()
Xref = np.matrix([2.65] * col).T
y_matrix = getypinghua()
x_matrix = getxpinghua()
z_matrix = getzpinghua()


# 定义适应度函数
def F(x):
    # A=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
    # B=np.matrix([14,32,50]).T

    if type(x[0]) == np.float64:
        X = np.matrix(x).T
        # return pow(np.linalg.norm(A * X - B), 2)
        # return pow(np.linalg.norm(A * X - B), 2) + 0.05 * (
        #         10 * np.linalg.norm(X - Xref) + 1 * np.linalg.norm(X - y_matrix * X) + 1 * np.linalg.norm(
        #     X - x_matrix * X) + 5 * np.linalg.norm(X - z_matrix * X))
        return pow(np.linalg.norm(A * X - B), 2) + 0.05 * (
            10 * pow(np.linalg.norm(X - Xref),2) + 1 * pow(np.linalg.norm(X - y_matrix * X),2) + 1 * pow(np.linalg.norm(
        X - x_matrix * X),2) + 5 * pow(np.linalg.norm(X - z_matrix * X),2))

    ans = [0] * POP_SIZE
    # length = len(x)
    for i in range(POP_SIZE):
        Xlist = [0] * col
        for j in range(col):
            Xlist[j] = x[j][i]
        X = np.matrix(Xlist).T
        # 平滑度用矩阵的方法
        ans[i]=pow(np.linalg.norm(A * X - B), 2) + 0.05 * (
            10 * pow(np.linalg.norm(X - Xref),2) + 1 * pow(np.linalg.norm(X - y_matrix * X),2) + 1 * pow(np.linalg.norm(
        X - x_matrix * X),2) + 5 * pow(np.linalg.norm(X - z_matrix * X),2))
        # ans[i] = pow(np.linalg.norm(A * X - B), 2) + 0.05 * (
        #         10 * np.linalg.norm(X - Xref) + 1 * np.linalg.norm(X - y_matrix * X) + 1 * np.linalg.norm(
        #     X - x_matrix * X) + 5 * np.linalg.norm(X - z_matrix * X))
    ans = np.array(ans)

    return -ans
    # duibi=(pow(1 * x[0] + 2 * x[1] + 3 * x[2] - 14, 2) + pow(4 * x[0] + 5 * x[1] + 6 * x[2] - 32, 2) + pow(7 * x[0] + 8 * x[1] + 9 * x[2] - 50,
    #                                                                                         2))
    # return 20 * x + 10 * y + 10 * x * y - np.exp(0.2 * x) - np.exp(0.3 * y)
    # return -(pow(1 * x[0] + 2 * x[1] + 3 * x[2] - 14, 2) + pow(4 * x[0] + 5 * x[1] + 6 * x[2] - 32, 2) + pow(7 * x[0] + 8 * x[1] + 9 * x[2] - 50,
    #                                                                                         2))


# 3d绘图
# def plot_3d(ax):
#     X = np.arange(*x_bound, 5)
#     Y = np.arange(*y_bound, 5)
#     X, Y = np.meshgrid(X, Y)  # 网格的创建
#     Z = F(X, Y)
#     # R = np.sqrt(X ** 2 + Y**2)
#     # Z = np.sin(R)\
#     # rstride:行之间的跨度 cstride:列之间的跨度 camp是颜色映射表
#     ax.plot_surface(X, Y, Z, rstride=20, cstride=20, alpha=0.5, cmap=plt.cm.coolwarm)
#     # 设置z轴的维度
#     ax.set_zlim(-40, 40)
#     # 坐标标签
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_zlabel('z')
#     plt.pause(3)
#     plt.show()


# 评价个体对环境的适应度 在MAX问题中适应度越大越有可能留下
def get_fitness(pop):
    x = translateDNA(pop)
    # pred是将可能解带入函数F中得到的预测值
    pred = F(x)
    return (pred - np.min(pred)) + 1e-3


# 减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)],最后在加上一个很小的数防止出现为0的适应度
# 解码环节 即将二进制按权展开为十进制，将转换后的实数压缩到[0，1]之间的小数，再将其映射到给定区间中即可
# pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
# 注：此处的DNA_SIZE即染色体长度 为24，两个实数共48位二进制，奇数24列为x的编码，偶数为y的
def translateDNA(pop):
    # x_pop = pop[:, ::unknown_num]  # 奇数列表示x1
    # y_pop = pop[:, 1::unknown_num]  # 偶数列表示x2
    # z_pop = pop[:, 2::unknown_num]

    ans = [0] * col
    for i in range(col):
        # ans[i] = pop[:, i * DNA_SIZE:(i + 1) * DNA_SIZE]
        ans[i] = pop[:, i::col]

    # pop:(POP_SIZE,DNA_SIZE)*(DNA_SIZE,1) --> (POP_SIZE,1) dot用于向量点积和矩阵乘法。
    # x = x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (bound[1] - bound[0]) + bound[0]
    # y = y_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (bound[1] - bound[0]) + bound[0]
    # z = z_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (bound[1] - bound[0]) + bound[0]

    ans_ = [0] * col
    for i in range(col):
        ans_[i] = ans[i].dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (bound[1] - bound[0]) + bound[
            0]

    return ans_


# 实现交叉和变异 同时将后代加入新种群中，输出新种群
def crossover_and_mutation(pop, CROSSOVER_RATE=0.8):
    new_pop = []
    for father in pop:  # 遍历种群中的每一个个体，将该个体作为父亲
        child = father  # 孩子先得到父亲的全部基因(指二进制中的0、1字符)
        if np.random.rand() < CROSSOVER_RATE:  # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
            mother = pop[np.random.randint(POP_SIZE)]  # 在种群中选择另一个个体，并将该个体作为母亲
            cross_points = np.random.randint(low=0, high=DNA_SIZE * col)  # 随机产生交叉的点
            child[cross_points:] = mother[cross_points:]  # 孩子得到位于交叉点后的母亲的基因
        mutation(child)  # 每个后代有一定的机率发生变异
        new_pop.append(child)  # 将后代加入新种群中
    return new_pop


# 后代变异函数
def mutation(child, MUTATION_RATE=0.003):
    if np.random.rand() < MUTATION_RATE:  # 以MUTATION_RATE的概率进行变异
        mutate_point = np.random.randint(0, DNA_SIZE * col)  # 随机产生一个实数，代表要变异基因的位置
        child[mutate_point] = child[mutate_point] ^ 1  # 将变异点的二进制为反转


# 选择留下的 不能单纯的选择适应度高的，否则会陷入局部最优而非全局最优
# 此处进行折中处理，即适应度越高的，被选择的机会越高，适应度低的，被选择的机会越低。
def select(pop, fitness):  # nature selection wrt pop's fitness

    # choice(a,size,replace,p)从一维array a 或 int 数字a 中，以概率p随机选取大小为size的数据，
    # replace表示是否重用元素，即抽取出来的数据是否放回原数组中，默认为true（抽取出来的数据有重复）
    # 轮盘赌选择法
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                           p=(fitness) / (fitness.sum()))
    return pop[idx]


# 输出
def print_info(pop):
    fitness = get_fitness(pop)
    max_fitness_index = np.argmax(fitness)
    print("max_fitness:", fitness[max_fitness_index])
    ans = translateDNA(pop)
    print("最优的基因型：", pop[max_fitness_index])
    # x1 = ans[0][max_fitness_index]
    # x2 = ans[1][max_fitness_index]
    # x3 = ans[2][max_fitness_index]
    # print("(x1, x2,x3):", (x1,x2,x3))

    x = [0] * col
    for no, val in enumerate(ans):
        x[no] = val[max_fitness_index]

    qian = 10
    print(f'前{qian}位:{x[:qian]}')
    new = F(x)
    print(new)
    if abs(new) < 1:
        return x, True
    return x, False


if __name__ == "__main__":
    # 创建一个画布 并转换为三维建图
    # fig = plt.figure()
    # ax = Axes3D(fig, auto_add_to_figure=False)
    # fig.add_axes(ax)
    # plt.ion()  # 将画图模式改为交互模式，程序遇到plt.show不会暂停，而是继续执行
    # plot_3d(ax)
    # 随机生成二进制码 即染色体

    total = DNA_SIZE * col
    # 改变写法，不符合人类思想
    pop = np.random.randint(2, size=(POP_SIZE - 1, total))
    add = [0] * total
    s = '11100010001000100001'
    for j in range(DNA_SIZE):
        add[j * col:(j + 1) * col] = [int(s[j])] * col
    pop = np.row_stack((pop, np.array(add)))

    index = 0
    for index in range(N_GENERATIONS):  # 迭代N代
        # while True:
        # 使用自定义translateDNA函数进行解码
        #     x, y = translateDNA(pop)
        # if 'sca' in locals():
        #     sca.remove()
        # 颜色是黑色，标记为●
        # sca = ax.scatter(x, y, F(x, y), c='black', marker='o')
        # plt.show()
        # plt.pause(0.1)
        # 交叉和变异

        # F_values = F(translateDNA(pop)[0], translateDNA(pop)[1])#x, y --> Z matrix
        #
        fitness = get_fitness(pop)
        pop = select(pop, fitness)  # 选择生成新的种群
        pop = np.array(crossover_and_mutation(pop, CROSSOVER_RATE))

        # print_info(pop)
        x, boolean = print_info(pop)
        if boolean:
            print(f"迭代{index + 1}代")
            break
        index += 1
        # plt.ioff()
        # plot_3d(ax)

    with open(r'data\output\ans_8_30_gene', 'w') as w:
        for val in x:
            w.write(f'{val}\n')
