from tkinter import * 
from tkinter import messagebox as mb 
import pymysql 

conobj = pymysql.connect (host = 'localhost', user='root', password='', port =3306)
curobj =conobj.cursor ()
#curobj.execute ('create database MyClg;')
curobj.execute ('use MyClg;')
#curobj.execute ('create table info (FName varchar (20),LName varchar (20),Email varchar (30),UserId varchar (25) primary key,Gender varchar (10),Branch varchar (15), Passsword varchar (20));')
curobj.close () 
conobj.close ()

win1 = Tk ()
def Submit () : 
	Fname = RFname.get ()
	Lname = RLname.get ()
	Email= REid.get ()
	Uid=RUid .get ()
	Gender= Gvar.get ()
	branch = Branch.get ()
	Pwd= RPwd.get () 
	#print (Fname, Lname, Email,Uid, Gender, branch, Pwd )
	conobj = pymysql.connect (host = 'localhost', user='root', password='', port =3306)
	curobj =conobj.cursor ()
	curobj.execute ('use MyClg;')
	r= 'insert into info values ("{FName}", "{LName}", "{Email}", "{UserId}", "{Gender}", "{Branch}", "{Password}");'
	r1= r.format (FName =Fname,LName= Lname, Email=Email, UserId=Uid, Gender=Gender, Branch=branch,Password=Pwd)
	curobj.execute (r1)
	conobj.commit ()
	curobj.close () 
	conobj.close ()
	mb.showinfo ('showinfo', "Sucessfully Submit Record")
	win1.destroy ()
	#import newuser

def ReSet ():
	RFname.delete(0, END )
	RLname.delete (0,END)
	REid.delete (0,END)
	RUid.delete (0,END)
	Branch.set ("Select")
	Gvar.set (None)
	RPwd.delete(0,END)
#win1.geometry('1000x600')
win1.maxsize (700, 900 )
win1.minsize (700, 900 )
win1.title ("Login Page")
win1.configure(bg='PaleGreen')

Gvar = StringVar (win1,None)
Branch= StringVar () 
Label (win1, text = "Please SignUp Here", font = ("Cooper", 22), bg = "#addbe6", fg="#000000",width=20, relief= "raised").place (x= 165, y = 20)

Label (win1, text = "Enter First Name ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 100)

RFname= Entry (win1,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
RFname . place (x= 370, y = 100)

Label (win1, text = "Enter Last Name ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 180)

RLname= Entry (win1,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
RLname . place (x= 370, y = 180)

Label (win1, text = "Enter Email Id ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 260)

REid= Entry (win1,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
REid . place (x= 370, y = 260)

Label (win1, text = "Enter User Id  ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 340)

RUid= Entry (win1,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
RUid . place (x= 370, y = 340)

Label (win1, text = "Select Gender", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 420)

 
r1= Radiobutton (win1,text = "Male",font = ("Constantia", 16), bg = "#808000", fg="#000000", variable=Gvar, value ="M")
r1.place (x= 370, y = 420)
r2= Radiobutton (win1,text = "FeMale", font = ("Constantia", 16), bg = "#808000", fg="#000000", variable=Gvar, value ="F")
r2.place (x= 470, y = 420)

Label (win1, text = "Select Branch  ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 500)


Branch.set ("Select Branch")

drop = OptionMenu(win1, Branch, 'Bsc.ITM',"Bsc.CS",'BCA','ME','Civil','CSE','EEE')
drop. place (x= 370, y = 500)

Label (win1, text = "Enter New Password ", font = ("Constantia", 16), bg = "#808000", fg="#000000",width=15, relief= "raised").place (x= 100, y = 580)

RPwd= Entry (win1,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" , show = "*")
RPwd . place (x= 370, y = 580)

Button (win1, text = 'Submit', font=("Elephant", 14), width=8,bg= "green", fg="white", relief= "raised", activebackground="red", command = Submit).place (x= 200, y = 650)

Button (win1, text = 'Reset', font=("Elephant", 14), width=8,bg= "yellow", fg="black", relief= "raised", activebackground="red", command = ReSet).place (x= 400, y = 650)

win1. mainloop () 