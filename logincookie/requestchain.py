#网页防盗链
import requests

url = "https://www.pearvideo.com/video_1795088"

contId = url.split("_")[1]


videoUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.20977252056039"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Referer": url
}


resp = requests.get(url=videoUrl,headers=headers)

dic = resp.json()

#对返回数据进行重新拼接
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]

systemTime = dic["systemTime"]

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

# print(srcUrl)

# 下载视频
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(url=srcUrl).content)

