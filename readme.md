# 8x8像素数字识别

该项目为`利用logisim实现的24+4条指令CPU来实现神经网络识别8x8像素数字识别`的上游任务,主要实现

- 利用keras的神经网络对sklearn自带8x8手写数字数据集进行训练
- 将训练权值保存为HDF5文件并转为整形存储在txt文本中以便将来导入logism中的存储器中
- 使用python简单的模拟logism对预测过程进行测试

## 说明

- `train.py`: 训练神经网络
- `hdf5totxt`: 将HDF5格式的神经网络权值转化为int类型的神经网络权值
- `np2num.py`: 将np.array格式的数据存储为8x8像素数字存储在num.txt中
- `int2hex.py`: 将所有权值数据转为连续存储的三十二位十六进制数据以便加载在logisim中的ROM中
- `pred.py`: 模拟logism对num.txt中的8x8像素数字进行识别
- `hex_hack_in_logisim.py`: 该文件用来将hex指令直接hack进circ文件中的ROM中
- `hdf_files`: 存储神经网络权值(HDF5格式)
- `weights`: 存储转化为int类型的神经网络权值
- `num.txt`: 0-1表示的8x8像素数字

## 结果说明

1. 训练集中`acc`可达仅97%,测试集为89%
2. 利用python模拟logism对num.txt中的8x8像素数字进行识别,数据使用sklearn的数据,预测结果基本与实际结果一致
3. sklearn的8x8数字质量并不好,实际上自己制作的8x8的0-1数字准确率估计没有80%

## TODO 

- 对sklearn的数据集做进一步的处理,使之更接近人工制作的8x8的0-1像素数字
- 自己生成数据集?
