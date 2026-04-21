import time
# 计时器
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__}运行的时间为{t2 - t1}")
        return result
    return wrapper
