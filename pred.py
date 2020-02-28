'''
@Author: misaka7690
@Description: 该文件读取神经网络权值,然后读取num.txt的0-1表示的8*8数字,然后利用矩阵运算进行预测
'''
import numpy as np
from numpy.linalg import *

# 由于logisim设计的CPU不支持浮点运算,故将浮点数全部乘以1000然后转为int
kernel_1=np.loadtxt(r'.\weights\kernel_1.txt')
kernel_2=np.loadtxt(r'.\weights\kernel_2.txt')
bias_1=np.loadtxt(r'.\weights\bias_1.txt')
bias_2=np.loadtxt(r'.\weights\bias_2.txt')

kernel_1=kernel_1.astype(np.int)
kernel_2=kernel_2.astype(np.int)
bias_1=bias_1.astype(np.int)
bias_2=bias_2.astype(np.int)

num=np.loadtxt(r'.\num.txt')
num=num*16
num=num.ravel()

output_1=num.dot(kernel_1)+bias_1
# relu函数
def relu(x):
    return (abs(x)+x)/2
output_1 =relu(output_1)

output_2=output_1.dot(kernel_2)+bias_2
pred=output_2.argmax()
print(pred)