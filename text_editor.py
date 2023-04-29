from tkinter import *
from tkinter import filedialog
def new_file():
    text.delete(0.0,END)
def open_file():
    file1=filedialog.askopenfile(mode='r')
    data=file1.read()
    text.delete(0.0,END)
    text.insert(0.0,data) #Inserts data
def save_file():
    filename="Untitled.txt"
    data=text.get(0.0,END)
    file1=open(filename,"w")
    file1.write(data)
def save_as():
    file1=filedialog.asksaveasfile(mode='w')
    data=text.get(0.0,END)
    file1.write(data)
gui=Tk() #tkinter object.
gui.title("Text Creator")
gui.geometry("800x1000")
text=Text(gui)
text.pack() #Display the text
mymenu=Menu()
list1=Menu()
list1.add_command(label='Create File',command=new_file) #Create menus.
list1.add_command(label='Save File',command=save_file)
list1.add_command(label='Save File As',command=save_as)
list1.add_command(label='Open File',command=open_file)
list1.add_command(label='Exit',command=gui.quit)
mymenu.add_cascade(label='File @CC text editor',menu=list1) #Create a file option.
gui.config(menu=mymenu)
gui.mainloop()