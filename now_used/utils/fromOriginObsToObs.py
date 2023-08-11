from now_used.config import root_path_input


def calc():
    """
    计算dataset1的obs
    :return:
    """
    with open(root_path_input+r'\dataset1\obs_origin','r') as r,open(root_path_input+r'\dataset1\obs','w') as w:
        count=int(r.readline())
        w.write(str(count))
        for _ in range(count):
            myArray=r.readline().strip().split()
            w.write(myArray[0]+' '+myArray[1]+' '+myArray[2]+' '+myArray[3]+' '+myArray[4]+' '+myArray[5]+' '+myArray[7])

if __name__ == '__main__':
    calc()