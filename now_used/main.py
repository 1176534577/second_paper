from datetime import datetime
from algorithm.ComputationalNeuralDynamicsAlgorithm import paper_noise_free,paper_noise_constant,paper_noise_random
from utils import fromAnsgeneDen, LineChart, LineChart1, CompaerTable, air_cell_abnormal_cell

"""
new_obs.dat
mesh1_copy.txt
new_ijg
"""

now_time = datetime.now()
tao = 0.2
suf = now_time.strftime('%Y_%m_%d_%H_%M_%S') + '_' + str(tao)
type = 1

if type==1:
    typeSuf = r"\noise_free_" + suf
    # 主函数，存储所有的数据
    paper_noise_free.main(suf)
elif type==2:
    typeSuf = r"\noise_constant_" + suf
    paper_noise_constant.main(suf)
elif type==3:
    typeSuf = r"\noise_random_" + suf
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
LineChart1.main(type, suf)
# 表格对比
CompaerTable.main(typeSuf)
