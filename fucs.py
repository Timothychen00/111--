import random
import os.path as path
from sys import argv


def read_settings():
    i=0;
    job_list=[]
    needed_number=[]
    exception=[]
    seat_number=list(range(1,36))
    dirname=path.dirname(path.realpath(argv[0]))
    file=path.join(dirname,'config.txt')
    with open(file,mode="r",encoding='utf-8') as f1:
        for line in f1.readlines():
            if line!="\n":#刪除空白行
                line_split=line.split(":")
                if not line.startswith('#'):
                    job_list.append(line_split[0])
                    needed_number.append(int(line_split[-1].split('\n')[0]))
                    print(line,end='')
                    i+=1
                else:
                    if line_split[0]=="#排除":
                        for each in line_split[1].split(' '):
                            exception.append(int(each))
                    elif line_split[0]=='#總人數':
                        seat_number=list(range(1,int(line_split[1])))
        for each in exception:
            seat_number.remove(each)
        random.shuffle(seat_number)
    return job_list,needed_number,seat_number,exception