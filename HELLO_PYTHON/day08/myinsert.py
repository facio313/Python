import psycopg2

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor()

sql = """
insert into sample (col01, col02, col03)
values ('4', '3', '3')
"""
cursor.execute(sql)
connection.commit()
print("cnt", cursor.rowcount)

cursor.execute("select col01, col02, col03 from sample")
data = cursor.fetchall()
print(data)

cursor.close()
connection.close()