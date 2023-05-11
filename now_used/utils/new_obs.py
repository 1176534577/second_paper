from math import ceil

from now_used.utils.base import root_path

with open(root_path+r"\data\input\dataset2", 'r') as d, open(root_path+r"\data\input\new_dataset2", 'w') as dd:
    d_line = d.readline()
    # int(48000/23)=2086
    dd.write(f'{ceil(int(d_line) / 23)}')
    dd.write('\n')
    # flag = 0
    while (d_line := d.readline()) != '':
        dd.write(d_line)
        for _ in range(22):
            d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
        # d.readline()
    # print('第一行'+d_line)
    # print('第二行'+d.readline())
    # print('第三行'+d.readline())
    # if flag == 0:
    #     dd.write(d_line)
    #     flag = 1
    # elif flag == 1:
    #     flag = 2
    # else:
    #     flag = 0
