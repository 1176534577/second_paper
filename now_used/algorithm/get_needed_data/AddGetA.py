import numpy as np

# from Paper.getabc import getabc

def getPos(my, mx, mz,i):
    x = i / (my * mz)
    i %= (my * mz)
    y = i / mz
    z = i % mz
    return int(y), int(x), int(z)

def getpinghua(col):
    my, mx, mz = 11,12,10
    # col = 1320
    m = np.matrix(np.zeros((col, col)))

    for i in range(col):

        # if i==1318:
        #     pass
        y, x, z = getPos(my, mx, mz,i)
        # 确定坐标
        # xcel = x * my * mz + y * mz + z + 1
        # 找到它的左右
        jihe = []
        yzuo = y - 1
        if yzuo > -1:
            zuo = x * my * mz + yzuo * mz + z
            jihe.append(zuo)
            # m[i, zuo] = 0.05
        yyou = y + 1
        if yyou < my:
            you = x * my * mz + yyou * mz + z
            jihe.append(you)
            # m[i, you] = 0.05
        for value in jihe:
            m[i,value]= 0.05 / len(jihe)
        # 找到它的前后
        jihe = []
        xqian = x - 1
        if xqian > -1:
            qian = xqian * my * mz + y * mz + z
            jihe.append(qian)
            # m[i, qian] = 0.05
        xhou = x + 1
        if xhou < mx:
            hou = xhou * my * mz + y * mz + z
            jihe.append(hou)
            # m[i, hou] = 0.05
        for value in jihe:
            m[i,value]= 0.05 / len(jihe)
        # 找到它的上下
        jihe = []
        zshang = z - 1
        if zshang > -1:
            shang = x * my * mz + y * mz + zshang
            jihe.append(shang)
            # m[i, shang] = 0.25
        zxia = z + 1
        if zxia < mz:
            xia = x * my * mz + y * mz + zxia
            jihe.append(xia)
            # m[i, xia] = 0.25
        for value in jihe:
            m[i,value]= 0.25 / len(jihe)
    return m
# print(m[0])
# a=getpinghua()
# pass


def getypinghua():
    my, mx, mz = 11, 12, 10
    col = 1320
    m = np.matrix(np.zeros((col, col)))

    for i in range(col):
        y, x, z = getPos(my, mx, mz, i)
        # 找到它的左右
        jihe = []
        yzuo = y - 1
        if yzuo > -1:
            zuo = x * my * mz + yzuo * mz + z
            jihe.append(zuo)
        yyou = y + 1
        if yyou < my:
            you = x * my * mz + yyou * mz + z
            jihe.append(you)
        for value in jihe:
            m[i, value] = 1 / len(jihe)
    return m

def getxpinghua():
    my, mx, mz = 11, 12, 10
    col = 1320
    m = np.matrix(np.zeros((col, col)))

    for i in range(col):
        y, x, z = getPos(my, mx, mz, i)
        # 找到它的前后
        jihe = []
        xqian = x - 1
        if xqian > -1:
            qian = xqian * my * mz + y * mz + z
            jihe.append(qian)
        xhou = x + 1
        if xhou < mx:
            hou = xhou * my * mz + y * mz + z
            jihe.append(hou)
        for value in jihe:
            m[i, value] = 1 / len(jihe)
    return m

def getzpinghua():
    my, mx, mz = 11, 12, 10
    col = 1320
    m = np.matrix(np.zeros((col, col)))

    for i in range(col):
        y, x, z = getPos(my, mx, mz, i)
        # 找到它的上下
        jihe = []
        zshang = z - 1
        if zshang > -1:
            shang = x * my * mz + y * mz + zshang
            jihe.append(shang)
        zxia = z + 1
        if zxia < mz:
            xia = x * my * mz + y * mz + zxia
            jihe.append(xia)
        for value in jihe:
            m[i, value] = 1 / len(jihe)
    return m
