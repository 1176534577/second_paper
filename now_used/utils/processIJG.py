air_cell=[]
with open(r'../../data/output/old/air_cell', 'r') as r:
    while (line:=r.readline())!='':
        air_cell.append(int(line))

with open(r'..\..\data\output\ijg','r') as r,open(r'..\..\data\output\new_ijg','w') as w:
    w.write(r.readline())
    while (r_line:=r.readline())!='':
        if int(r_line.strip().split()[1]) not in air_cell:
            w.write(r_line)
