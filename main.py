o = ""
text = ""

def command(sign, txt):
    sign.config(text=sign["text"] + txt)

def operation(sign):
    s = sign["text"]
    el1, el2 = map(int, s.split(o))
    if o == "+":
        result = el1 + el2
    elif o == "-":
        result = el1 - el2
    elif o == "x":
        result = el1 * el2
    else:
        result = el1 / el2
    sign.configure(text=str(result))

def clear_text(sign):
    sign.configure(text="")

def change_o(op, sign):
    sign.configure(text=sign["text"] + op)
    global o
    o = op
