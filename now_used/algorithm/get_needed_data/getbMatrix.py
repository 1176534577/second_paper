from sympy import Matrix
# import os.path

# from numpy import matrix
from now_used.utils.base import root_path


def return_b():
    m = []
    with open(root_path + r'\data\output\ray_way_j', 'r') as d:
        while (d_line := d.readline()) != '':
            m.append(float(d_line.strip()))
    return Matrix(m)

# class a:
#     def __new__(cls, *args, **kwargs):
#         pass