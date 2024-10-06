from tkinter import *
from tkinter import ttk

def create_window():
    new_window = Tk()
    
    Label(new_window,text="login",width=50,height=25).pack()


    #old_window.destroy()

    


old_window = Tk()
notebook = ttk.Notebook(old_window)

img=PhotoImage(file='C://Users//PC//OneDrive//Pictures//Saved Pictures//Image.png')
old_window.iconphoto(False,img)



tab1 = Frame(notebook)
tab2 = Frame(notebook)


notebook.add(tab1,text="home")
notebook.add(tab2,text="ght")
notebook.pack(expand=True,fill="both")

Button = Button(tab1,text="login",command=create_window).pack()
Label(tab1,text="hey man",width=50,height=25).pack()
Label(tab2,text="he man",width=50,height=25).pack()



old_window.mainloop()
