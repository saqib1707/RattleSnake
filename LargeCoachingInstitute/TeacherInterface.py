import json,Error,getpass

class TeacherInterface:
	def __init__(self):
		print

	def checkBatchEmpty(self,batch):
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
			jsonData2=json.load(readStudentFile)
			for i in range(len(jsonData2)):
				if jsonData2[i]['batch']==batch:
					return False
			print "Batch is empty"
			return True

        


	def showListOfStudents(self,batch):
		if self.checkBatchEmpty(batch)==True:
			return
		listOfStudent=[]
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
			jsonData2=json.load(readStudentFile)
			for i in range(len(jsonData2)):
				if jsonData2[i]['batch']==batch:
					#listOfStudent.append(jsonData2[i]['name'])
					print jsonData2[i]['name']," : ",jsonData2[i]['marks']
			

	def uploadMarks(self,batch):
		if self.checkBatchEmpty(batch)==True:
			return
		print "Upload of Student Marks of Last Test"
		print "Enter Marks for students"
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
			jsonData2=json.load(readStudentFile)
			for i in range(len(jsonData2)):
				if jsonData2[i]['batch']==batch:
					jsonData2[i]['marks']=input(jsonData2[i]['name'])
			open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w').write(json.dumps(jsonData2,indent=4))
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt') as readTeacherFile:
			jsonData1=json.load(readTeacherFile)
			for i in range(len(jsonData1)):
				if jsonData1[i]['batch']==batch:
					jsonData1[i]['is_Marks_Updated']="True"
			open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt','w').write(json.dumps(jsonData1,indent=4))


	def modifyMarks(self,batch):
		if self.checkBatchEmpty(batch)==True:
			return
		is_Modified=False
		print "Enter student name whose marks has to be modified"
		name=raw_input(">>>")
		with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
			jsonData2=json.load(readStudentFile)
			for i  in range(len(jsonData2)):
				if jsonData2[i]['name']==name and jsonData2[i]['batch']==batch:
					jsonData2[i]['marks']=input('Enter modified marks >>> ')
					is_Modified=True
					break
			if is_Modified==False:
				print "Modification Failure!!!Student not found"
			open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w').write(json.dumps(jsonData2,indent=4))


def main():
	batch=None
	username=raw_input("Username >>>")
	pwd=getpass.getpass("Password >>>")
	with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\TeacherRecords.txt') as readTeacherFile:
		jsonData1=json.load(readTeacherFile)
		for i in range(len(jsonData1)):
			if jsonData1[i]['username']==username and jsonData1[i]['password']==pwd :
				batch=jsonData1[i]['batch']
				print jsonData1[i]['name']," -Batch ",batch,"\n","Access Granted"
				if jsonData1[i]['is_Marks_Updated']=="False":
					print "Reminder to upload the latest test marks"
				break
		if batch==None:
			print "Access Denied"
			print "Username or password or both are incorrect!!!Please try again"
			return
	while True:
		print "1. See the list of students in ur batch"
		print "2. Upload marks of the Latest Test"
		print "3. Modify marks of individual student"
		print "4. Quit"
		choice=input(">>>")
		obj=TeacherInterface()
		if choice==1:
			obj.showListOfStudents(batch)

		elif choice==2:
			obj.uploadMarks(batch)

		elif choice==3:
			obj.modifyMarks(batch)

		elif choice==4:
			break

		else:
			Error.showError()

if __name__=="__main__":
	main()
