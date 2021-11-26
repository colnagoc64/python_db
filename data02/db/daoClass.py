import pymysql

class DAO():

# def create(id,pw, name,tel):
    def create(self,vo):
        conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')

        print('1. db연결 성공',conn)

        cur = conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',cur)

        # sql = "insert into member values ('"+ id +"','"+pw +"','"+name+"','"+tel+"')"
        # sql = "insert into member values ('" + vo[0] + "','" + vo[1] + "','" + vo[2] + "','" + vo[3] + "')"
        sql = "insert into member values (%s,%s,%s,%s)" # 이게 제일 좋은코드 속도가 제일빠르다
        result = cur.execute(sql,vo) #execute 함수에의해서 자동으로 정확하게 넘겨줌
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        conn.commit()
        conn.close()

    def update(self,vo):
        conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')

        print('1. db연결 성공',conn)

        cur = conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',cur)

        sql = "update member set pw= (%s) ,tel= (%s) where id =(%s)"
        result = cur.execute(sql,vo)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        conn.commit()
        conn.close()

    def delete(self,vo):
        conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')

        print('1. db연결 성공',conn)

        cur = conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',cur)

        sql = "delete from member  where id =(%s)"
        result = cur.execute(sql,vo)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        conn.commit()
        conn.close()

    def read(self,id):
        conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')

        print('1. db연결 성공',conn)

        cur = conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',cur)

        sql = "select * from member  where id =(%s)"
        result = cur.execute(sql,id)

        row =cur.fetchone() # cur함수 가져와라  row 하나가져와라
        print(row)
        print('3. sql문을 만들어서 mysql로 보낸다:',result)

        conn.commit()
        conn.close()

        return row # 검색한 결과를 다시 넘겨준다. 그래서 return을 작성
         # 리턴값이 ('win', 'win', 'win', 'win')

    def all(self):
        conn= pymysql.connect(host='localhost',
                              port=3306,
                              user='root',
                              password='1234',
                              db='cloth',
                              charset='utf8')

        print('1. db연결 성공',conn)

        cur = conn.cursor()
        print('2. db 연결 스트림을 접근할 수 있는 객체 획득 성공',cur)

        sql = "select * from member "
        result = cur.execute(sql)

        rows =cur.fetchall()
        print(len(rows))
        print('3. sql문을 만들어서 mysql로 보낸다:',result)
        print(rows)

        conn.commit()
        conn.close()

        return rows #((),(),()) 튜플에 튜플일 가져온다





#해당 모듈이 main되어서 실행될떄만, 실행해주는 부분
if __name__ == '__main__':
    dao= DAO()
    dao.create('apple','apple','apple','apple')