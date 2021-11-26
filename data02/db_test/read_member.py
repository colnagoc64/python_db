import data02.db.dao as dao

id= input('id:')


row = dao.read(id) #('win', 'win', 'win', 'win')

print('------')
print('결과는 ' + row[0]+""+row[1]+""+row[2]+""+row[3])
#모듈을 만들 때는 각자의 역활에 충실하도록, 역활을 섞어서 만들면 안된다.
#응집도