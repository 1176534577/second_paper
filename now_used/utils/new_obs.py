with open(r"../../data/input/obs.dat", 'r') as d, open(r"../../data/input/new_obs1.dat", 'w') as dd:
    d_line = d.readline()
    dd.write(f'{int(int(d_line) / 8)}')
    dd.write('\n')
    # flag = 0
    while (d_line := d.readline()) != '':
        dd.write(d_line)
        d.readline()
        d.readline()
        d.readline()
        d.readline()
        d.readline()
        d.readline()
        d.readline()
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
