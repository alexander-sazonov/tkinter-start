from tkinter import *
def action_sum(event):
    numer1 = float(ent1.get())
    numer2 = float(ent2.get())
    result['text'] = numer1 + numer2
root = Tk()
ent1 = Entry(width=10)
ent2 = Entry(width=10)
btn_sum = Button(text='+')
btn_sum.bind('<Button-1>', action_sum)
btn_minus = Button(text='-')
btn_mul = Button(text='*')
btn_div = Button(text='/')
result = Label()
ent1.pack()
ent2.pack()
btn_sum.pack()
btn_minus.pack()
btn_mul.pack()
btn_div.pack()
result.pack()
root.mainloop()
