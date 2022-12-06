import psycopg2
from psycopg2 import extras

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor(cursor_factory=extras.DictCursor)

cursor.execute("select col01, col02, col03 from sample")
data = cursor.fetchall()

print(data)

cursor.close()
connection.close()
