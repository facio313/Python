import psycopg2

class DaoSample:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
    
    def selects(self):
        mydict = []
        self.cursor.execute("select col01, col02, col03 from sample")
        data = self.cursor.fetchall()
        
        for i in data:
            mydict.append({"col01" : i[0], "col02" : i[1], "col03" : i[2]})
            
        return mydict
    
    def select(self, col01):
        self.cursor.execute(f"select col01, col02, col03 from sample where col01 = '{col01}'")
        data = self.cursor.fetchall()
        ret = {'col01':data[0][0], 'col02':data[0][1], 'col03':data[0][2]}
        return ret
    
    def insert(self, col01, col02, col03):
        self.cursor.execute(f"insert into sample values ('{col01}', '{col02}', '{col03}')")
        self.connection.commit()
        return self.cursor.rowcount

    def update(self, col01, col02, col03):
        self.cursor.execute(f"update sample set col02 = '{col02}', col03 = '{col03}' where col01 = '{col01}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, col01):
        self.cursor.execute(f"delete from sample where col01 = '{col01}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = DaoSample()
    
    list = ds.selects()
    print(list)
    
    sample = ds.select('1')
    print(sample)
    
    cnt = ds.insert('4', '4', '4')
    print(cnt)
    
    sample = ds.select('4')
    print(sample)
    
    cunt = ds.update('4', '6', '6')
    print(cunt)
    
    sample = ds.select('4')
    print(sample)
    
    cdnt = ds.delete('4')
    print(cdnt)
    
    list = ds.selects()
    print(list)