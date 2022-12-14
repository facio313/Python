import psycopg2

class Dao:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
    
    def selects(self):
        mydict = []
        self.cursor.execute("select t_id, t_name, mobile, addr from teacher order by t_id")
        data = self.cursor.fetchall()
        
        for i in data:
            mydict.append({"t_id" : i[0], "t_name" : i[1], "mobile" : i[2], "addr" : i[3]})
            
        return mydict
    
    def select(self, t_id):
        self.cursor.execute(f"select  t_id, t_name, mobile, addr from teacher where t_id = '{t_id}'")
        data = self.cursor.fetchall()
        row = {'t_id':data[0][0], 't_name':data[0][1], 'mobile':data[0][2], 'addr':data[0][3]}
        return row
    
    def insert(self, t_name, mobile, addr):
        self.cursor.execute(f"insert into teacher values (nextval('t_seq'), '{t_name}', '{mobile}', '{addr}')")
        self.connection.commit()
        return self.cursor.rowcount

    def update(self, t_id, t_name, mobile, addr):
        self.cursor.execute(f"update teacher set t_name = '{t_name}', mobile = '{mobile}', addr = '{addr}' where t_id = '{t_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, t_id):
        self.cursor.execute(f"delete from teacher where t_id = '{t_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    dt = Dao()
    teacher = dt.select(5)
    print(teacher)
