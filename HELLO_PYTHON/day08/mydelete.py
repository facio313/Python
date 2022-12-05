import psycopg2

col01 = '4'

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()

sql = f"""
delete from sample
where col01 = '{col01}'
"""
# f스트링은 파이썬 3.5부터 쓸 수 있음
# .format(col02, col03, col01)

cursor.execute(sql)
connection.commit()
print("cnt", cursor.rowcount)

cursor.execute("select col01, col02, col03 from sample")
data = cursor.fetchall()
print(data)

cursor.close()
connection.close()