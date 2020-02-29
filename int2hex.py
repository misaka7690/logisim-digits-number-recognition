'''
@Author: misaka7690
@Description: 该文件用来将神经网络所有权值(int类型)存储为连续的txt中以便加载到Logisim的ROM中
'''
import numpy as np

kernel_1=np.loadtxt(r'.\weights\kernel_1.txt')
kernel_2=np.loadtxt(r'.\weights\kernel_2.txt')
bias_1=np.loadtxt(r'.\weights\bias_1.txt')
bias_2=np.loadtxt(r'.\weights\bias_2.txt')

kernel_1=kernel_1.astype(np.int)
kernel_2=kernel_2.astype(np.int)
bias_1=bias_1.astype(np.int)
bias_2=bias_2.astype(np.int)

rom=[]

M=2**32

def f1(x):
    x+=M
    x=x%M
    x=hex(x)[2:]
    x='0'*(8-len(x))+x
    return x 

#kernel_1存在0~639号地址 共640个数字

a,b=kernel_1.shape
for i in range(a):
    for j in range(b):
        x=kernel_1[i][j]
        rom.append(f1(x))

#bias_1存在640~649号地址 共10个数字
for i in range(len(bias_1)):
    x=bias_1[i]
    rom.append(f1(x))
#kernel_2存在650~749号地址 共100个数字
a,b=kernel_2.shape
for i in range(a):
    for j in range(b):
        x=kernel_2[i][j]
        rom.append(f1(x))
#bias_2存在750~759号地址 共10个数字
for i in range(len(bias_2)):
    x=bias_2[i]
    rom.append(f1(x))

rom_path=r'.\weights\rom.txt'
with open(rom_path, 'w') as f:
    f.write('\n'.join(rom))