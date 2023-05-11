from datetime import datetime

from algorithm.ComputationalNeuralDynamicsAlgorithm import paper_noise_free, paper_noise_constant, paper_noise_random
from now_used.algorithm.ConjugateGradient import CG
from now_used.algorithm.GeneticAlgorithm import GA
from now_used.algorithm.SimulatedAnnealing import SA
from now_used.utils.base import type
from utils import fromAnsgeneDen, LineChart, LineChart1, CompaerTable, air_cell_abnormal_cell

"""
new_obs.dat
mesh
new_ijg
路径解释见README.md
"""


class AlgorithmFactory:
    def __init__(self):
        pass

    def execute(self):

        now_time = datetime.now()
        tao = 0.2
        suf = now_time.strftime('%Y_%m_%d_%H_%M_%S')
        # type = 1

        if type == 1:
            subclass = paper_noise_free.rnn()
            # 主函数，存储所有的数据
            # paper_noise_free.main(dataset_no, suf)
        elif type == 2:
            subclass = paper_noise_constant.rnn()
        elif type == 3:
            subclass = paper_noise_random.rnn()
        elif type == 4:
            subclass = CG()
        elif type == 5:
            subclass = GA()
        elif type == 6:
            subclass = SA()
        else:
            raise ValueError("type值错误")

        # 主流程
        subclass.main(suf)
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

# if __name__ == '__main__':
#     for type in [3]:
#         main(type)
