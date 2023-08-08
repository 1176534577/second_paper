
# 空气
# air_cell= set()
# with open(r'..\data\output\air_cell','r') as r:
#     while (line:=r.readline())!='':
#         air_cell.append(int(line))
# my, mx, mz = 17,22,10
from now_used.pre_data.cellbnd import cellbnd
from now_used.pre_data.getmesh import getmesh


class TheoreticalValue:
    def __init__(self):
        self.empty_hole=[]
        x_set=set()
        y_set=set()
        z_set=set()
        mesh=getmesh(r'C:\Users\CHANG\Desktop\paper\calculate\data\test\seed_opt.msh').getmesh()
        cell=cellbnd(*mesh[:-1])
        self.mx,self.my,self.mz=mesh[:3]
        with open(r'C:\Users\CHANG\Desktop\paper\calculate\data\test\center_right_5box.obj','r') as r:
            file_data=r.readlines()[2:26]
        for data in file_data:
            data_list=data.split()
            discrete_x,discrete_y,discrete_z=cell.getcellbnd(float(data_list[2]), float(data_list[1]), mesh[-1]-float(data_list[3]))
            x_set.add(discrete_x+1)
            y_set.add(discrete_y+1)
            z_set.add(discrete_z+1)
        xlist=list(range(min(x_set),max(x_set)))
        ylist=list(range(min(y_set),max(y_set)))
        zlist=list(range(min(z_set),max(z_set)))

        for x in xlist:
            for y in ylist:
                for z in zlist:
                    self.empty_hole.append(x * self.my * self.mz + y * self.mz + z)

    def storage(self):
        with open(r'..\data\output\res_theory10_18', 'w') as w:
            n = self.mx * self.my * self.mz
            for i in range(n):
                if i in self.empty_hole:
                    # 空洞为1
                    w.write('1\n')
                else:
                    # 为2.65的四棱柱
                    w.write('2.65\n')

th=TheoreticalValue()
th.storage()

# 空洞
# 三个方向的取值范围
# xlist=[9,10,11,12]
# ylist=[10,11,12]
# zlist=[3,4]

# empty_hole=[]
#
# for y in ylist:
#     for x in xlist:
#         for z in zlist:
#             empty_hole.append(x * my * mz + y * mz + z + 1)




# for y in ylist:
#     for x in xlist:
#         for z in zlist:
#             empty_hole.append(x * my * mz + y * mz + z + 1)


