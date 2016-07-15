import json
import getpass 
import os  

def checkFileEmpty():
        if os.stat("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt").st_size == 0:
            print "Empty File!!!Please add members to perform these operations"
            return True
        else:
            return False

def login():
	found=False
	if checkFileEmpty()==True:              #checks whether the file is empty or not
		return
	username=raw_input("User Name >>>")
	pwd=getpass.getpass("Password >>>")
	
	with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readFile:
		jsonData=json.load(readFile)
        for i in range(len(jsonData)):
        	if jsonData[i]['username']==username and jsonData[i]['password']==pwd:
        		#show his username,marks ,rank and current batch
        		found=True
        		print "\n",jsonData[i]['name'],"\nMarks:",jsonData[i]['marks'],"\tBatch:",jsonData[i]['batch'],"\n"
        if found==False:
        	print "\nNot registered or not admitted yet!!!If Registered ,then Sign Up!!!\n"
    

#for the first time users.
def signUp():
	found=False
	countOfTry=0
	if checkFileEmpty()==True:              #checks whether the file is empty or not
		return
	name=raw_input("Name >>>")
	phoneno=raw_input("Phone No >>>")
	
	with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
		jsonData=json.load(readStudentFile)
		for i in range(len(jsonData)):
			if jsonData[i]['name']==name and jsonData[i]['phoneno']==phoneno and jsonData[i]['username']=="" and jsonData[i]['password']=="":
				found=True
				username=raw_input("UserName >>>")
				pwd=getpass.getpass("Password >>>")
				confirmpwd=getpass.getpass("Confirm Password >>>")
				if pwd!=confirmpwd:
					print "Password don't match!!!Try Again(max. 3 times)"
					countOfTry+=1
					if countOfTry==2:
						break
				else:
					#Register the student username and password
					print "\nRegistration complete\n"
					jsonData[i]['username']=username
					jsonData[i]['password']=pwd
					open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w').write(json.dumps(jsonData,indent=4))
					
				break
		if found==False:
			print "\nNot admitted yet or data filled incorrectly or already registered\n"


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


	
