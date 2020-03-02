'''
@Author: misaka7690
@Description: 该文件用来将hex指令直接hack进circ文件中的ROM中
'''

filename='begin&gameover.hex'

hex=open(filename,'r').read().split('\n')

out_filename='hack.txt'

ans=[]

i=0
while i<len(hex):
    t=hex[i:i+8]
    t=' '.join(t)
    ans.append(t)
    i+=8

with open(out_filename,'w') as f:
    f.write('\n'.join(ans))