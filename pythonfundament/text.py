# import datetime

# class Polynomial:
#     def __init__(self, coeffsicients):
#         self.coeffs = coeffsicients
    
#     def coeff(self, i):
#         return self.coeffs[-1*i-1]
    
#     def add(self, other):
#         if len(self.coeffs)> len(other.coeffs):
#             project = self.coeffs.copy()
#             judge = 0
#         else:
#             project = other.coeffs.copy()
#             judge = 1
        
#         if judge ==0:
#             for m in range(len(other.coeffs)):
#                 project[-1*m-1] += other.coeffs[-1*m-1]
#         else:
#             for m in range(len(self.coeffs)):
#                 project[-1*m-1] += self.coeffs[-1*m-1]  
        
#         return project
#         # 这里要返回什么类型的数值呢？？？

#     def mul(self, other):
#         list2 = []
#         for a in range(len(other.coeffs)):
#             list1 = [i*other.coeffs[a-1] for i in self.coeffs]
#             for b in range(a):
#                 list1.append(0)
#             list2 = Polynomial(list2).add(Polynomial(list1))
#         return list2

#     def __str__(self):
#         return str(self.coeffs)
    
#     def val(self, v):
#         num = len(self.coeffs)
#         sum = 0 
#         for n in range(num):
#             sum += v**n*self.coeffs[(num-n)-1]
#         return sum
    
#     def val1(self, v):
#         num = len(self.coeffs)
#         sum = 0
#         tem = 0
#         for n in range(num):
#             sum *= v
#             sum = sum+ self.coeffs[n]
#         return sum

#     def roots(self):
#         if len(self.coeffs)==2:
#             return self.coeffs[1]/(-1*self.coeffs[0])
#         elif len(self.coeffs)==3:
#             root1 = -1*self.coeffs[1]/2/self.coeffs[0]
#             root = self.coeffs[1]**2 - 4* self.coeffs[0]*self.coeffs[2]
#             if root >= 0:
#                 root2 = (root)**0.5/ 2/ self.coeffs[0]
#             else:
#                 root2 = complex(root, 0)**0.5/2/self.coeffs[0]
                
#             return root1+root2, root1-root2

#         else:
#             return ("can't handle this problem")
#     def __repr__(self):
#         # 可以修改交互式输入界面的实例类型的输出结果
#         # 和__str__方法相对应，str方法不能修改交互式界面的输出只能修改print的输出
#         return str(self)
#     def __add__(self, other):
#         return self.add(other)
#     def __mul__(self, other):
#         return self.mul(other)
#     def __call__(self, x):
#         # 可以将实例作为一个函数在进行一次输入
#         # 这里的x就相当与实例接受的参数
#         return self.val(x)

# object1 = Polynomial([1,2,3,4,5,6,7,8,9,10,11,12,12,12,13,145,125,1251,1224512,1234,13124,123,523,435,23534,457456,2323,645534,324523,6434,34,4,6,345,345,34534,346])
# object2 = Polynomial([1,-2, 3])
# starttime = datetime.datetime.now()
# print(object1.val(2))
# starttime1 = datetime.datetime.now()
# print("运行时间是{}".format(starttime1-starttime))
# print(object1.val1(2))
# endtime = datetime.datetime.now()
# print("新方法的运行时间是{}".format(endtime-starttime1))



# def compare(x, y):
#     if x>y:
#         return 1
#     elif x<=y:
#         return 0

# print(compare(2,1))

# def arithmeticIf(v, a, b, c):
#     if v>0:
#         return a
#     elif v==0:
#         return b
#     else:
#         return c

# print(arithmeticIf(1,compare,abs,len))

# def clip(lo, x, hi):
#     return min(max(lo,x),hi)

# print(clip(1,0,3))

# def multIA(m, n):
#     sum = 0
#     while n>0:
#         sum += m
#         n-=1
#     return sum
# print(multIA(5,10))

# def multIAgen(m, n):
#     sum = multIA(m,abs(n))
#     if n<0:
#         return -1*sum
#     else:
#         return sum
# print(multIAgen(-5, -10))

