import json
import coachingtemp
import os
import Error

class Administrator:
	def __init__(self):
		#print "In init of administrator"
		print

	def startNewTest(self):
		flag=True
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt','r') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
				if jsonData[i]['is_Marks_Updated']=="None":
					flag=False
					jsonData[i]['is_Marks_Updated']="False"
			if flag==False:
				print "New Test could not be started now.Reminders to teachers who have not submitted marksheet"
				return
		print "Start a new Test"
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
					jsonData[i]['is_Marks_Updated']="None"
			open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt','w').write(json.dumps(jsonData,indent=4))

	def reMapping(self):
		count=0
		listObj=[]
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt','r') as readTeacherFile:
			jsonData=json.load(readTeacherFile)
			for i in range(len(jsonData)):
				if jsonData[i]['is_Marks_Updated']!="True":
					print "All students marks has not be uploaded!! ReMapping could not be done now"
					return
		print "ReMapping of students"
		i=1
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','r') as readStudentFile:
			jsonData=json.load(readStudentFile)
			jsonDataSorted=sorted(jsonData,key=lambda k:k['marks'],reverse=True)
			for j in range(len(jsonDataSorted)):
				count+=1
				if count%5==0:
					i+=1
					count+=1
				jsonDataSorted[j]['batch']=i
		open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w').write(json.dumps(jsonDataSorted,indent=4))
		#showing the shuffled data
		for i in range(len(jsonDataSorted)):
			datadict={'name':jsonDataSorted[i]['name'],'marks':jsonDataSorted[i]['marks'],"batch":jsonDataSorted[i]['batch']}
			listObj.append(datadict)
		json.dump(listObj,open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\MarkSheet.txt','w'))
		jsonDataSorted=json.load(open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\MarkSheet.txt'))
		open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\MarkSheet.txt','w').write(json.dumps(jsonDataSorted,indent=4))
		os.system('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\MarkSheet.txt')


def AdmInterface(choice):
	AdmObj=Administrator()
	if choice==2:
		AdmObj.startNewTest()    #upload marks for all the students
	elif choice==3:
		AdmObj.reMapping()       #Shuffle students and allot them batches

while(True):
	print "Press 1 to Access the Coaching Students Database"	
	print "Press 2 to start a new test(give reminders to teachers)"
	print "Press 3 for Batch Allotment"
	print "Press 0 to exit"
	choicefour=input(">>>")
	if choicefour==1:
		coachingtemp.accessStuData()
	elif choicefour==2 or choicefour==3:
		AdmInterface(choicefour)
	elif choicefour==0:
		break
	else:
		Error.showError()

