#pip install aiohttp
#requests.get() -- 同步网络请求  aiohttp---异步请求

# 注意 这里一开始把py文件名命名为aiohttp 导致import时候默认导入自己的文件而不是aiphttp库 
import aiohttp
import asyncio
import time

urls = [
    "https://i1.huishahe.com/uploads/tu/201911/9999/9ceb92f5ea.jpg",
    "https://i1.huishahe.com/uploads/allimg/202205/9999/a703018f22.jpg",
    "https://i1.huishahe.com/uploads/tu/201910/9999/124e5f8c94.jpg"
]

url1 = "https://i1.huishahe.com/uploads/tu/201911/9999/9ceb92f5ea.jpg"
url2 = "https://i1.huishahe.com/uploads/allimg/202205/9999/a703018f22.jpg"
url3 = "https://i1.huishahe.com/uploads/tu/201910/9999/124e5f8c94.jpg"

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #请求结束。写入文件
            with open(name, mode="wb") as f:
                f.write(await resp.content.read()) #读取内容异步，需要await挂起
    print(name,"保存成功")

async def func1():
    print("start1")
    await asyncio.sleep(2)
    # time.sleep(2)
    print("end1")

async def func2():
    print("start2")
    await asyncio.sleep(4)
    # time.sleep(4)
    print("end2")

async def func3():
    print("start3")
    await asyncio.sleep(5)
    # time.sleep(4)
    print("end3")

async def func():

    # 这样会报错 pthon3.11后 直接传一个协程对象会报错
    # 得传task
    # tasks = [
    #     func1(),
    #     func2(),
    #     func3()
    # ]
    # 这样会报错

    loop = asyncio.new_event_loop()

    tasks = [
        loop.create_task(i) for i in [func1(),func2(),func3()]
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    # await asyncio.gather(func1(),func2(),func3())

def asyncTask():
    downloadTasks = []
    for url in urls:
        downloadTasks.append(aiodownload(url))

    loop = asyncio.new_event_loop()

    tasks = [
        loop.create_task(i) for i in [downloadTasks]
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    

async def asyncTest():
    # print("testtest")
    # 使用gather代替wait
    await asyncio.gather(func1(),func2(),func3())



    # 这种wait方法运行报错，改用gather方法
    # await asyncio.wait(func1(),func2(),func3())

if __name__=='__main__':
    # # asyncio.run(asyncTask())
    # asyncio.run(asyncTest())
    # asyncio.run(func())
    print("asyncio start")
    t1 = time.time()
    # loop = asyncio.new_event_loop()

    # tasks = [
    #     loop.create_task(i) for i in [func1(),func2(),func3()]
    # ]
    # loop.run_until_complete(asyncio.wait(tasks))
    # asyncTask()

    loop = asyncio.new_event_loop()

    tasks = [
        loop.create_task(i) for i in [aiodownload(url1),aiodownload(url2),aiodownload(url3)]
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    t2 = time.time()
    print(t2 - t1)



