from threading import Thread
from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def func(name):
    for i in range(100):
        print(name,i)

def process_func():
    for i in range(100):
        print("子进程",i)


# t = Thread(target=func)
# t.start()

# p = Process(target=process_func)
# p.start()
# for i in range(100):
#     print("main",i)

# t1 = Thread(target=func,args=("t1",))

# t2 = Thread(target=func, args=("t2",))

# t1.start()

# t2.start()

#创建线程池
with ThreadPoolExecutor(50) as f:
    for i in range(100):
        f.submit(func,name = f"线程{i}")


#这个会等待线程池中任务全部执行完毕，才继续执行
print("123")