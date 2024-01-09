# Read trajectory file
import random
from functools import reduce

from llvmlite.ir import values

from main_computer import main_computer

# with open('Traj_1.txt', 'r') as fid:
#     fid.readline()  # skip the first line
#     i = 0
#     Data = {'pos': {'x': [], 'y': []}, 'curr_Pos': {'x': 0, 'y': 0}, 'Const': {'Obstacle': [30, 30]}}
#
#     for line in fid:
#         i += 1
#         fnum = list(map(float, line.split()))
#         Data['pos']['x'].append(fnum[0])
#         Data['pos']['y'].append(fnum[1])
#
# Data = {'pos': {'x': [values], 'y': [values]}, 'curr_Pos': {'x': 0, 'y': 0}, 'Const': {'Obstacle': [30, 30]}}
# main_computer(Data)
# print(Data['OutPos'])


# -----------------------
# list_test=[random.randint(1,20) for x in range(1,10)]
list_test=[1,2,3]
print(list_test)
num_sum=reduce(lambda x,y : x+y,list_test)
print(num_sum)

