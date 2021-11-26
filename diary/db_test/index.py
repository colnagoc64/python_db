from tkinter import *

import diary.db.daoClass as dao

dao = dao.DAO()
def create():
    vo = [title_text.get(),content_text.get()]

    dao.create(vo)

def delete():
    pass


w = Tk() # 화면 프레임
w.geometry('500x800')
w.config(bg='lightgray')

icon = PhotoImage(file='car.png')
dogLabel = Label(w, image=icon)
dogLabel.pack() # pack 그래픽에 올려두는 함수


title_label = Label(w, text='title', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
title_label.pack()

title_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
title_text.pack()

content_label = Label(w, text='content', font=('맑은 고딕', 20), bg='lightgray', fg='blue')
content_label.pack()

content_text = Entry(w, font=('맑은 고딕', 20), bg='yellow', fg='red')
content_text.pack()

button = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='글작성', command=create)
button.pack()

button2 = Button(w, width=30, height=3, bg='green', font=('맑은 고딕', 10), text='글삭제', command=delete)
button2.pack()

w.mainloop() # 화면에 떠야하니깐 loop가 마지막