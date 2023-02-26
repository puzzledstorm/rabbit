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

### 2. 内置函数map, reduce, filter，sorted zip enumerate partial operator 匿名函数lambda 
函数允许我们将复杂的问题分解为若干个子问题，并逐个解决。此外，它还可以减少重复性的代码，并为其他程序所重用。

lambda: lambda表达式，匿名函数。
```
f = lambda x: x*2+1
print(f(3))
```

map: 一一映射函数。输入变量为函数和序列，通过定义的函数对序列中的每个元素进行一一映射，返回的是一个列表。
```
ls= [1,2,3,4]
print( map(lambda x :x*x, ls) )
```

reduce: 函数接收两个参数，一个是函数，另一个是序列，但是，函数必须接收两个参数reduce把结果继续和序列的下一个元素做累积计算，其效果就是reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)。
```
from functools import reduce
ls= [1,2,3,4]
print(reduce(lambda x,y: x+y, ls))
```

filter: filter函数是使用限定条件进行过滤的函数。输入变量为函数和序列，通过指定的函数对序列中的每个元素进行过滤，返回的是一个Iterator（隋性序列），通过list函数可以获得所有结果的列表。
```
ls= [1,2,3,4]
print(list(filter(lambda x:x%2==1,ls)))
```

partial:

operator:
```
```

### 3. 深浅拷贝
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

