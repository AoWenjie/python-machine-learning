#专用于生成一些数据集
#作者：敖文杰
#日期：2019/01/09
import random

f = open('k_means_dataSet.txt','w+')

for i in range(100):
    f.write(str(round(random.uniform(0,20),2)) + '\t' +str(round(random.uniform(0,20))) + '\n')
    f.write(str(round(random.uniform(20,40),2)) + '\t' +str(round(random.uniform(20,40))) + '\n')

#测试git是否能用
