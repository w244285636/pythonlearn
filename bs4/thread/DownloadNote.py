#多线程下载《西游记》

# 异步文件操作  
# pip install aiofiles

#原始链接
url = "http://dushu.baidu.com/api/pc/getCatalog?data={\"book_id\":\"4306063500\"}"

contentUrl = "http://dushu.baidu.com/api/pc/getChapterContent?data={\"book_id\":\"4306063500\",\"cid\":\"4306063500|1569782244\",\"need_bookinfo\":1}"

import requests
import aiohttp
import asyncio
import aiofiles
import json

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}


def get_item_cid(url):
    resp = requests.get(url,headers=headers)
    return resp.json()["data"]["novel"]["items"]


async def get_content(b_id,c_id,title):

    data = {
        "book_id":b_id,
        "cid":f"{b_id}|{c_id}",
        "need_bookinfo":1
    }

    #json转变为string
    data = json.dumps(data)
    title = title + ".txt"

    url = f"http://dushu.baidu.com/api/pc/getChapterContent?data={data}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url,headers=headers) as resp:
            content = await resp.json()

            async with aiofiles.open(title,mode="w",encoding="utf-8") as f:
                 await f.write(content["data"]["novel"]["content"])
    print(title + "写入完成")
           


if __name__=='__main__':

    item_info = get_item_cid(url)

    b_id = "4306063500"
    tasks = []
    loop = asyncio.new_event_loop()
    for i in item_info:
        # print(i["title"])
        # print(i["cid"])
        tasks.append(loop.create_task(get_content(b_id,i["cid"],i["title"])))    

    # task = [
    #     loop.create_task(i) for i in [get_content(contentUrl,"第一章")]
    # ]

    loop.run_until_complete(asyncio.wait(tasks))
