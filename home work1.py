from tkinter import *
import tkinter.ttk as ttk1
def knopka():
    print("Все работает хорошо")
root = Tk()
root.geometry('430x220+430+220')
frm = ttk1.Frame(root, padding=100)
root.title("Заголовок окна программы")
root.geometry("480x280")
frm.pack()
Button(text="Это кнопка",
         foreground="blue",  # цвет текста
         padx="100",  # отступ от границ до содержимого по горизонтали
         pady="40",  # отступ от границ до содержимого по вертикали
         font="16",  # высота шрифта
         command=knopka
        ).pack(sid=TOP)


root.mainloop()