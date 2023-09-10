from tkinter import * 
from tkinter import messagebox as mb  
import pymysql 
# user id = satya ,abinash   pass = satya,abinash


win = Tk ()
def Login () :
	uid =Luid.get ()
	pwd =Lpwd.get () 
	print (uid, '  ', pwd)
	conobj = pymysql.connect(host='localhost', user ='root',password='', port =3306 )
	curobj = conobj.cursor () 
	curobj.execute ('use MyClg;')
	#curobj.execute ('select UserId ,Password from info;')
	#data = curobj.fetchall ()
	test = f'select * from info where UserId= "{uid}" and Password= "{pwd}";'
	curobj.execute(test) 
	record = curobj.fetchall () 
	if len (record) : 
		mb.showinfo ('showinfo', "Login Sucess")
		win.destroy () 
		import option
		#win2.destroy () 
		 
	else : 
		mb.showerror ('showerror', "Please Try Next Time...")
	#print (data)
	curobj.close () 
	conobj.close ()   

def ReSet () : 
	Luid .delete (0, END)
	Lpwd .delete (0, END)
def Exit () : 
	win.destroy ()
#def NewUser () : 
#	import newuser 
 
win.geometry('1000x600')
win.maxsize (600, 600 )
win.minsize (600, 600 )
win.title ("Login Page")
win.configure(bg='PaleGreen')



Label (win, text = "Please Login Here", font = ("Cooper", 22), bg = "#addbe6", fg="#000000",width=20, relief= "raised").place (x= 120, y = 30)

Label (win, text = "Enter User Id ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 60, y = 150)

Luid= Entry (win,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
Luid . place (x= 320, y = 150)

Label (win, text = "Enter Password", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 60, y = 250)

Lpwd= Entry (win,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove", show = "*" )
Lpwd . place (x= 320, y = 250)

Button (win, text = 'Login', font=("Elephant", 14), width=8,bg= "green", fg="white", relief= "raised", activebackground="red", command = Login).place (x= 80, y = 400)

Button (win, text = 'Reset', font=("Elephant", 14), width=8,bg= "yellow", fg="black", relief= "raised", activebackground="red", command = ReSet).place (x= 240, y = 400)

Button (win, text = 'Exit', font=("Elephant", 14), width=8,bg= "green", fg="yellow",relief= "raised", activebackground="red",command= Exit).place (x= 410, y = 400)

#Button (win, text = 'Create New Account', font=("Elephant", 14), width=20,bg= "blue", fg="white",relief= "raised", activebackground="blue",command= NewUser).place (x= 160, y = 480)


win.mainloop ()  
 

