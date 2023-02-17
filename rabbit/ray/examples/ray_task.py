import ray

ray.init()


@ray.remote
def f(x):
    return x * x


futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))  # [0, 1, 4, 9]

# 2023-02-15 14:47:40,919	INFO worker.py:1518 -- Started a local Ray instance.
# [0, 1, 4, 9]
