import diary.db.daoClass as dao


# writeday= input('writeday:')
title= input('title:')
content= input('content:')


# 값을 전달할 때 묶어서 보내는 역활의 클래스(data transfer object, DTO , value Object, VO)
# list를 선호해서 list를만들어서 전달

vo =list()
vo.append(title)
vo.append(content)


# v02 = [id,pw,name,tel]
# data02.db_test.dao.create(id,pw,name,tel)
# data02.db_test.dao.create(vo)

dao=dao.DAO()
dao.create(vo)

print('------')