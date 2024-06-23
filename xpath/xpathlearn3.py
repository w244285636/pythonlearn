import requests
from lxml import etree
import time

#从网页中获取图片
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

resp = requests.get(url=url,headers=headers)
resp.encoding = "UTF-8"

tree = etree.HTML(resp.text)

# item_list = tree.xpath("/html/body/div[@class='Clbc_Game']/div[@ id='load-img']/div[@class='listlbc_cont_l']/div[@class='Clbc_Game_l_a']/div[id='infinite_scroll']/div")

item_list = tree.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/div[1]/div")
# item_content = tree.xpath("/html/body/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/span/a/text()")
# print(item_content)


for item in item_list:
    origin_photo_url = item.xpath("./div[1]/div/a/img/@data-original")[0]
    
    name = origin_photo_url.split("/")[-1]
    print(name)
    phtoto_resp = requests.get(origin_photo_url,headers=headers,verify=False)
    with open("img/"+name,mode="wb") as f:
        f.write(phtoto_resp.content)
    
    time.sleep(1)
print("photo save end")
