import coaching_temp
import Error
from StudentLogin import *
import administrator


print "1. Administrator"
print "2. Student"
choiceone=input("Press 1 or 2 >>> ")
	
while(True):
	#Administrator access
	if choiceone==1:
		print "Press 1 to Access the Coaching Students Database"	
		print "Press 2 to Upload the New MarkSheet of the latest Test"
		print "Press 3 to shuffle the Students based on their marks"
		print "Press 0 to exit\n"
		choicefour=input(">>>")
		if choicefour==1:
			#call add student wala function
			coaching_temp.accessStuData()
		elif choicefour==2 or choicefour==3:
			#call admin wala function
			administrator.AdmInterface(choicefour)
		elif choicefour==0:
			break
		else:
			Error.showError()
	#Student Access		
	elif choiceone==2:
		#call student wala function
		print "Press 1 to Login to view Results"
		print "Press 2 to Sign Up for the first time"
		print "Press 0 to exit"
		choicethree=input("Press 1 or 2 >>> ")
		if choicethree==1:
			login()
		elif choicethree==2:
			signUp()
		elif choicethree==0:
			break
		else:
			Error.showError()

	else:
		Error.showError()