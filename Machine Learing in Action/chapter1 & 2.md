# Chapter1&2

## Chapter1

* 用于执行分类、回归、聚类和密度估计的机器学习算法

*****
**监督学习**

* [ ] K近邻算法

适用于分类算法，特别是数值型数据分类，数据要求是标称的。

线性回归

* [ ] 朴素贝叶斯算法

局部加权线性回归

* [ ] SVM 支持向量机

Ridge回归 **？？？**

* [ ] 决策树

*****

**非监督学习**

* [ ] K-均值

最大期望算法

* [ ] DBSCAN **？？？**

Parzen窗设计 **？？？**

*****

* 对于数据需要考虑的问题

1. 特征值是离散值还是连续值

2. 特征值中是否存在缺失的值

3. 何种原因导致的缺失

4. 数据中是否存在异常值

5. 某个特征值的出现频率如何（是否是均衡出现的）

这些方法可以缩小我们在算法选择的范围

* 机器学习程序的应用步骤

1. 收集数据

2. 准备数据的格式
处理一些数据的格式使得可以输入到算法中去

3. 分析输入的数据
比如查看是否存在空值和异常值，通过绘图来进行查看是一个很好的方式。但是我们的数据往往是多于三维的，这时候需要对数据进行一些压缩，方便数据的展示

4. 训练算法

5. 测试算法/评估算法

* python运行速度的问题怎么解决：

我们应当首先使用python实现系统，实现目的后可以逐步使用C++Boost来替代算法中的核心代码，能否实现问题是最重要的。实现之后再考虑怎么进行优化

## chapter2

* 什么是k近邻算法

将数据中的特征和样本中的所有数据进行一次比较，之后选择最接近的k个数据，之后对着k个数据进行一下分析其中出现频率最高的类就是期望值。

* k近邻的优点和缺点
  * 优点：精度高、对异常值不敏感、没有数据的输入假定
  
  * 缺点：计算的复杂度高、空间复杂度高

  * 适用的数据范围：数值型和标称型数据（非畸形数据？）

* 使用python导入数据

使用python实现kNN算法：
首先的思路：

1. 计算对象到训练集中每个点的距离(将目标向量按照列进行拓展，之后和训练集中的数据做差，之后求欧式距离)

2. 对计算结果进行一次排序(这里不要对距离进行一个简单的排序，除非带着labels一起进行排序，这里使用argsort函数进行排序得到从大到小的索引值，这样就方便对label进行处理了，之后创建一个字典，字典的键是对应的label，值是出现的次数这里使用字典的get方法)

3. 选择距离最近的k个点(使用sorted对字典中的键进行排序key设定为operate.itemgetter(1),就能通过值实现键的排序了)

4. 将这k个点中出现频率最高的一个类型作为最终的预测结果(
    就直接使用排序list中的第一个值就行了。
)

python实现：
需要传入的参数：
目标向量inX、训练集dataSet、标签向量labels、参数k

```python
def classify0(inX, dataSet, labels, k):
    dataSetsize = dataSet.shape[0]  
    # shape[0]表示的是一共有多少个行
    diffMat = tile(inX, (dataSetsize,1)) - dataSet
    # 使用tile将目标向量进行堆叠，之后再做差
    sqDiffMat = diffMat ** 2  
    # 这里是是每个元素平方不是转置相乘
    distances = sqDiffMat.sum(axis=1)
    # 将两列的值进行合并的到欧式距离
    sortedDistIndicies = distances.argsort()
    # 这个思路很重要，使用argsort()函数得到index的排序而不是直接使用排序。其实感觉使用zip合并之后在直接排序也可以，但是创造字典的时候就比较麻烦了，使用index排序是很好的思路。
    classCount ={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) +1 # 参数0有什么
        # get用来查找字典中的指定key的value，只有一个参数的时候不会报错只是没有返回值，这里的第二个参数表示
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1),reverse=True)
    # 字典的items属性将字典的key和value变成一个元组。key传递的值表示按照元组的第二个值进行排序，reverse表示降序排列，默认是False
    return sortedClassCount[0][0]
```
