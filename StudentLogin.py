import json
import getpass
"""
from Tkinter import *

top=Tk()
def login():
	username=Entry(top,cursor="arrow",text="User Name",fg="blue")
	username.pack()
	pwd=Entry(top,text="Password",fg="blue",show="*")
	pwd.pack()
	top.mainloop()

	
def signUp():
	username=Entry(top,cursor="arrow",text="User Name",fg="blue")
	username.pack()
	pwd=Entry(top,text="Password",fg="blue",show="*")
	pwd.pack()
	confirmpwd=Entry(top,text="Confirm Password",cursor="arrow",fg="blue")
	confirmpwd.pack()
	top.mainloop()
"""

def login():
	found=False
	username=raw_input("User Name >>>")
	pwd=getpass.getpass("Password >>>")
	with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as readFile:
		jsonData=json.load(readFile)
		if jsonData==[]:
			print "Student database empty"
			return
        for i in range(len(jsonData)):
        	if jsonData[i]['stu_username']==username and jsonData[i]['stu_password']==pwd:
        		#show his username,marks ,rank and current batch
        		found=True
        		print jsonData[i]['stu_name'],"\nMarks:",jsonData[i]['stu_marks'],"\tBatch:",jsonData[i]['stu_batch']
        if found==False:
        	print "\nNot registered or not admitted yet\n"

#for the first time users.
def signUp():
	found=False
	name=raw_input("Name >>>")
	phoneno=raw_input("Phone No >>>")
	with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as readFile:
		jsonData=json.load(readFile)
	for i in range(len(jsonData)):
		if jsonData[i]['stu_name']==name and jsonData[i]['stu_phoneno']==phoneno:
			found=True
			username=raw_input("UserName >>>")
			pwd=getpass.getpass("Password >>>")
			confirmpwd=getpass.getpass("Confirm Password >>>")
			if pwd!=confirmpwd:
				print "Password don't match!!!"
			else:
				#Register the student username and password
				print "Registration complete"
				jsonData[i]['stu_username']=username
				jsonData[i]['stu_password']=pwd
				open('C:\Users\Saqib\Desktop\Snake\Records.txt','w').write(json.dumps(jsonData,indent=4))
			break
	if found==False:
		print "Not admitted yet or data filled incorrectly"
	



	

