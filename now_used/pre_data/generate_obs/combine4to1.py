# id, y0, x0, z0, theta0, phi0, d

from now_used.config import row_data, regenerate_obs, obs_temp

# num = 2
# row_data = r'C:\Users\CHANG\Desktop\paper\second_paper\data\rawData\dataset2'
# obs_temp=r'C:\Users\CHANG\Desktop\paper\second_paper\data\input\dataset2\obs_temp'

def combine4to1():
    n = 12000
    count=0
    with open(obs_temp, 'w') as w:
        w.write('11111\n')

        # 12000个
        with open(row_data + r'\LRC_thetaphi-D1.dat', 'r') as r1:
            r1.readline()
            for _ in range(n):
                a = r1.readline().strip().split()[0:3]
                if float(a[2]) < 1:
                    continue
                w.write(f'1 7.5 -0.1 0.1  {a[1]} {a[0]} {a[2]}\n')
                count+=1

        # 12000个
        with open(row_data + r'\LRC_thetaphi-D2.dat', 'r') as r1:
            r1.readline()
            for _ in range(n):
                a = r1.readline().strip().split()[0:3]
                if float(a[2]) < 1:
                    continue
                w.write(f'2 15.1 10 0.1 {a[1]} {a[0]} {a[2]}\n')
                count+=1

        # 12000个
        with open(row_data + r'\LRC_thetaphi-D3.dat', 'r') as r1:
            r1.readline()
            for _ in range(n):
                a = r1.readline().strip().split()[0:3]
                if float(a[2]) < 1:
                    continue
                w.write(f'3 7.5 20.1 0.1 {a[1]} {a[0]} {a[2]}\n')
                count+=1

        # 12000个
        with open(row_data + r'\LRC_thetaphi-D4.dat', 'r') as r1:
            r1.readline()
            for _ in range(n):
                a = r1.readline().strip().split()[0:3]
                if float(a[2]) < 1:
                    continue
                w.write(f'4 -0.1 10 0.1 {a[1]} {a[0]} {a[2]}\n')
                count+=1
        w.seek(0, 0)
        w.write(f'{count}')

if __name__ == '__main__':
    combine4to1()