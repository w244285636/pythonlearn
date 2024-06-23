#豆瓣top电影解析

import requests
import re
import mysql.connector
import csv

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "xxxx",
    database = "wuk_python",
    charset = "utf8mb4"
)
cursor = db.cursor();

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

f = open("doubandata.csv",mode="a+",encoding='utf-8')
csvwriter = csv.writer(f)
for page in range(0,10):
    url = "https://movie.douban.com/top250?start=%s&filter="% (page * 25)
    resp = requests.get(url=url,headers=headers);
    page_content = resp.text
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?导演: (?P<direct>.*?)'
                 r'&nbsp.*?<br>(?P<year>.*?)&nbsp.*?/&nbsp;(?P<region>.*?)&nbsp.*?/&nbsp;(?P<types>.*?)</p>.*?'
                 r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)
    result = obj.finditer(page_content)

    
    for it in result:
        print(it.group("name"))
        print(it.group("direct").strip())
        print(it.group("year").strip())
        print(it.group("region"))
        print(it.group("types").strip())
        print(it.group("score"))

        datadic = it.groupdict()
        datadic["direct"] = datadic["direct"].strip()
        datadic["year"] = datadic["year"].strip()
        datadic["types"] = datadic["types"].strip()
        csvwriter.writerow(datadic.values())

    #     # dir = it.group("direct").strip();
    #     # print(dir.encode('utf-8'))
    #     query_sql = "select * from douban_rank_list where move_name = \'%s\'" % it.group("name")
    #     print(query_sql)
    #     cursor.execute(query_sql)
    #     result = cursor.fetchall();
    #     if len(result) == 0:
    #         sql = "insert into douban_rank_list (move_name,score,types,regions,release_date,directors) values (\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')".format(
    #         it.group("name"),it.group("score"),it.group("types").strip(),it.group("region"),
    #         it.group("year").strip(),it.group("direct").strip()
    #         )
    #         print(sql)
    #         cursor.execute(sql)
    #         db.commit()
    #     else:
    #         sql = "update douban_rank_list set score = \'{}\',types = \'{}\',regions = \'{}\',release_date = \'{}\',directors = \'{}\' where move_name =  \'{}\' ".format(
    #             it.group("score"),it.group("types").strip(),it.group("region"),
    #             it.group("year").strip(),it.group("direct").strip(),
    #             it.group("name")
    #         )
    #         print(sql)
    #         cursor.execute(sql)
    #         db.commit()
    #     print("---------")
f.close
resp.close
cursor.close
db.close