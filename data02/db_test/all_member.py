import data02.db.dao as dao

rows = dao.all()
#(('food', 'food', 'food', 'food'), ('melon', '123', 'melon', '123'), ('pen', 'pen', 'pen', 'pen'), ('watermelon', 'watermelon', 'watermelon', 'watermelon'), ('win', 'win', 'win', 'win'), ('win2', 'win2', 'win2', None), ('win3', 'win3', 'win3', 'win3'))
#튜플에 튜플을 가져온다


print('------')
# print('결과는 ' + row[0]+""+row[1]+""+row[2]+""+row[3])

# for i in range(0,len(rows)):
#     print(rows[i])

#위 코드와 같은거 이걸더 선호
for row in rows:
    # print(one)
    print('결과는 ' + row[0] + " " + row[1] + " " + row[2] + " " + row[3])

    # 아까 에러 떳던이유는 null 값이 안에 들어가있어서 출력이 안됬던것