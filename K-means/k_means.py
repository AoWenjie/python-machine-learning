from numpy import *
import time
import matplotlib.pyplot as plt

DataSet = []

#计算欧式距离euclidean metric
def Count_Euclidean_Distance(vector1, vector2):
    return sqrt(sum(power(vector1 - vector2, 2)))


#初始化质心
#DataSet长下面这样
'''
DataSet = {[[1,2,3,4,5,...];
            [6,7,8,9,10,...];
            ...
            [.............]]
           }
'''
def Initial_Centriods(DataSet,K):
    _row,_col = DataSet.shape #返回数据集的行和列
    _centriods = zeros((K,_col)) #初始化聚类中心矩阵
    for i in range(K):
        index = int(random.uniform(0,_row)) #随机生成聚类中心点的索引，即在哪行
        #⬆能保证下一次生成的随机数与本次不同吗？暂时未知
        _centriods[i,:] = DataSet[index,:]
    return _centriods

def K_Means(DataSet,K):
    _row = DataSet.shape[0]

    #cluster_info是一个与DataSet行数相同，列为2的矩阵
    #第一列保存了它属于哪个cluster的信息
    #第二列保存了
    cluster_info = mat(zeros((_row,2)))
    is_cluster_changed = True
    _centeriods = Initial_Centriods(DataSet,K)

    while is_cluster_changed:
        is_cluster_changed = False
        for i in range(_row):
            min_dist = 1000000.0
            min_index = 0

            #找出最邻近点
            for j in range(K):
                _distance = Count_Euclidean_Distance(_centeriods[j,:],DataSet[i,:])
                if _distance < min_dist:
                    min_dist = _distance
                    min_index = j

            #将聚类信息保存到cluster_info
            if cluster_info[i,0] != min_index:
                is_cluster_changed = True
                cluster_info[i,:] = min_index, min_dist
        
        #更新聚类中心
        for j in range(K):
            #下面这个操作有点绕
            #注意cluster_info是mat形式的数据，这样可以方便的进行行列操作，线性变换
            #cluster_info[:,0].A,.A是将mat转为array
            #cluster_info[:,0].A == j是用来找出所有的第0列为j的array
            #⬆会返回(True,False,...)
            #nonzero函数是得出不为0的元素的索引，对二维数组，会分别返回行列信息
            #nonzero(a)[0]是行的信息，nonzero(a)[1]是列的信息
            point_cluster = DataSet[nonzero(cluster_info[:,0].A == j)[0]]
            _centeriods[j,:] = mean(point_cluster,axis = 0)
    return _centeriods,cluster_info

def load_dataSet():
    f = open('k_means_dataSet.txt')
    for line in f.readlines():
        lineArr = line.strip().split('\t')
        DataSet.append([float(lineArr[0]),float(lineArr[1])])

print("开始加载数据")
load_dataSet()
DataSet = mat(DataSet)
plt.scatter(DataSet[:,0].A,DataSet[:,1].A,s = 20, c = 'red')
print("开始进行计算")
_centeriods,cluster_info = K_Means(DataSet,4)
print(_centeriods)
plt.scatter(_centeriods[:,0],_centeriods[:,1],s = 60,c = 'black')
plt.show()