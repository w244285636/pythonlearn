from lxml import etree

# current_path = os.getcwd()
# file_path = current_path + "\pythonlearn\xpath\test.html"
# print(file_path)

tree = etree.parse("pythonlearn/xpath/test.html")

result = tree.xpath("/html/body/ul/li[1]/a/text()") # 注意这里xpath是从1开始的

print(result)

herf_name = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()") # [@xxx=xxx] 属性值

print(herf_name)


ol_li_list = tree.xpath("/html//ol/li")

for li in ol_li_list:
    li_name = li.xpath("./a/text()")   #这里相对查找要./
    print(li_name)
    li_href_name = li.xpath("./a/@href") #属性取值
    print(li_href_name)

div_name = tree.xpath("/html/body/div[1]/text()")
print(div_name)