from datetime import datetime
from algorithm.ComputationalNeuralDynamicsAlgorithm import paper_noise_free, paper_noise_constant, paper_noise_random
from utils import fromAnsgeneDen, LineChart, LineChart1, CompaerTable, air_cell_abnormal_cell

"""
new_obs.dat
mesh
new_ijg
\data\compare 代码的结果，部分格子的密度
\data\output res所有格子的密度 res_without_outside_除去外部格子的剩余格子的密度
"""


def main(type):
    now_time = datetime.now()
    tao = 0.2
    suf = now_time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + str(tao)
    # type = 1

    if type == 1:
        # 主函数，存储所有的数据
        paper_noise_free.main(suf)
    elif type == 2:
        paper_noise_constant.main(suf)
    elif type == 3:
        paper_noise_random.main(suf)
    else:
        raise ValueError('type只能是1，2，3')

    # 存储空气都位置，已经在getA的里面完成，因此此处不需要
    # air_cell_abnormal_cell.get_air()
    # 存储异常区的位置
    air_cell_abnormal_cell.get_empty_hole()

    # 转化为最终meshTool需要的数据
    fromAnsgeneDen.main(type, suf)
    # 密度与数量图
    LineChart.main(type, suf)
    # 迭代次数与二范数
    LineChart1.main(tao, type, suf)
    # 表格对比
    CompaerTable.main(type, suf)


if __name__ == '__main__':
    for type in [ 3]:
        main(type)
