from tkinter import *
import random
font = "Verdana 12 bold" #шрифт
BG = "#262622" #цвет фона
FG = "#F3F1ED" #цвет текста
BTNC = "#FF6800" #цвет кнопки
ACTIVE = "#CA883E" #цвет активного состояния

def generate():
    if ent1.get() == "":
        ent2.delete(0, END)
        ent2.insert(0, "Введите количество символов!")
    else:
        l = cb1_var.get()  # буквы
        ch = cb3_var.get()  # знаки
        n = cb2_var.get()  # числа
        if not l and not ch and not n:
            ent2.delete(0, END)
            ent2.insert(0, "Выберите символы!")
        else:
            c = int(ent1.get())  #кол-во символов

            alp = ""
            psw = ""
            if l == True:
                alp = alp + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            if ch == True:
                alp = alp + "@#$%&?"
            if n == True:
                alp = alp + "0123456789"
    
            for i in range(c):
                psw = psw + random.choice(alp)
            ent2.delete(0, END)
            ent2.insert(0, psw)


window = Tk()
window.title("Генератор паролей")
window.config(bg=BG)

lbl = Label(window, bg=BG, fg=FG, text="Введите количество символов:", font=font)
ent1 = Entry(window, font=font, relief=FLAT)
cb1_var = BooleanVar()
cb1 = Checkbutton(window, selectcolor=BG, activeforeground=ACTIVE, activebackground=BG, bg=BG, fg=FG,
                  text="Добавить буквы", variable=cb1_var, onvalue=True, offvalue=False, font=font)
cb2_var = BooleanVar()
cb2 = Checkbutton(window, selectcolor=BG, activeforeground=ACTIVE, activebackground=BG, bg=BG, fg=FG,
                  text="Добавить цифры", variable=cb2_var, onvalue=True, offvalue=False, font=font)
cb3_var = BooleanVar()
cb3 = Checkbutton(window, selectcolor=BG, activeforeground=ACTIVE, activebackground=BG, bg=BG, fg=FG,
                  text="Добавить символы", variable=cb3_var, onvalue=True, offvalue=False, font=font)
btn = Button(window, bg=BTNC, fg=FG, text="Сгенерировать пароль!", command=generate, font=font, activebackground=ACTIVE, relief=FLAT)
ent2 = Entry(window, width=30, font=font, relief=FLAT)


lbl.grid(row=0, column=0, padx=20, pady=20)
ent1.grid(row=0, column=1, padx=20, pady=20)
cb1.grid(row=1, column=0, padx=20, pady=20)
cb2.grid(row=1, column=1, padx=20, pady=20)
cb3.grid(row=2, column=0, padx=20, pady=20, columnspan=2)
btn.grid(row=3, column=0, padx=20, pady=20, columnspan=2)
ent2.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

window.mainloop()
