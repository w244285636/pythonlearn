#安装bs4 pip install bs4

import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/chart"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

#获取网页源码
resp = requests.get(url=url,headers=headers)

# with open("pythonlearn/bs4/bs4_douban.txt","w",encoding="utf-8") as f:
#     f.write(resp.text)

#解析数据
page = BeautifulSoup(resp.text,"html.parser")

#find(标签，属性)
#find_all(标签，属性)
table = page.find_all("table", attrs={
    "width":"100%"
})
# table2 = page.find("table", attrs={
#     "width":"100%"
# })
# # print(table2)
# m1 = table2.find("div", attrs={
#         "class":"pl2"
# })
# name = m1.find("a")
# chinese_name = name.text.replace('\n','').split("/")[0].strip()
# print(chinese_name)
# print(name.text.replace('\n','').strip().split("/"))
for li in table:
    # movie_info = li.find_all("div", attrs={
    #     "class":"p12"
    # })
    movie_info = li.find("div", attrs={
        "class":"pl2"}
    )
    name = movie_info.find("a")
    chinese_name = name.text.replace('\n','').split("/")[0].strip()
    print(chinese_name)
    movie_time_actor = movie_info.find("p")
    print(movie_time_actor.text)

    movie_star = movie_info.find("span",attrs={
        "class":"rating_nums"}
    )
    if movie_star is None:
        print("0")
    else:
        print(movie_star.text)
    print("-------")


