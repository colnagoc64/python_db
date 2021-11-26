import diary.db.daoClass as dao

id= input('id:')

vo =list()
vo.append(id)

dao=dao.DAO()
dao.delete(vo)

print('------')