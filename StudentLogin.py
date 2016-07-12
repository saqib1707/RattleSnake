import json
import getpass

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
        		print "\n",jsonData[i]['stu_name'],"\nMarks:",jsonData[i]['stu_marks'],"\tBatch:",jsonData[i]['stu_batch'],"\n"
        if found==False:
        	print "\nNot registered or not admitted yet!!!If Registered ,then Sign Up!!!\n"

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
				print "\nRegistration complete\n"
				jsonData[i]['stu_username']=username
				jsonData[i]['stu_password']=pwd
				open('C:\Users\Saqib\Desktop\Snake\Records.txt','w').write(json.dumps(jsonData,indent=4))
			break
	if found==False:
		print "\nNot admitted yet or data filled incorrectly\n"
while(True):	
	print "Press 1 to Login to view Results"
	print "Press 2 to Sign Up for the first time"
	print "Press 0 to exit"
	choicethree=input(">>> ")
	if choicethree==1:
		login()
	elif choicethree==2:
		signUp()
	elif choicethree==0:
		break
	else:
		Error.showError()


	

