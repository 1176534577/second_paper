root_path = r'C:\Users\CHANG\Desktop\paper\second_paper\data'
root_path_input = root_path + r'\input'
root_path_output = root_path + r'\output'
# 模型大小不变，空气编号就不变
air_cell_path = root_path_output + r'\air_cell'

# VITAL 修改此处
# 算法类型1-6
type = 6
# 数据集1-4
dataset = r'\dataset1'

# 输入
mesh = root_path_input + dataset + r'\mesh'
# 输出
root_path_output_dataset = root_path_output + dataset

# 异常区体素
abnormal_cell_path = root_path_output_dataset + r'\abnormal_cell'

ijg = root_path_output_dataset + r'\ijg'
ray_way_j = root_path_output_dataset + r'\ray_way_j'

CG_all_res = root_path_output_dataset + r'\CG\all_res_'
GA_all_res = root_path_output_dataset + r'\GA\all_res_'
SA_all_res = root_path_output_dataset + r'\SA\all_res_'

# MA=MyAlgorithm
root_path_output_dataset_MA = root_path_output_dataset + r'\MyAlgorithm'
MA_free = root_path_output_dataset_MA + r'\noise_free\\'
MA_constant = root_path_output_dataset_MA + r'\noise_constant\\'
MA_random = root_path_output_dataset_MA + r'\noise_random\\'
