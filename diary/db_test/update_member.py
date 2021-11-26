import diary.db.daoClass as dao

id= input('id:')
title= input('title:')
content= input('content:')

# 순서값에 맞게 dao에 list 순서가 pw tel id 이니깐 여기서도 순서대로
vo =list()
vo.append(title)
vo.append(content)
vo.append(id)

dao=dao.DAO()
dao.update(vo)

print('------')