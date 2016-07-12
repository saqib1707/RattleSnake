import json
import coaching_temp
import os

class Administrator:
	def __init__(self):
		#print "In init of administrator"
		print ""

	def uploadMarks(self):
		#print "In upload of administrator"
		listObj=[]
		with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as readFile:
			jsonFile=json.load(readFile)
			readFile.close()
		with open('C:\Users\Saqib\Desktop\Snake\Records.txt','w') as writeFile:
			for i in range(len(jsonFile)):
				jsonFile[i]['stu_marks']=raw_input("Enter marks for %s :"%jsonFile[i]['stu_name'])
				datadict={'stu_name':jsonFile[i]['stu_name'],'stu_phoneno':jsonFile[i]['stu_phoneno'],'stu_marks':jsonFile[i]['stu_marks'],"stu_batch":jsonFile[i]['stu_batch'],"stu_username":jsonFile[i]['stu_username'],"stu_password":jsonFile[i]["stu_password"]}
				listObj.append(datadict)
			json.dump(listObj,writeFile)	
			writeFile.close()
		with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as readFile:
			jsonFile=json.load(readFile)
		open('C:\Users\Saqib\Desktop\Snake\Records.txt','w').write(json.dumps(jsonFile,indent=4))
		#jsonFile=json.load(open('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt'))	
		#open('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt','w').write(json.dumps(jsonFile,indent=4))
		#os.system('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt')


	def reMapping(self):
		count=0
		i=1
		listObj=[]
		print "In remapping of administrator"
		with open('C:\Users\Saqib\Desktop\Snake\Records.txt','r') as readFile:
			jsonFile=json.load(readFile)
			jsonFileSorted=sorted(jsonFile,key=lambda k:k['stu_marks'],reverse=True)
			for j in range(len(jsonFileSorted)):
				count+=1
				if count%4==0:
					i+=1
				jsonFileSorted[j]['stu_batch']=i
		open('C:\Users\Saqib\Desktop\Snake\Records.txt','w').write(json.dumps(jsonFileSorted,indent=4))
		#showing the shuffled data
		for i in range(len(jsonFileSorted)):
			datadict={'stu_name':jsonFileSorted[i]['stu_name'],'stu_marks':jsonFileSorted[i]['stu_marks'],"stu_batch_alloted":jsonFileSorted[i]['stu_batch']}
			listObj.append(datadict)
		json.dump(listObj,open('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt','w'))
		jsonFileSorted=json.load(open('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt'))
		open('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt','w').write(json.dumps(jsonFileSorted,indent=4))
		os.system('C:\Users\Saqib\Desktop\Snake\MarkSheet.txt')



def AdmInterface(choice):
	AdmObj=Administrator()
	if choice==2:
		#upload marks for all the students
		AdmObj.uploadMarks()
	elif choice==3:
		AdmObj.reMapping()
	else:
		print "Wrong Input"
