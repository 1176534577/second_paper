from sympy import Matrix

# from numpy import matrix
# from now_used.config import ray_way_j
from now_used.config_new import Config


# import os.path


def return_b():
    m = []
    with open(Config.ray_way_j, 'r') as d:
        while (d_line := d.readline()) != '':
            m.append(float(d_line.strip()))
    return Matrix(m)

# class a:
#     def __new__(cls, *args, **kwargs):
#         pass