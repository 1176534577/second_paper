import os


class Config:
    row_data = None
    air_cell_path = None
    mesh = None
    obs = None
    obs_temp = None
    MA_random = None
    MA_constant = None
    MA_free = None
    SA_all_res = None
    GA_all_res = None
    CG_all_res = None
    ray_way_j = None
    ijg = None
    abnormal_cell_path = None
    algorithm_type = 1
    dataset = ''

    # VITAL 修改此处
    # 是否重新生成obs，当前全部自己手动实现
    regenerate_obs = True
    # 是否重新生成ijg,ray_way_j，当前全部自己手动实现
    regenerate_ijg_ray_way_j = True

    # 算法类型1-6
    @staticmethod
    def setAlgorithmType(algorithm_type):
        Config.algorithm_type = algorithm_type

    # 数据集1-4
    @staticmethod
    def setDataset(dataset_no):
        directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        root_path = directory_path + r'\data'
        root_path_input = root_path + r'\input'
        root_path_output = root_path + r'\output'
        root_path_rawData = root_path + r'\rawData'

        # 模型大小不变，空气编号就不变
        Config.air_cell_path = root_path_output + r'\air_cell'
        # 异常区体素，同一种构型，只是内部的异常区密度不同
        Config.abnormal_cell_path = root_path_output + r'\abnormal_cell'

        Config.dataset = r'\dataset' + str(dataset_no)
        # 原生
        Config.row_data = root_path_rawData + Config.dataset
        # 输入
        root_path_input_dataset = root_path_input + Config.dataset

        Config.mesh = root_path_input_dataset + r'\mesh'
        Config.obs_temp = root_path_input_dataset + r'\obs_temp'
        Config.obs = root_path_input_dataset + r'\obs'

        # 输出
        root_path_output_dataset = root_path_output + Config.dataset



        Config.ijg = root_path_output_dataset + r'\ijg'
        Config.ray_way_j = root_path_output_dataset + r'\ray_way_j'

        Config.CG_all_res = root_path_output_dataset + r'\CG\all_res_'
        Config.GA_all_res = root_path_output_dataset + r'\GA\all_res_'
        Config.SA_all_res = root_path_output_dataset + r'\SA\all_res_'

        # MA=MyAlgorithm
        root_path_output_dataset_MA = root_path_output_dataset + r'\MyAlgorithm'

        Config.MA_free = root_path_output_dataset_MA + r'\noise_free'
        Config.MA_constant = root_path_output_dataset_MA + r'\noise_constant'
        Config.MA_random = root_path_output_dataset_MA + r'\noise_random'
