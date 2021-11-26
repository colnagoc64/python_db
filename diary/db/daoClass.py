import pymysql

class DAO():
    def __init__(self):
        self.conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')
        print('1. db연결 성공',self.conn)

        self.cur = self.conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',self.cur)
    def create(self,vo):
        sql = "insert into diary (writeday, title,content) values (now(),%s,%s)"
        result = self.cur.execute(sql,vo)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        self.conn.commit()
        self.conn.close()

    def update(self,vo):
        sql = "update diary set title= (%s) ,content= (%s) where id =(%s)"
        result = self.cur.execute(sql,vo)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        self.conn.commit()
        self.conn.close()

    def delete(self,vo):
        sql = "delete from diary  where id =(%s)"
        result = self.cur.execute(sql,vo)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        self.conn.commit()
        self.conn.close()

    def read(self,id):
        sql = "select * from diary  where id =(%s)"
        result = self.cur.execute(sql,id)

        row =self.cur.fetchone() # cur함수 가져와라  row 하나가져와라
        print(row)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        self.conn.commit()
        self.conn.close()

        return row

    def all(self):
        sql = "select * from diary "
        result = self.cur.execute(sql)

        rows = self.cur.fetchall()
        print(len(rows))
        print('3. sql문을 만들어서 mysql로 보낸다:', result)
        print(rows)

        self.conn.commit()
        self.conn.close()

        return rows


if __name__ == '__main__':
    dao = DAO()
    dao.create(['test', 'test', 'test', 'test'])


