from tkinter import *
import tkinter.ttk as ttk1

def knopka():
    print("Все работает хорошо")
root = Tk()
frm = ttk1.Frame(root, padding=100)
root.title ("Заголовок окна программы")
root.geometry("480x280")
frm.grid()
Button( text="Это кнопка",
         foreground="blue",  # цвет текста
         padx="100",  # отступ от границ до содержимого по горизонтали
         pady="50",  # отступ от границ до содержимого по вертикали
         font="16",  # высота шрифта
         command = knopka
        ).grid(column=1, row=1)

root.mainloop()