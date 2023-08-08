from now_used.config import mesh


def getabc():
    with open(mesh, 'r') as r:
        line = r.readline().strip().split()
        a, b, c = [int(i) for i in line]

    return a,b,c