# def mod(m, n):
#     while m>=n:
#         m -= n
#     return m

# print(mod(10,2))

# def div(m, n):
#     i = 0
#     m -= n
#     while m>=0:
#         i+=1
#         m -= n
#     return i

# print(div(13, 4))

# def prime(n):
#     if n == 1:
#         return False
#     for i in range(2, round(n/2)):
#         if n%i==0:
#             return False
#     return True
# print(prime(13337))

# def p2(x):
#     '''返回指数还是返回2^n的值？题目说的是小于'''
#     i =0 
#     while 2**(i+1) < x:
#         i +=1
#     return i

# print(p2(3))

# import math
# def perfectSquare(n):
#     # i = math.sqrt(n)
#     # if i % 1== 0:
#     #     return True
#     # else:
#     #     return False
#     if n == 1:
#         return True
#     else:
#         for i in range(2, int(n/2)+1):
#             if n == i**2:
#                 return True
#         return False
# print(perfectSquare(15))

# def quadraticRoots(a, b, c):
#     if a == 0:
#         return -1* c/b
#     else:
#         root1 = -b/2/a
#         root = b**2 - 4*a*c
#         if root >= 0:
#             root2 = float(root)**0.5/2/a
#         else:
#             root2 = complex(float(root))**0.5/2/a
#         return [root1 + root2, root1-root2]

# print(quadraticRoots(1, 1.9, -3))

# import math
# def pointDist(p1, p2):
#     return math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2)

# def multIA(m, n):
#     sum = 0
#     for i in range(n):
#         sum += m
#     return sum

# print(multIA(-5, 6))

# def everyOther(list1):
#     listAlter = []
#     for i in range(0, len(list1), 2):
#         listAlter.append(list1[i])
#     return listAlter

# print(everyOther([1, 2, 3, 4, 5]))

# def cat6(l):
#     return l + [6]
# print(cat6([1, 2, 3, 4, 5]))

# def cyRange(n):
#     i = 0
#     list1 = []
#     while i<n:
#         list1.append(i)
#         i +=1
#     return list1
# print(cyRange(8))

import math
def mean(list1):
    if len(list1)==0:
        return None
    return float(sum(list1))/len(list1)

def stddev(list1):
    if len(list1)<2:
        return 0
    else:
        stdmean = 0
        numMean = mean(list1)
        return math.sqrt(1/len(list1)*sum([(i-numMean)**2 for i in list1]))
print(stddev([1, 3, 2, 4]))


def piSeries(n):
    for i in range(n):
        return 4*sum([(-1)**i/(2*i+1) for i in range(n)])
    
def evalPolynomial(coeffs, x):
    return sum([coeffs[-i-1]*x**i for i in range(len(coeffs))])

print(evalPolynomial([1, 2, 3], 2))

import math

def within(x, y, eps):
    return abs(x-y)<eps
def numTerms(eps):
    i = 1
    x = 4
    y = math.pi
    while not within(x, y, eps):
        x += 4*(-1)**(i)/(2*i+1)
        i+=1
    return i

print(numTerms(1))

def zeroVector(n):
    return [0 for i in range(n)]

print(zeroVector(10))

def zeroArray(x, y):
    return [[0 for m in range(y)] for n in range(x)]

print(zeroArray(3,4))

import datetime
import time


def sumArray(a):
    return sum([x for i in a for x in i])


# Second Solution
def sumArray1(a):
    sum1 = 0
    for i in range(len(a)):
        sum1 += sum(a[i])
    return sum1

# time1 = time.time()
# print(sumArray(list1))
# time2 = time.time()
# print(sumArray1(list1))
# time3 = time.time()
# print("Time of first solution is {}".format(time2-time1))
# print("Time of second solution is {}".format(time3-time2))
def addEntry(al, k, v):
    return al.append([k, v])

def lookup(al, k):
    for i in range(len(al)):
        if al[i][0] == k:
            return al[i]
    return None
            