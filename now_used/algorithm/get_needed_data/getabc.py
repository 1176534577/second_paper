from now_used.utils.base import root_path


def getabc():
    with open(root_path+r'\data\input\mesh1_copy.txt', 'r') as r:
        line = r.readline().strip().split()
        a, b, c = [int(i) for i in line]

    return a,b,c