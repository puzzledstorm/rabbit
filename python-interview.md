# python collection

# everyday plan
```
1. 基础整理
2. 算法数据结构
```

## 基础
### 1. 装饰器
```
装饰器的一大特性是，能把被装饰的函数替换成其他函数。
第二个特性是，装饰器在加载模块时立即执行。而被装饰的函数只在明确调用时运行。
---
变量作用域规则: 要想在内部函数中使用外部变量，必须做global声明
---
闭包：
闭包指延伸了作用域的函数，其中包含函数定义体中引用、但是不在定义体中定义的非全局变量。
example:
def make_averager():
  series = []
  def averager(new_value):
    series.append(new_value)
    total = sum(series)
    return total/len(series)
  return averager
---
装饰器example：
https://puzzledstorm.github.io/posts/python-decorator/
```

### 2. 内置函数map reduce filter sorted zip enumerate partial operator 匿名函数lambda 
函数允许我们将复杂的问题分解为若干个子问题，并逐个解决。此外，它还可以减少重复性的代码，并为其他程序所重用。

lambda: lambda表达式，匿名函数。
```
f = lambda x: x*2+1
print(f(3))
```

map: 一一映射函数。输入变量为函数和序列，通过定义的函数对序列中的每个元素进行一一映射，返回的是一个列表。
```
ls = [1,2,3,4]
print(map(lambda x :x*x, ls) )
```

reduce: 函数接收两个参数，一个是函数，另一个是序列，但是，函数必须接收两个参数reduce把结果继续和序列的下一个元素做累积计算，其效果就是reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)。
```
from functools import reduce
ls = [1,2,3,4]
print(reduce(lambda x,y: x+y, ls))
```

filter: filter函数是使用限定条件进行过滤的函数。输入变量为函数和序列，通过指定的函数对序列中的每个元素进行过滤，返回的是一个Iterator（隋性序列），通过list函数可以获得所有结果的列表。
```
ls = [1,2,3,4]
print(list(filter(lambda x:x%2==1,ls)))
```
sorted: sorted函数是排序函数。输入变量为序列和函数，通过定义的函数对序列中的每个元素进行排序，返回的排序后的列表。
```
ls = [3,2,1,-4]
print(sorted(ls, key=lambda x: x*x) )

---
sorted 与 sort 的区别	
ls= [3,2,1,-4]

ls_ed=sorted(ls, key=lambda x: x*x) 
print(ls)		#-[3, 2, 1, -4]

ls.sort(key=lambda x: x*x )
print(ls)  # [1, 2, 3, -4]

sorted 与 sort 的区别
- 都可以使用可选参数key和reverse	
- sorted()可在列表，字符串和元组中使用，而sort()仅在列表中使用
ls= [3,2,1,-4]
ls_sorted=sorted( ls, key=abs, reverse=True) 
print(ls_sorted)		# [-4, 3, 2, 1]
str_sorted=sorted("spam")
print(str_sorted)		# ['a', 'm', 'p', 's']
```
zip: zip函数将多个可迭代的对象作为参数，依次将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的迭代器。
```
names=['张三','李四','王五'] 
sexs='男女男' 
scores=[86,92,75] 
for name,sex,score in zip(names,sexs,scores): 
    print('{}:{} {}'.format(name,sex,score)) 
```
enumerate: enumerate函数将一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据的下标。常用在for循环当中，可同时得到数据对象的值及对应的索引值.
```
list1 = ['zero', 'one', 'two', 'three', 'five'] 
for i, v in enumerate(list1):  	
    print('{}:{}'.format(i, v)) 
```
partial:
```
https://docs.python.org/3/library/functools.html#functools.partial
from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))
```
operator:
```
https://docs.python.org/3/library/operator.html
排序指南：
https://docs.python.org/zh-cn/3/howto/sorting.html

from operator import itemgetter, attrgetter

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=itemgetter(2))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

sorted(student_objects, key=attrgetter('age'))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


----
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
    ]
def multisort(xs, specs):
    for key, reverse in reversed(specs):
        xs.sort(key=attrgetter(key), reverse=reverse)
    return xs

multisort(list(student_objects), (('grade', True), ('age', False)))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

```

### 3. 深浅拷贝
```
浅拷贝(会创建新对象，其内容是原对象的引用)
简单而言，假定L1是L的浅拷贝，则有
L1 is L          False
L1[i] is L[i]    True
有五种形式：
切片操作
    L1 = L[:]
列表推导式
    L2 = [ item for item in L]
工厂函数
    L3 = list(L)
list.copy函数
    L4 = L.copy()
copy模块中的copy函数
    L5 = copy.copy(L)

深拷贝(拷贝对象的所有元素，包括多层嵌套的元素)
  只有一种形式：
copy模块中的deepcopy函数
    Ldc = copy.deepcopy(L)
简单而言，假定Ldc是L的深拷贝，则Ldc是一个全新的对象，不再与L有任何关联
Ldc is L          False
Ldc[i] is L[i]    False

```

### 4. 线程，进程，协程
### 5. 上下文管理器
### 6. unittest单元测试
### 7. 生成器generator、迭代器iterator
### 8. 魔法函数
```
https://www.zywvvd.com/notes/coding/python/python-magic-func/python-magic-func/
```

### 9. 面向对象(封装、继承、多态)

## pandas numpy opencv等常用三方库

## 框架

## 分布式

## 数据结构

## 算法

## 云原生kubernetes

## 多媒体处理

## linux

## 数据库

## 机器学习

## 深度学习

## 自动化流程

## 计算机网络

## 操作系统

## 数学基础

## 工具

## java, javascript，go

