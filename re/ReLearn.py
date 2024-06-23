import re

lst = re.findall(r"\d+","移动客服电话：10086，联通客服电话：10010")
print(lst)

lt = re.finditer(r"\d+","移动客服电话：10086，联通客服电话：10010")
for i in lt:
    print(i)
