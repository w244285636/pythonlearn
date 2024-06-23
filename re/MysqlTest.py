import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "xxx",
    database = "wuk_python"
)

cursor = db.cursor();

cursor.execute("select * from douban_rank_list")

result = cursor.fetchall();

for row in result:
    print(row)
db.close
