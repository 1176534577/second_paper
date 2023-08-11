from now_used.algorithm_factory import AlgorithmFactory
import time

# from now_used.pre_data.generate_obs.new_obs import generate_obs
# from now_used.pre_data import generate_ijg_ray_way_j

# 生成新的obs，是否生成看base里的值
# generate_obs()

# 生成新的ijg、ray_way_j，是否生成看base里的值
# generate_ijg_ray_way_j.main()

# 实施方法
# algorithm_type 算法类型 1-6
# dataset_no 数据集编号 1-4
for algorithm_type in range(4, 7):
    for dataset_no in range(1, 5):
        for _ in range(3):
            try:
                AlgorithmFactory().main(algorithm_type, dataset_no)
            except Exception as e:
                print(e)
            time.sleep(3)
