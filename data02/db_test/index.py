from tkinter import *

import data02.db.dao as dao

def create():
    vo = [id_text.get(),pw_text.get(),name_text.get(),tel_text.get()]
    # print(id_text.get())
    dao.create(vo)

def delete():
    pass


w = Tk() # 화면 프레임
w.geometry('500x800')
w.config(bg='lightgray')

icon = PhotoImage(file='car.png')
dogLabel = Label(w, image=icon)
dogLabel.pack() # pack 그래픽에 올려두는 함수

id_label = Label(w, text='아이디입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue') #앞에 w 에다가 넣을꺼야 사실주소값 넣어준거다
id_label.pack()

id_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
id_text.pack()

pw_label = Label(w, text='패스워드입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
pw_label.pack()

pw_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
pw_text.pack()

name_label = Label(w, text='이름입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
name_label.pack()

name_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
name_text.pack()

tel_label = Label(w, text='전화번호입력', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
tel_label.pack()

tel_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
tel_text.pack()

button = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원가입', command=create)
button.pack()

button2 = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='회원탈퇴', command=delete)
button2.pack()

w.mainloop() # 화면에 떠야하니깐 loop가 마지막