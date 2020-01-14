# python review

`一直使用Matlab，一个月没有使用python，在重新使用python好多基础函数已经很手生了，把之前《python数据分析》没看的第三章给看了一遍算是重新回顾一下python基础了`

*****

## 2019 12 23

*****

### jupyter:

* 使用两个问号可以实现查看函数的源代码

* 使用一个问号可以实现查看函数的说明

* 使用%run可以运行函数

* 使用CTRL plus C可以实现停止某一步的运行

*****

### python fundament：

* import的使用  
  * import function as ad
  
  * from function import f, g, PI

  * import function

* str操作
  * count function
  
  ```python
  # count函数可以实现统计代码中某个字符出现的次数
  c.count("\n")
  ````
  
  * replace function
  
  ```python
  # str 中的基础操作
  b = a.replace('string', 'longer string')
  ```

  * list function
  
  ```python
  # list函数能够将一个字符串分割成字符list
  list(str1)
  ```

  * raw转义
  
  ```python
  # 在python中想要使用“\"字符，需要进行转义
  # 有两种方法：一种是写两个斜杠，还有就是在字符串的前面写一个r表示这行字符不进行转义，r的意思是raw
  ```

  * str的格式化
  所谓格式化就是将字符串中添加一些格式化的参数，之后可以对这些格式化的参数进行赋值，填充str
  
  ```python
  template = '{0:.2f} {1:s} are worth US${2:d}'
  template.format(4.5556, 'Argentine', 1)
  ```

  格式化的含义：
    1. 其中第一个{0:.2f}表示这个是一个参数格式化为2位小数的浮点数

    2. {1:s}表示这是一个参数格式化为一个字符串

    3. {2:d}表示这是一个参数格式化为一个整数

  * 字节和Unicode
  `个人理解为字节类型的数据是和Unicode类型的数据是相互对应的，utf-8就是一个字节类型的数据`
  这里有通过两个函数来进行数据类型的转化：encode和decode分别表示编码和解码

* 日期和时间
  使用的是datatime模块，需要导入
  
  ```python
  from datatime import datatime, data, time
  ```

  注意datatime是datatime中的一个库是从datatime库中导入的
  
  ```python 
  dt = datatime(2019, 12, 23, 22, 03, 15)
  print(dt.day)  # day of dt
  print(dt.minute) # minute of dt
  print(dt.time())  # hours, minute, second of dt, output a datatime object
  print(dt.data())  # data fo dt, similarly datatime object
  ```
  
  注意day和minute是属性，而time，data是需要导入的datatime库中俄方法

  strftime和strptime函数，前者表示将datatime数据转化成str数据，后者表示将str数据转化成datatime数据
  格式为：
  
  ```python
  dt.strftime('%m/%d/%Y %H:%M')
  datatime.strptime('20091031', '%Y%m%d')
  ```
  
  注意datatime类型的数据是不可变的数据，这些操作都是产生一些新的对象。
  还有一些其他操作注意查看

*****

### tuple

1. tuple的拆包
`这是tuple很重要的性质很重要`
    * 所谓的拆包就是按位赋值

```python
    seq = [(2, 3, 4), (5, 6, 7), (8, 9, 10)]
    for a, b, c in seq:
        print('a={0}, b={1}, c={2}'.format(a, b, c))  
    # a = 2 a =5 a = 8
    # 更高级的拆包功能：
    a, b, *_ = values
    # *_means (3,:)values, in most cases, those values are discarded
```

### 内建序列函数

1. 函数enumerate的使用
  使用enumerate可以实现将一个list变成一个字典，是index和value的一一对应。

  ```python
  some_list = ['foo', 'bar', 'baz']
  mappint = {}
  for i, v in enumerate(some_list):
      mapping[v] = i

  >>>{'bar': 1, 'foo': 0, 'baz': 2}
  ```

  index是从0开始的

1. zip函数的使用
可以实现多个list的合并，合并之后还是一个list只是element变成tuple了
合并list的长度决定于最短的那个list，意味着可以使用不同长度的list

2. 从序列生成字典
使用zip函数，再使用一个遍历实现。

3. 注意字典的键必须是一个不可变的对象

### 列表、集合和字典的推导式

```python
[x.upper() for x in setrings if len(x) > 2]
# 一个列表生成器，表示将字母长度大于2的字母的字母变成大写
some_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
[x for tup in some_list for x in tup]
# 生成一个一维的list，迭代的顺序和我们写循环的顺序是一样的。
```

### 匿名函数Lambda

```python
lambda x: x*2
```

### 生成器

```python
def squares(n=10):
    for i in range(1, n+1):
        yield i**2
gen = squares()
# 这个表达式不能得到结果因为gen是一个生成器
for x in gen:
    print(x, end = ' ')
# 这样才能得到结果
```

### 文件与操作系统









