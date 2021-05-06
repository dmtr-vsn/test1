

import tkinter as tk
from tkinter import messagebox

mans_logs = tk.Tk()
mans_logs.title('Tic Tac Toe')
mans_logs.iconbitmap('x_square_cross_close_icon_184547.ico')

speletajs = True    # True == X, False = O
skaits = 0

def click_poga(poga):
    global speletajs, skaits
    if poga['text'] == ' ' and speletajs:
        poga['text'] = 'X'
        speletajs = False
        skaits += 1
        parbaudit_uzvaru()
    elif poga['text'] == ' ' and not speletajs:
        poga['text'] = 'O'
        speletajs = True
        skaits += 1
        parbaudit_uzvaru()
    else:
        messagebox.showerror('TicTacToe', 'Si rutina ir aiznemta')

def uzvara(s):
    if (poga_1['text'] == s and poga_2['text'] == s and poga_3['text'] == s or
        poga_4['text'] == s and poga_5['text'] == s and poga_6['text'] == s or
        poga_7['text'] == s and poga_8['text'] == s and poga_9['text'] == s or
        poga_1['text'] == s and poga_4['text'] == s and poga_7['text'] == s or
        poga_2['text'] == s and poga_5['text'] == s and poga_8['text'] == s or
        poga_3['text'] == s and poga_6['text'] == s and poga_9['text'] == s or
        poga_1['text'] == s and poga_5['text'] == s and poga_9['text'] == s or
        poga_3['text'] == s and poga_5['text'] == s and poga_7['text'] == s):
        return True
    else:
        return False

def parbaudit_uzvaru():
    global uzvaretajs
    uzvaretajs = False
    if uzvara('X'):         # uzvareja X
        messagebox.showinfo('TicTacToe', 'Speletajs X ir uzvarejis')
        uzvaretajs = True
        izslegt_pogu()
    elif uzvara('O'):      # uzvareja O
        messagebox.showinfo('TicTacToe', 'Speletajs O ir uzvarejis')
        uzvaretajs = True
        izslegt_pogu()
    elif skaits == 9 and not uzvaretajs:    # neizskirts
        messagebox.showinfo('TicTacToe', 'Neizskirts')
        izslegt_pogu()

def izslegt_pogu():
    poga_1.config(state=tk.DISABLED)
    poga_2.config(state=tk.DISABLED)
    poga_3.config(state=tk.DISABLED)
    poga_4.config(state=tk.DISABLED)
    poga_5.config(state=tk.DISABLED)
    poga_6.config(state=tk.DISABLED)
    poga_7.config(state=tk.DISABLED)
    poga_8.config(state=tk.DISABLED)
    poga_9.config(state=tk.DISABLED)

def atiestatit():
    poga_1.config(state=tk.NORMAL)
    poga_2.config(state=tk.NORMAL)
    poga_3.config(state=tk.NORMAL)
    poga_4.config(state=tk.NORMAL)
    poga_5.config(state=tk.NORMAL)
    poga_6.config(state=tk.NORMAL)
    poga_7.config(state=tk.NORMAL)
    poga_8.config(state=tk.NORMAL)
    poga_9.config(state=tk.NORMAL)

    poga_1['text'] = ' '
    poga_2['text'] = ' '
    poga_3['text'] = ' '
    poga_4['text'] = ' '
    poga_5['text'] = ' '
    poga_6['text'] = ' '
    poga_7['text'] = ' '
    poga_8['text'] = ' '
    poga_9['text'] = ' '

    global speletajs, skaits, uzvaretajs
    speletajs = True
    skaits = 0
    uzvaretajs = False

def info():
    jauns_logs = tk.Toplevel()
    jauns_logs.title('Par Programmu')
    jauns_logs.geometry('400x400')
    apraksts = tk.Label(jauns_logs, text='Te bus info par speli')
    apraksts.grid(row=0, column=0)

galvena_izvelne = tk.Menu(mans_logs)
mans_logs.config(menu=galvena_izvelne)
iespejas = tk.Menu(galvena_izvelne, tearoff=False)
parprogrammu = tk.Menu(galvena_izvelne, tearoff=False)
galvena_izvelne.add_cascade(label="Iespējas", menu=iespejas)
galvena_izvelne.add_cascade(label="Par programmu", menu=parprogrammu)

iespejas.add_command(label="Jauna spēle", command=atiestatit)
iespejas.add_command(label="Iziet", command=mans_logs.destroy)

parprogrammu.add_command(label="About", command=info)


poga_1 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_1))
poga_2 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_2))
poga_3 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_3))
poga_4 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_4))
poga_5 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_5))
poga_6 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_6))
poga_7 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_7))
poga_8 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_8))
poga_9 = tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(poga_9))

poga_1.grid(row=0, column=0)
poga_2.grid(row=0, column=1)
poga_3.grid(row=0, column=2)
poga_4.grid(row=1, column=0)
poga_5.grid(row=1, column=1)
poga_6.grid(row=1, column=2)
poga_7.grid(row=2, column=0)
poga_8.grid(row=2, column=1)
poga_9.grid(row=2, column=2)


mans_logs.mainloop()


#==========================================================

'''

import tkinter as tk
from tkinter import messagebox

speletajs = True    # True == X, False = 0
skaits = 0

def click_poga(poga):
    global speletajs, skaits
    if poga['text'] == ' ' and speletajs:
        poga['text'] = 'X'
        speletajs = False
        skaits += 1
        parbaudit_uzvaru()
    elif poga['text'] == ' ' and not speletajs:
        poga['text'] = 'O'
        speletajs = True
        skaits += 1
        parbaudit_uzvaru()
    else:
        messagebox.showerror('TicTacToe', 'Si rutina ir aiznemta')


def uzvara(s):
    if (poga_1['text'] == s and poga_2['text'] == s and poga_3['text'] == s or
        poga_4['text'] == s and poga_5['text'] == s and poga_6['text'] == s or
        poga_7['text'] == s and poga_8['text'] == s and poga_9['text'] == s or
        poga_1['text'] == s and poga_4['text'] == s and poga_7['text'] == s or
        poga_2['text'] == s and poga_5['text'] == s and poga_8['text'] == s or
        poga_3['text'] == s and poga_6['text'] == s and poga_9['text'] == s or
        poga_1['text'] == s and poga_5['text'] == s and poga_9['text'] == s or
        poga_3['text'] == s and poga_5['text'] == s and poga_7['text'] == s):
        return True
    else:
        return False

def parbaudit_uzvaru():
    global uzvaretajs
    uzvaretajs = False
    if uzvara('X'):         # uzvareja X
        messagebox.showinfo('TicTacToe', 'Speletajs X ir uzvarejis')
        uzvaretajs = True
    elif uzvara('O'):      # uzvareja O
        messagebox.showinfo('TicTacToe', 'Speletajs O ir uzvarejis')
        uzvaretajs = True
    elif skaits == 9 and not uzvaretajs:    # neizskirts
        messagebox.showinfo('TicTacToe', 'Neizskirts')
mans_logs = tk.Tk()
mans_logs.title('Tic Tac Toe')


pogas = []
for i in range(9):
    pogas.append(tk.Button(mans_logs, text=" ", width=6, height=3, font=("Helvetica",24), command=lambda:click_poga(pogas[i])))

for i in range(3):
    for j in range(3):
        pogas[i*3 + j].grid(row=i, column=j)


mans_logs.mainloop()



'''