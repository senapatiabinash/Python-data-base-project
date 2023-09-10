from tkinter import * 
import pymysql 
win3= Tk ()
win3.geometry('1000x600')
win3.maxsize (900, 500 )
win3.minsize (900, 500 )
win3.title ("Display Page")
win3.configure(bg='PaleGreen')
conobj = pymysql.connect (host ='localhost', user ='root', password ='', port = 3306) 
curobj = conobj .cursor () 
curobj .execute ('use MyClg;')
curobj.execute ('select Fname, Lname , Email, UserId , Gender , Branch from Info ;')
record = curobj.fetchall () 
i= 0
for student in record : 
	for j in range (len (student)) :
		#e= Entry (win3, width= 15, font= ("Elephant", 10))
		e= Label (win3, width= 12, text= student[j],font= ("Elephant", 10), borderwidth= 2, relief='ridge', anchor='w')
		e.grid (row=i , column= j)
		#e. insert (END, student[j])
	i+=1 

curobj.close ()
conobj.close () 

win3.mainloop ()
