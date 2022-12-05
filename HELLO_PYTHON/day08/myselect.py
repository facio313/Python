import psycopg2

connection = psycopg2.connect(database="python", user="postgres", password="python")
cursor = connection.cursor() # java의 statement / oracle의 cursor와는 다름

cursor.execute("select col01, col02, col03 from sample")
data = cursor.fetchall() # 하나 하나 가져오기보다는 파이썬 입장에선 한 번에 다 가져오는 게 나음. 남음 건 어쩌고 되기 때문에
print(data)

cursor.close() # memory leak 방지
connection.close()

# from sympy.polys.polyconfig import query
#
# class Databases():
#     def __init__(self):
#         self.db = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
#         self.cursor = self.db.cursor()
#
#     def __del__(self):
#         self.db.close()
#         self.cursor.close()
#
#     def execute(self,query,args={}):
#         self.cursor.execute(query,args)
#         row = self.cursor.fetchall()
#         return row
#
#     def commit(self):
#         self.cursor.commit()
#
# if __name__ == "__main__":
#     query = "SELECT * FROM SAMPLE"
#     db = Databases()
#     print(db.execute(query))
