from tkinter import *
from tkinter.filedialog import *
win = Tk()
win.geometry('400x570')
win.title('Notebook')
#Button Function
def openfile():
    file = askopenfile(mode='r',filetypes=[('filename','*.txt')])
    if file is not None:
        content = file.read()
        text.insert(INSERT,content)
def savefile():
    new_file = asksaveasfile(mode='w',filetypes=[('filename','.txt')])
    if new_file  is None:
        return
        text1 = text.get(1.0,END)
        new_file.write(text1)
        new_file.close()
def clearfile():
    text.delete(1.0,END)
#text box
text = Text(win,font='impack 15 bold',bg='pink',wrap=WORD)
text.pack(padx=10,pady=40)
#buttons
Button(win,text='Open',font='poppins 15 bold',bg='blue',fg='white',bd=0,cursor='hand2',command=openfile).place(x=50,y=530)
Button(win,text='Save',font='poppins 15 bold',bg='green',fg='white',bd=0,cursor='hand2',command=savefile).place(x=130,y=530)
Button(win,text='Clear',font='poppins 15 bold',bg='purple',fg='white',bd=0,cursor='hand2',command=clearfile).place(x=210,y=530)
Button(win,text='Exit',font='poppins 15 bold',bg='orange',fg='white',bd=0,cursor='hand2',command=lambda :exit()).place(x=290,y=530)
mainloop()