from Calcu_sensitivity_paper import Calcsensitivity

# from Paper.paper_shibubian1_copy import rnn


# class Loger:
#     def write(self, value):
#         print(value)
from now_used.utils.base import root_path

process = True

num=2
root_path_input=root_path+r'\data\input\dataset'+str(num)
root_path_output=root_path+r'\data\output\dataset'+str(num)

if process:
    # loger = Loger()
    Calcsensitivity(root_path_input + r"\dataset",
                    root_path_input + r"\mesh.txt").calcsensitivity(
        ijf=root_path_output + r"\ijg",
        Ray_way_j_file=root_path_output + r"\ray_way_j", )
# else:
#     a = rnn(13, 14, 10)
#     a.solver(tao=0.01, total=100)
