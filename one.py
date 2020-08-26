import tkinter as tk
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
from tkinter.filedialog import *
from tkinter import messagebox
filename=None
def newfile():
    global filename
    filename="Untitled"
    text.delete(0.0,END)
def savefile():
    global filename
    t=text.get(0.0,END)
    f=open(filename,'w')
    f.write(t)
    f.close()
def saveAs():
    f=asksaveasfile(mode='w',defaultextension=".txt")
    t=text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror("Title", "Message")

def openfile():
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)


app = tk.Tk()
app.title("Text Editor")
app.configure(background="black")
w=ttk.Scrollbar(app)
w.pack(side='right', fill='y')
style = ThemedStyle(app)
style.set_theme("equilux")
text=Text(app)
text.pack(side='left',fill='both')
w.config(command=text.yview)

menubar=Menu(app)
filemenu=Menu(menubar)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)




app.config(menu=menubar)
app.mainloop()
