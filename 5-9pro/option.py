from tkinter import * 

win2 = Tk () 
def Add () :
	import newuser
def Search () :
	import search
def Delete () :
	import delete
def Update () :
	import update
def Display () :
	import display

win2.geometry('1000x600')
win2.maxsize (500, 300 )
win2.minsize (500, 300 )
win2.title ("Option Page")
win2.configure(bg='PaleGreen')

Button (win2, text = 'Add Student', font=("Elephant", 14), width=12,bg= "green", fg="yellow",relief= "raised", activebackground="red", command = Add ).place (x= 70, y = 50)

Button (win2, text = 'Search Student', font=("Elephant", 14), width=12,bg= "green", fg="yellow",relief= "raised",activebackground="red",command= Search).place(x= 260, y = 50)

Button (win2, text = 'Delete Student', font=("Elephant", 14), width=12,bg= "green", fg="yellow",relief= "raised", activebackground="red", command = Delete).place (x= 70, y = 120)

Button (win2, text = 'Update Info', font=("Elephant", 14), width=12,bg= "green", fg="yellow",relief= "raised", activebackground="red", command = Update).place (x= 260, y = 120)

Button (win2, text = 'Display All ', font=("Elephant", 14), width=12,bg= "green", fg="yellow",relief= "raised", activebackground="red", command = Display).place (x= 170, y = 190)


win2.mainloop () 
