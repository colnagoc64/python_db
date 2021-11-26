import data02.db.dao as dao

id= input('id:')
pw= input('pw:')
name= input('name:')
tel= input('tel:')


# 값을 전달할 때 묶어서 보내는 역활의 클래스(data transfer object, DTO , value Object, VO)
# list를 선호해서 list를만들어서 전달

vo =list()
vo.append(id)
vo.append(pw)
vo.append(name)
vo.append(tel)

# v02 = [id,pw,name,tel]
# data02.db_test.dao.create(id,pw,name,tel)
# data02.db_test.dao.create(vo)

dao.create(vo)

print('------')