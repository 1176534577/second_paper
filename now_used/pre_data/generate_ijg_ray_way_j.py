from now_used.pre_data.Calcu_sensitivity import Calcsensitivity

# from Paper.paper_shibubian1_copy import rnn


# class Loger:
#     def write(self, value):
#         print(value)
from now_used.utils.base import obs, mesh, ijg, ray_way_j, regenerate_ijg_ray_way_j


# num=2
# root_path_input=root_path+r'\data\input\dataset'+str(num)
# root_path_output=root_path+r'\data\output\dataset'+str(num)
def main():
    if regenerate_ijg_ray_way_j:
        # loger = Loger()
        Calcsensitivity(obsf=obs, meshf=mesh).calcsensitivity(ijf=ijg, Ray_way_j_file=ray_way_j)
# else:
#     a = rnn(13, 14, 10)
#     a.solver(tao=0.01, total=100)
