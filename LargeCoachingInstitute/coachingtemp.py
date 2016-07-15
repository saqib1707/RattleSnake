import json
import os
max_batchstrength=3
noofbatches=4

class RattleSnake:
    def __init__(self):
        self.nametoadd=""
        self.phone_no=""
        self.marks=0
        self.batch=None
        self.username=""
        self.password=""

    def checkFileEmpty(self):
        if os.stat("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt").st_size == 0:
            print "Empty File!!!Please add members to perform these operations"
            return True
        else:
            return False
        
    def addStudent(self):
        listobj=[]
        count=0
        string=""
        myModifiedList=""
        #noofStudents=input("How many students data u want to add ?? >>> ")
        #for i in range(noofStudents):
        self.nametoadd=raw_input("\nEnter student name to be added >>> ")
        self.phone_no=raw_input("Enter phone no:")
        with open("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt") as readStudentFile:
            if self.checkFileEmpty()==False:
                jsonData=json.load(readStudentFile)
                if len(jsonData) in range(1,4):
                    self.batch=1
                elif len(jsonData) in range(4,8):
                    self.batch=2
                elif len(jsonData) in range(8,12):
                    self.batch=3
                elif len(jsonData) in range(11,15):
                    self.batch=4
            else:
                self.batch=1

        data= {"name":self.nametoadd,"phoneno":self.phone_no,"marks":self.marks,"batch":self.batch,"username":self.username,"password":self.password}
        listobj.append(data)
        
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','a') as appendStudentFile:
            json.dump(listobj,appendStudentFile)
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
            textdata=readStudentFile.read()
            for char in textdata:
                if count==1:
                    string+=char
                    if string=="][":
                        count=2
                        char=','
                if char==']':
                    count+=1
                    string+=char
                else:
                    myModifiedList+=char
                if count==2:
                    continue
            if count==1 or count==3:
                myModifiedList+=']'
        
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w') as file:
            file.write(myModifiedList)
        jsonData=json.load(open("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt"))
        open("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt",'w').write(json.dumps(jsonData,indent=4))

    def removeStudent(self):
        if self.checkFileEmpty()==True:
            return
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as readStudentFile:
            jsonData1=json.load(readStudentFile)
            nooftimes=input("How many student data u want to delete >>> ")
            for i in range(nooftimes):
                found=False
                #jsonfile=json.load(open("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt"))
                if jsonData1==[]:
                    print "Student Database already empty!!!No more members to delete"
                    break
                self.nameToRemove=raw_input("Enter student name to be removed from Database >>> ")
                for i in range(len(jsonData1)):
                    if jsonData1[i]["name"]==self.nameToRemove :
                        jsonData1.pop(i)
                        print "%s deleted from Database "%self.nameToRemove
                        found=True
                        break
                if found==False:
                    print "\n%s not in the DataBase\n" %self.nameToRemove
                open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt','w').write(json.dumps(jsonData1,indent=4))


    def showListOfStudents(self):
        listObj=[]
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as infile:
            if self.checkFileEmpty()==False:
                data=json.load(infile)
                for i in range(len(data)):
                    dictionary={"name":data[i]['name'],"phoneno":data[i]['phoneno'],"marks":data[i]['marks'],"batch":data[i]['batch']}
                    listObj.append(dictionary)
                with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\Info.txt','w') as readFile:
                    json.dump(listObj,readFile,indent=4)
                os.system('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\Info.txt')     
        infile.close()

    def modifyData(self):
        with open('C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt') as infile:
            if self.checkFileEmpty()==False:
                jsonData=json.load(infile)
                self.dataToModify=raw_input("Enter student name whose data has to be modified >>> ")
                modification=True
                for i in range(len(jsonData)):
                    if jsonData[i]["name"]==self.dataToModify :
                        print "Press 1 to modify Student Name"
                        print "Press 2 to modify Student phone_no"
                        modify_choice=input("Enter ur choice >>> ")
                        if modify_choice==1:
                            jsonData[i]["name"]=raw_input("Enter Modified Name:")
                            
                        elif modify_choice==2:
                            jsonData[i]["phone"]=raw_input("Enter Modified Phone no:")
                           
                        else:
                            print "Wrong choice"
                            modification=False

                        if modification==True:
                            print "Data Modified for %s"%self.dataToModify 
                        open("C:\Users\Saqib\Desktop\Snake\LargeCoachingInstitute\StudentRecords.txt",'w').write(json.dumps(jsonData,indent=4))
        infile.close()

    

# Interface to access data of coaching students
def accessStuData():
    while(True):
        print "Press 1 to Add Students to the Database"
        print "Press 2 to Remove students from the Database"
        print "Press 3 to Print all the students in the Database"
        print "Press 4 to modify the basic info of students"
        print "Press any other key to go back to the previous menu"
            
        obj=RattleSnake()
        inputchoice=input("Enter ur choice >>> ")

        if inputchoice==1:
            obj.addStudent()
                    
        elif inputchoice==2:
            obj.removeStudent()

        elif inputchoice==3:
            obj.showListOfStudents()

        elif inputchoice==4:
            obj.modifyData()

        else:
            break
    return
    