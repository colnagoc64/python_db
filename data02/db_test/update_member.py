import data02.db.dao as dao

id= input('id:')
pw= input('pw:')
tel= input('tel:')

# 순서값에 맞게 dao에 list 순서가 pw tel id 이니깐 여기서도 순서대로
vo =list()
vo.append(pw)
vo.append(tel)
vo.append(id)


dao.update(vo)

print('------')