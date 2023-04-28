from numpy import array

from Paper.getA import getA

my, mx, mz = 13, 14, 10

a=getA(13,14,10)
ans = [2.65] * a.return_cell_total()

# 空气
with open(r'..\..\data\output\air_cell','r') as r:
    while (r_line:=r.readline())!='':
        ans[int(r_line.strip().split()[0])-1]=0

ss=a.return_newtoold_col()

sss=list(a.return_oldtonew_col().keys())
col=a.return_col()

ylist = [7, 8, 9]
xlist = [5, 6, 7, 8]
zlist = [3, 4]

empty_hole = []

for y in ylist:
    for x in xlist:
        for z in zlist:
            empty_hole.append(x * my * mz + y * mz + z + 1)
# count=0
# for i in empty_hole:
#     if i not in sss:
#         print(i)
#         count+=1

# print('======')
# print(len(empty_hole))
# print(count)

index=0
with open(r"C:\Users\CHANG\Desktop\paper\calculate\compare\data\gongetidu", 'r') as r:
    while (line:=r.readline())!='':
        val=float(line.strip().split()[0])
        ans[ss[index] - 1] = val
        index+=1
with open(r"C:\Users\CHANG\Desktop\paper\calculate\compare\data\gongetidu_9_29", 'w') as w:
    for value in ans:
        w.write(f'{value}\n')