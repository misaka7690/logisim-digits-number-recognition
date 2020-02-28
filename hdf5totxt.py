'''
@Author: misaka7690
@Description: 该文件读取HDF5文件,然后将其权值存储于txt文件中
'''
filename=r'.\hdf5_files\my_model_weights_1.h5'

import h5py  #导入工具包  
import numpy as np  

#HDF5的读取：  
f = h5py.File(filename,'r')   #打开h5文件  

paths=[]
for root_name, g in f.items():
    print(root_name)
    for _, weights_dirs in g.attrs.items():
        for i in weights_dirs:
            name = root_name + "/" + str(i, encoding="utf-8")
            print(name)
            paths.append(name)


kernel_1=f[paths[0]].value*1000
bias_1=f[paths[1]].value*1000
kernel_2=f[paths[2]].value*1000
bias_2=f[paths[3]].value*1000

np.savetxt(r'weights\kernel_1.txt', kernel_1,fmt='%d')
np.savetxt(r'weights\kernel_2.txt', kernel_2,fmt='%d')
np.savetxt(r'weights\bias_1.txt', bias_1,fmt='%d')
np.savetxt(r'weights\bias_2.txt', bias_2,fmt='%d')