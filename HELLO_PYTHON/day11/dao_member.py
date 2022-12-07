import psycopg2

class MemberDao:
    def __init__(self):
        self.connection = psycopg2.connect(database="python", user="postgres", password="python")
        self.cursor = self.connection.cursor()
    
    def selects(self):
        mydict = []
        self.cursor.execute("select m_id, m_nm, tel, ymd from member")
        data = self.cursor.fetchall()
        
        for i in data:
            mydict.append({"m_id" : i[0], "m_nm" : i[1], "tel" : i[2], "ymd" : i[3]})
            
        return mydict
    
    def select(self, m_id):
        self.cursor.execute(f"select  m_id, m_nm, tel, ymd from member where m_id = '{m_id}'")
        data = self.cursor.fetchall()
        row = {'m_id':data[0][0], 'm_nm':data[0][1], 'tel':data[0][2], 'ymd':data[0][3]}
        return row
    
    def insert(self, m_id, m_nm, tel, ymd):
        self.cursor.execute(f"insert into member values ('{m_id}', '{m_nm}', '{tel}', '{ymd}')")
        self.connection.commit()
        return self.cursor.rowcount

    def update(self, m_id, m_nm, tel, ymd):
        self.cursor.execute(f"update member set m_nm = '{m_nm}', tel = '{tel}', ymd = '{ymd}' where m_id = '{m_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self, m_id):
        self.cursor.execute(f"delete from member where m_id = '{m_id}'")
        self.connection.commit()
        return self.cursor.rowcount
    
    def __del__(self):
        self.cursor.close()
        self.connection.close()
        
if __name__ == '__main__':
    ds = MemberDao()
    
    list = ds.selects()
    print(list)
    
    # sample = ds.select('1')
    # print(sample)
    
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