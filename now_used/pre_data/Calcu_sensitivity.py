# 如果对数据要求精确的话，使用Decimal
# from decimal import Decimal
from math import pi
from math import sin, cos

from prettytable.prettytable import PrettyTable
from tqdm import trange

from now_used.pre_data.cellbnd import cellbnd
from now_used.pre_data.getmesh import getmesh


class Calcsensitivity:
    def __init__(self, obsf, meshf):
        self.obsf = obsf
        self.meshf = meshf

    def calcsensitivity(self, ijf, Ray_way_j_file):
        """
        计算射线穿过格子的长度

        :param obsf:obs文件的路径
        :param meshf: mesh文件的路径，当meshf为None时，默认会寻找在obsf所在文件夹下的mesh文件
        :param ijf: ij文件的路径，当ijf为None时，默认会存放在obsf所在的文件夹下的ij文件中，i和j均是从1开始的
        :param ray_cell_mapf: 正常射线穿过的格子编号
        :param isprint: 是否打印排除掉的射线的信息，默认不打印
        :return:
        """
        mx, my, mz, xnode, ynode, znode, elev0 = getmesh(meshf=self.meshf).getmesh()
        cell_entity = cellbnd(mx, my, mz, xnode, ynode, znode)

        dirr = [0] * 2
        oldid = 0
        oldi = 1
        oldabnormal = normal = habnormal = xabnormal = yabnormal = 0
        rayexclude, hlist, xlist, ylist, sen_nor = [], [], [], [], []
        id_set = set()

        with open(self.obsf, 'r') as f, open(ijf, 'w') as ff, open(Ray_way_j_file, 'w') as fff:
            ndat = int(f.readline())

            ff.write(f'{ndat} {mx * my * mz}\n')

            for i in trange(ndat):
                i += 1
                fflist = f.readline().strip().split()
                id, y0, x0, z0, theta0, phi0, d = int(fflist[0]) - 1, float(fflist[1]), float(
                    fflist[2]), elev0 - float(fflist[3]), pi / 2 - float(fflist[4]), float(fflist[5]), float(
                    fflist[6])

                # 记录除最后一个探测器以外的其余探测器的异常射线的信息(最后一个探测器的异常射线信息在循环结束后记录)
                if id != oldid:
                    oldid = id
                    newabnormal = habnormal + xabnormal + yabnormal
                    rayexclude.append([newabnormal - oldabnormal, i - oldi])
                    oldi = i
                    oldabnormal = newabnormal
                # 根据探测器id来增加sen_nor的长度
                if id not in id_set:
                    id_set.add(id)
                    sen_nor.append([])

                ind, sensrow = [], []  # ind存放射线穿过哪些格子，即j，sensrow存放射线穿过格子时，在格子内的路径长度

                # ux是x轴的，uy是y轴的，uz是z轴的，单位长度(可以看作是1)投影到各个轴上的长度，只需要乘以实际长度就可以得到实际的投影长度
                ux = abs(sin(phi0) * cos(theta0))
                uy = abs(cos(phi0) * cos(theta0))
                uz = sin(theta0)

                # dirr[0]是x轴的，dirr[1]是y轴的
                dirr[0] = -1 if sin(phi0) < 0 else 1
                dirr[1] = -1 if cos(phi0) < 0 else 1

                # 考虑射线近乎(贴近)水平时的情况，此类射线不参与计算
                if abs(uz) < 1e-5:
                    habnormal += 1
                    # hlist.append([i, d, derr])
                    continue

                # 得到探测器的位置离散坐标
                xc, yc, zc = cell_entity.getcellbnd(x0, y0, z0)
                # 是否停止(结束)计算，done为False时继续计算，为True时停止(结束)计算
                isnext = done = False
                # 射线在每个格子停留时，必定是停留在格子的某个面上
                # 如果射线与z轴的夹角很小
                if abs(uz - 1) < 1e-5:
                    # 如果探测器几乎紧挨着格子壁，x0和y0就减小一点
                    if abs(x0 - xnode[xc + 1] < 1e-5): x0 -= (xnode[xc + 1] - xnode[xc]) / 10
                    if abs(y0 - ynode[yc + 1] < 1e-5): y0 -= (ynode[yc + 1] - ynode[yc]) / 10

                    while not done:
                        zbound = znode[zc]
                        dr = z0 - zbound
                        z1 = z0 - dr * uz
                        xcel = xc * my * mz + yc * mz + zc + 1

                        ind.append(xcel)
                        sensrow.append(dr)

                        zc -= 1
                        z0 = z1

                        if zc == -1:
                            done = True
                # 探测器与z轴的夹角既不大也不小
                else:
                    while not done:
                        # 找到射线此时所在的格子的z方向的上边界值
                        zbound = znode[zc]
                        # 求射线距离上边界值的距离
                        z1 = z0 - zbound
                        # dz是斜边，z1是对边，dx,dy,dz的方向都是相同的，只是长短不一
                        # 射线要到达z格子上边界所要走的路程
                        dz = z1 / uz
                        # 根据射线与y轴的角度给dx赋值
                        # 与y轴的角度不是很小
                        if abs(ux) > 1e-5:  # match考虑到python版本的问题，改用if
                            if dirr[0] == 1:
                                x1 = xnode[xc + 1] - x0
                            else:
                                x1 = x0 - xnode[xc]  # dirr[0]==-1说明与y轴的夹角在180°和360°之间，在x轴的负半轴
                            # 射线要到达x格子边界的所要走的路程
                            dx = x1 / ux
                        # 如果射线与y轴的夹角很小，就说明射线接下来必定不会到达x格子边界，所以就把dx设的很大，选取dr的时候肯定不会选择dx，同时可以避免计算dx
                        else:
                            dx = 1e32
                        # 根据射线与y轴的角度给dy赋值
                        # 与y轴的角度不是很大
                        if abs(uy) > 1e-5:
                            if dirr[1] == 1:
                                y1 = ynode[yc + 1] - y0
                            else:
                                y1 = y0 - ynode[yc]
                            # 射线要到达y格子边界的所要走的路程
                            dy = y1 / uy
                        # 如果射线与y轴的夹角很大(也即射线与x轴的夹角很小)，就说明射线接下来必定不会到达y格子边界，所以就把dy设的很大，选取dr的时候肯定不会选择dy，同时可以避免计算dy
                        else:
                            dy = 1e32

                        # dx,dy,dz哪个值赋值给dr，射线接下来就穿过哪个格子，e.g. dx最小，那么射线接下来就到达x格子边界
                        dr = min(dx, dy, dz)
                        # 计算接下来射线走dr路程到达的x1,y1位置,z1是射线走dr路程到达的位置到z方向最大值的差
                        x1 = (x0 + dirr[0] * dr * ux)
                        y1 = (y0 + dirr[1] * dr * uy)
                        z1 = (z0 - dr * uz)
                        # 计算射线此时所在格子的j值，因为xc,yc,zc是从0开始的，所以j也是从0开始的，但是需要j从1开始，所以要+1
                        # 除去射线的第一个点，其余的点都在格子的表面上，每次到达的下一个点所在的面都是距离当前点最近的面
                        # 当一个点在一个面上时，它归属于射线沿着穿出的方向所处的格子
                        xcel = xc * my * mz + yc * mz + zc + 1

                        # 存放射线穿过的格子ind以及在格子内的长度sensrow,大小都是numz,即射线穿过的格子数量
                        ind.append(xcel)
                        sensrow.append(dr)

                        # dx最小，说明射线到达了x格子边界，xc改变(根据射线的角度来决定加减)
                        # dy最小，说明射线到达了y格子边界，yc改变(根据射线的角度来决定加减)
                        # dz最小，说明射线到达了z格子边界，zc改变(只能减，即一直往上方靠)
                        # 可能当前的点
                        if dx < dy and dx < dz:
                            xc += dirr[0]
                        elif dy < dx and dy < dz:
                            yc += dirr[1]
                        elif dz < dx and dz < dy:
                            zc -= 1
                        else:
                            if dx < dy:
                                xc += dirr[0]
                                zc -= 1
                            else:
                                yc += dirr[1]
                                zc -= 1

                        x0, y0, z0 = x1, y1, z1

                        if -1 < xc < mx and -1 < yc < my:
                            if zc == -1: done = True
                        elif xc == -1 or xc == mx:
                            xabnormal += 0
                            done = True
                        else:
                            yabnormal += 0
                            done = True


                sen_nor[id].append(i)
                fff.write(f'{d}\n')
                for jg, row in zip(ind, sensrow):
                    ff.write(f'{i} {jg} {row}\n')
                normal += 1
            abnormal = habnormal + xabnormal + yabnormal
            rayexclude.append([abnormal - oldabnormal, i - oldi + 1])
            table = PrettyTable(["探测器编号", "排除数", "总数", "排除百分比"])
            for i, ray in enumerate(rayexclude):
                table.add_row([i + 1, ray[0], ray[1], '{:.2%}'.format(ray[0] / ray[1])])
            table.add_row(['总计', abnormal, ndat, '{:.2%}'.format(abnormal / ndat)])
            print(table)

