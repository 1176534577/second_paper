from math import floor

from now_used.config import obs, obs_temp, regenerate_obs

# obs_temp=r'C:\Users\CHANG\Desktop\paper\second_paper\data\input\dataset2\obs_temp'
# obs=r'C:\Users\CHANG\Desktop\paper\second_paper\data\input\dataset2\obs'


def generate_obs():
    if not regenerate_obs:
        return
    with open(obs_temp, 'r') as d, open(obs, 'w') as dd:
        d_line = d.readline()
        cmout = floor(int(d_line) / 2200)
        # int(48000/23)=2086
        dd.write('1111\n')
        # flag = 0
        count=0
        while (d_line := d.readline()) != '':
            dd.write(d_line)
            count+=1
            for _ in range(cmout - 1):
                d.readline()
        dd.seek(0,0)
        dd.write(f'{count}')

    # print('第一行'+d_line)
    # print('第二行'+d.readline())
    # print('第三行'+d.readline())
    # if flag == 0:
    #     dd.write(d_line)
    #     flag = 1
    # elif flag == 1:
    #     flag = 2
    # else:
    #     flag = 0

if __name__ == '__main__':
    generate_obs()