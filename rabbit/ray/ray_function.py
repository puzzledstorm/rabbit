import ray
# 本地启动 ray，如果想指定已有集群，在 init 方法中指定 RedisServer 即可
ray.init()

# 可以声明一个 remote function；
# remote 函数是 Ray 的基本任务调度单元，remote 函数定义后会立即被序列化存储到 RedisServer中，并且分配了一个唯一的 ID，这样就保证了集群的所有节点都可以看到这个函数的定义
@ray.remote
def f1(x):
    return x * x

@ray.remote
def f2(y):
    return y + 10

@ray.remote
def f3(x, y):
    return x + y

# 这里拿到的都是 future，相当于异步调用，只要调用 get 接口才会去拿计算的结果；通过 function.remote() 的方式调用这个函数
# 这里的 x/y 实际上拿到的都是 Object IDs
x = f1.remote(2)
y = f2.remote(3)
print(f"x:{x}, y:{y}")
# remote function 可以组合在一起使用
z = f3.remote(x, y)
print(f"z:{z}")

# get 接口可以通过 ObjectID 获取 ObjectStore 内的对象并将之转换为 Python 对象
# get 接口在调用时会阻塞，知道获取结果
print(ray.get(z))

####### 输出结果 ########
# 17