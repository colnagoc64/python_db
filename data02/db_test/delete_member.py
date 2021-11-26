import data02.db.dao as dao

id= input('id:')

vo =list()
vo.append(id)

dao.delete(vo)

print('------')