# from now_used.config import mesh
from now_used.config_new import Config


def getabc():
    with open(Config.mesh, 'r') as r:
        line = r.readline().strip().split()
        a, b, c = [int(i) for i in line]

    return a,b,c