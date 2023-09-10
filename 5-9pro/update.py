from tkinter import * 
import pymysql

win6 = Tk () 

def UpdateFun   () :
	Uid = uuid .get ()
	Ucol= Update .get ()	
	Udata =udata.get () 
	print (Uid , Ucol ,Udata )
	conobj = pymysql.connect (host ='localhost', user ='root', password ='', port = 3306) 
	curobj = conobj .cursor () 
	curobj .execute ('use MyClg;')
	u= f'update info set {Ucol}= "{Udata}" where UserId = "{Uid}";'
	#print (u)
	curobj .execute (u)
	conobj.commit () 
	win6.destroy ()
	import option 
	curobj.close () 
	conobj.close()   

win6.maxsize (800, 300 )
win6.minsize (800, 300 )
win6.title ("Update  Page")
win6.configure(bg='PaleGreen')
Label (win6, text = "Enter UserId which want to Update", font = ("Cooper", 18), bg = "#addbe6", fg="#000000",width=28, relief= "raised"). place (x= 50, y = 100)

uuid =Entry (win6,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
uuid. place (x= 500, y = 100 ) 

Update= StringVar ()
Update .set ("Select Column Name")
drop = OptionMenu(win6, Update, 'Fname',"Lname",'Email','Gender','Dept')
drop. place (x= 300, y = 150)

udata =Entry (win6,width=18,font =("Constantia", 16), bg="#add8e6",fg= "#ff0000",relief= "groove" )
udata. place (x= 500, y = 150 ) 

Button (win6, text = 'Update', font=("Elephant", 14), width=20,bg= "blue", fg="white",relief= "raised", activebackground="blue", command = UpdateFun  ).place (x= 300, y = 250)


win6.mainloop () 
 
