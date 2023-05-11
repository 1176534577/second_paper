from Calcu_sensitivity import Calcsensitivity


# from Paper.paper_shibubian1_copy import rnn


class Loger:
    def write(self, value):
        print(value)


process = True

if process:
    loger = Loger()
    Calcsensitivity(r"data\input\new_obs.dat", r"data\input\mesh1_copy.txt").calcsensitivity(ijf=r"data\output\new_ijg",
                                                                                             Ray_way_j_file=r"data\output\ray_way_j",
                                                                                             loger=loger,
                                                                                             isprint=False)
# else:
#     a = rnn(13, 14, 10)
#     a.solver(tao=0.01, total=100)
