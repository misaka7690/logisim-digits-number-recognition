'''
@Author: misaka7690
@Description: 使用神经网络对8*8的图像进行训练,并把权值导出再HDF5文件中
'''
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop

# 导入数据
data=load_digits()
images=data.images
targets=data.target
# images[images>images.mean()/10]=1
# 以灰度图的形式,显示第9张image
plt.imshow(images[9],cmap='gray')

# 划分训练集和测试集
images=images.reshape((len(images),-1))
data_num=len(images)
train_num=int(data_num*7/10)
x_train=images[:train_num]
x_test=images[train_num:]
y_train=targets[:train_num]
y_test=targets[train_num:]

# 将图片中的数字(0-9)转为one-hot编码
y_train = keras.utils.to_categorical(y_train,10)
y_test = keras.utils.to_categorical(y_test,10)

# 使用keras,创建一个神经网络模型,输入层为64个节点,中间层10个节点,输出层10个节点
model = Sequential()
model.add(Dense(10,activation='relu',input_dim=8*8,kernel_constraint=keras.constraints.MinMaxNorm(min_value=1, max_value=10, rate=1.0, axis=0)))
model.add(Dense(10,activation='softmax',kernel_constraint=keras.constraints.MinMaxNorm(min_value=1, max_value=10, rate=1.0, axis=0)))

# 输出网络结构
model.summary()

# 输出为
# Model: "sequential_3"
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #   
# =================================================================
# dense_5 (Dense)              (None, 10)                650       
# _________________________________________________________________
# dense_6 (Dense)              (None, 10)                110       
# =================================================================
# Total params: 760
# Trainable params: 760
# Non-trainable params: 0


model.compile(loss='categorical_crossentropy',
             optimizer=RMSprop(),
             metrics=['accuracy'])

# 训练模型,其中train比validate的数据集比例为7:3
model.fit(x_train,y_train,batch_size=64,epochs=64,verbose=1,
         validation_split=0.3,shuffle=True)

score = model.evaluate(x_test, y_test, batch_size=128)
print(score)
# 输出为[0.5744654103561684, 0.8999999995584841],第一个为loss,第二个为acc

# 保存权值在文件中
model.save_weights('my_model_weights_1.h5')