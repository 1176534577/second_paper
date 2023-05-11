# id, y0, x0, z0, theta0, phi0, d
from math import ceil

from now_used.utils.base import root_path

num = 2
root_path += r'\data\input\dataset' + str(num)

w = open(root_path + r'\dataset', 'w')
w.write(f'{ceil(int(48000) / 23)}\n')
n = 12000
i = 0
# 12000个
with open(root_path + r'\LRC_thetaphi-D1.dat', 'r') as r1:
    r1.readline()
    for _ in range(n):
        a = r1.readline()
        if i % 23 == 0:
            a = a.strip().split()[0:3]
            w.write(f'1 0 10.1 0 {a[1]} {a[0]} {a[2]}\n')
        i += 1
# 12000个
with open(root_path + r'\LRC_thetaphi-D2.dat', 'r') as r1:
    r1.readline()
    for _ in range(n):
        a = r1.readline()
        if i % 23 == 0:
            a = a.strip().split()[0:3]
            w.write(f'2 -7.6 0 0 {a[1]} {a[0]} {a[2]}\n')
        i += 1

# 12000个
with open(root_path + r'\LRC_thetaphi-D3.dat', 'r') as r1:
    r1.readline()
    for _ in range(n):
        a = r1.readline()
        if i % 23 == 0:
            a = a.strip().split()[0:3]
            w.write(f'3 0 -10.1 0 {a[1]} {a[0]} {a[2]}\n')
        i += 1
# 12000个
with open(root_path + r'\LRC_thetaphi-D4.dat', 'r') as r1:
    r1.readline()
    for _ in range(n):
        a = r1.readline()
        if i % 23 == 0:
            a = a.strip().split()[0:3]
            w.write(f'4 7.6 0 0 {a[1]} {a[0]} {a[2]}\n')
        i += 1

w.close()
