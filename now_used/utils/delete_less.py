from Paper.getA import getA,count_less_and_equal_num

a=getA(13,14,10)
ss=a.return_oldtonew_row()
li=count_less_and_equal_num(a.return_A(), 10)


with open(r'..\..\data\output\new_ijg','r') as r,open(r'..\..\data\output\newww_ijg','w') as w:
    w.write(r.readline())
    while (line:=r.readline())!='':
        if ss[int(line.strip().split()[0])] not in li:
            w.write(line)