import tkinter as tk

# Калькулятор
#     0 1 2 3
#   -----------
# 0 | [     ] |
# 1 | C / % / |
# 2 | 7 8 9 X |
# 3 | 4 5 6 - |
# 4 | 1 2 3 + |
# 5 | 0 0 . = |
#   -----------

# Цвета
WHITE = "#FFFFFF"
BLACK = "#000000"
ORANGE = "#FE9505"
DARK_GRAY = "#333333"
LIGHT_GRAY = "#A5A5A5"

# Размеры кнопок
BTN_HEIGHT = 3

PADY, PADX = 8, 7

ROOT = tk.Tk()
ROOT.title("Calculator")
ROOT.config(bg='#000000')
ROOT.resizable(False, False)
ROOT.geometry(f"300x450+{ROOT.winfo_screenwidth() // 2 - 175}+{ROOT.winfo_screenheight() // 2 - 250}")

TEXT = "0"


def change():
    pass


def percent():
    pass


def equal():
    pass


def dot():
    pass


def clear():
    global TEXT
    TEXT = "0"
    sign.config(text=TEXT)


def number(button):
    global TEXT
    if TEXT == "0":
        TEXT = button["text"]
    else:
        TEXT += button["text"]
    sign.config(text=TEXT)


def operation():
    pass

# Кнопки цифр
btn_0 = tk.Button(text="0", command=lambda: number(btn_0))
btn_1 = tk.Button(text="1", command=lambda: number(btn_1))
btn_2 = tk.Button(text="2", command=lambda: number(btn_2))
btn_3 = tk.Button(text="3", command=lambda: number(btn_3))
btn_4 = tk.Button(text="4", command=lambda: number(btn_4))
btn_5 = tk.Button(text="5", command=lambda: number(btn_5))
btn_6 = tk.Button(text="6", command=lambda: number(btn_6))
btn_7 = tk.Button(text="7", command=lambda: number(btn_7))
btn_8 = tk.Button(text="8", command=lambda: number(btn_8))
btn_9 = tk.Button(text="9", command=lambda: number(btn_9))

# Кнопки операций
btn_multiply = tk.Button(text="x", command=operation)
btn_divide = tk.Button(text="/", command=operation)
btn_minus = tk.Button(text="-", command=operation)
btn_plus = tk.Button(text="+", command=operation)

# Другие кнопки
btn_plus_minus = tk.Button(text="+/-", command=change)
btn_percent = tk.Button(text="%", command=percent)
btn_equals = tk.Button(text="=", command=equal)
btn_dot = tk.Button(text=".", command=dot)
btn_c = tk.Button(text="C", command=clear)

# Список всех кнопок
buttons = [
    [btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9, btn_dot],
    [btn_multiply, btn_divide, btn_minus, btn_plus, btn_equals],
    [btn_plus_minus, btn_percent, btn_c]
]

# Настраиваем размер, цвет и команды кнопок
btn_0.config(width=18, height=BTN_HEIGHT)
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = buttons[i][j]
        text = btn["text"]
        if btn != btn_0:
            btn.config(width=7, height=BTN_HEIGHT)
        if i == 0:
            btn.config(bg=DARK_GRAY, fg=WHITE)
        elif i == 1:
            btn.config(bg=ORANGE, fg=WHITE)
        else:
            btn.config(bg=LIGHT_GRAY, fg=BLACK)




sign = tk.Label(width=8, text=TEXT, fg=WHITE, bg=BLACK, font=("Arial", 42))
sign.grid(row=0, column=0, columnspan=4, pady=PADY, padx=PADX)


buttons = [
    [btn_c, btn_plus_minus, btn_percent, btn_divide],
    [btn_7, btn_8, btn_9, btn_multiply],
    [btn_4, btn_5, btn_6, btn_minus],
    [btn_1, btn_2, btn_3, btn_plus],
    [None, None, btn_dot, btn_equals]
]
btn_0.grid(row=5, column=0, pady=PADY, padx=PADX, columnspan=2)
for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = buttons[i][j]
        if btn:
            btn.grid(row=i + 1, column=j, pady=PADY, padx=PADX)

if __name__ == '__main__':
    ROOT.mainloop()
