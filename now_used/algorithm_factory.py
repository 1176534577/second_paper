from datetime import datetime

from algorithm.ComputationalNeuralDynamicsAlgorithm import paper_noise_free, paper_noise_constant, paper_noise_random
from now_used.algorithm.commonAlgorithm import commonAlgorithm
from now_used.config import algorithm_type, dataset_no
from utils import fromAnsgeneDen, LineChart, LineChart1, air_cell_abnormal_cell

"""
new_obs.dat
mesh
new_ijg
路径解释见README.md
"""


class AlgorithmFactory:
    def __init__(self):
        pass

    # 方法入口
    def main(self):
        myDict = {1: "无噪声", 2: "恒定噪声", 3: "随机噪声", 4: "共轭梯度法", 5: "遗传算法", 6: "模拟退火法"}
        print("算法类型：" + myDict.get(algorithm_type))
        print("数据集：" + str(dataset_no))
        self.selector()

    def selector(self):
        if algorithm_type == 1:
            subclass = paper_noise_free.rnn()
            # 主函数，存储所有的数据
            # paper_noise_free.main(dataset_no, suf)
        elif algorithm_type == 2:
            subclass = paper_noise_constant.rnn()
        elif algorithm_type == 3:
            subclass = paper_noise_random.rnn()
        elif algorithm_type == 4:
            from now_used.algorithm.ConjugateGradient import CG
            subclass = CG()
        elif algorithm_type == 5:
            from now_used.algorithm.GeneticAlgorithm import GA
            subclass = GA()
        elif algorithm_type == 6:
            from now_used.algorithm.SimulatedAnnealing import SA
            subclass = SA()
        else:
            raise ValueError("type值只能是1-6")
        self.execute(subclass)

    def execute(self, subclass: commonAlgorithm):
        now_time = datetime.now()
        tao = 0.2
        suf = now_time.strftime('%Y_%m_%d_%H_%M_%S')
        # 主流程
        subclass.main(suf)
        # if algorithm_type < 4:
        #     # 存储空气的位置，已经在getA的里面完成，因此此处不需要
        #     # air_cell_abnormal_cell.get_air()
        #     # 存储异常区的位置
        #     air_cell_abnormal_cell.get_empty_hole()
        #
        #     # 转化为最终meshTool需要的数据
        #     fromAnsgeneDen.main(algorithm_type, suf)
        #     # 密度与数量图
        #     LineChart.main(algorithm_type, suf)
        #     # 迭代次数与二范数
        #     LineChart1.main(tao, algorithm_type, suf)

        # 表格对比，待修改，10次的值
        # CompaerTable.main(type, suf)

# if __name__ == '__main__':
#     for type in [3]:
#         main(type)
