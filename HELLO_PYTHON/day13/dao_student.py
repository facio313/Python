import psycopg2

class Dao:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
    
    def selects(self):
        mydict = []
        self.cursor.execute("select s_id, s_name, mobile, address from student order by s_id")
        data = self.cursor.fetchall()
        
        for i in data:
            mydict.append({"s_id" : i[0], "s_name" : i[1], "mobile" : i[2], "address" : i[3]})
            
        return mydict
    
    def select(self, s_id):
        self.cursor.execute(f"select  s_id, s_name, mobile, address from student where s_id = '{s_id}'")
        data = self.cursor.fetchall()
        row = {'s_id':data[0][0], 's_name':data[0][1], 'mobile':data[0][2], 'address':data[0][3]}
        return row
    
    def insert(self, s_id, s_name, mobile, address):
        self.cursor.execute(f"insert into student values ('{s_id}', '{s_name}', '{mobile}', '{address}')")
        self.connection.commit()
        return self.cursor.rowcount

    def update(self, s_id, s_name, mobile, address):
        self.cursor.execute(f"update student set s_name = '{s_name}', mobile = '{mobile}', address = '{address}' where s_id = '{s_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, s_id):
        self.cursor.execute(f"delete from student where s_id = '{s_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = Dao()
    
    list = ds.selects()
    print(list)
    
    sample = ds.select(1)
    print(sample)
    
    cnt = ds.insert(4, '4', '4', 1)
    print(cnt)
    
    sample = ds.select(4)
    print(sample)
    
    cunt = ds.update(4, '6', '6', 1)
    print(cunt)
    
    sample = ds.select(4)
    print(sample)
    
    cdnt = ds.delete(4)
    print(cdnt)
    
    list = ds.selects()
    print(list)