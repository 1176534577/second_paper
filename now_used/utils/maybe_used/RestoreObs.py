with open(r'..\..\data\input\obs.dat', 'r') as r, open(r'..\..\data\input\new_obs.dat', 'w') as w:
    w.write(r.readline())

    while True:
        line = r.readline()
        list = line.strip().split()
        if list[0] == '1':
            list[2] = '-0.1'
            string = " ".join(list)
            w.write(f'{string}\n')
        else:
            w.write(line)
            break

    while (line := r.readline()) != '':
        w.write(line)
