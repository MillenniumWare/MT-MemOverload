import os
import multiprocessing
from multiprocessing import Process


def listfill():
    filllist = []
    for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
        filllist.append("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")



cpucount = os.cpu_count()
cpucount = int(cpucount)

for i in range(cpucount):
    if __name__ == '__main__':
        p = Process(target=listfill)
        p.start()
        p.join()
