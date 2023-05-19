from now_used.algorithm_factory import AlgorithmFactory
from now_used.pre_data.new_obs import generate_obs
from now_used.pre_data import generate_ijg_ray_way_j

# 生成新的obs，是否生成看base里的值
generate_obs()

# 生成新的ijg、ray_way_j，是否生成看base里的值
generate_ijg_ray_way_j.main()

# dataset_no 数据集编号 1-4
# type 算法类型 1-6
AlgorithmFactory().main()
