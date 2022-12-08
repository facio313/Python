import psycopg2

class Dao:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
    
    def selects(self):
        mydict = []
        self.cursor.execute("select e_id, e_name, sex, addr from emp order by e_id")
        data = self.cursor.fetchall()
        
        for i in data:
            mydict.append({"e_id" : i[0], "e_name" : i[1], "sex" : i[2], "addr" : i[3]})
            
        return mydict
    
    def select(self, e_id):
        self.cursor.execute(f"select  e_id, e_name, sex, addr from emp where e_id = '{e_id}'")
        data = self.cursor.fetchall()
        row = {'e_id':data[0][0], 'e_name':data[0][1], 'sex':data[0][2], 'addr':data[0][3]}
        return row
    
    def insert(self, e_id, e_name, sex, addr):
        self.cursor.execute(f"insert into emp values ('{e_id}', '{e_name}', '{sex}', '{addr}')")
        self.connection.commit()
        return self.cursor.rowcount

    def update(self, e_id, e_name, sex, addr):
        self.cursor.execute(f"update emp set e_name = '{e_name}', sex = '{sex}', addr = '{addr}' where e_id = '{e_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, e_id):
        self.cursor.execute(f"delete from emp where e_id = '{e_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = Dao()
    
    list = ds.selects()
    print(list)
    
    sample = ds.select('1')
    print(sample)
    
    cnt = ds.insert('4', '4', '4', '4')
    print(cnt)
    
    sample = ds.select('4')
    print(sample)
    
    cunt = ds.update('4', '6', '6', '6')
    print(cunt)
    
    sample = ds.select('4')
    print(sample)
    
    cdnt = ds.delete('4')
    print(cdnt)
    
    list = ds.selects()
    print(list)