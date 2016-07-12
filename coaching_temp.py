import json
import os

class RattleSnake:
    def __init__(self):
        self.nametoadd=""
        self.phone_no=""
        self.marks=0
        self.batch=None
        self.username=""
        self.password=""

    def checkFileEmpty(self):
        if os.stat("C:\Users\Saqib\Desktop\Snake\Records.txt").st_size == 0:
            print "Empty File!!!Please add members to perform these operations"
            return True
        else:
            return False
        
    def addStudent(self):
        listobj=[]
        count=0
        string=""
        myModifiedList=""
        noofStudents=input("How many students data u want to add >>> ")
        for i in range(noofStudents):
            self.nametoadd=raw_input("\nEnter student name to be added >>> ")
            self.phone_no=raw_input("Enter phone no:")
            data= {"stu_name":self.nametoadd,"stu_phoneno":self.phone_no,"stu_marks":self.marks,"stu_batch":self.batch,"stu_username":self.username,"stu_password":self.password}
            listobj.append(data)

        with open('C:\Users\Saqib\Desktop\Snake\Records.txt','a') as file:
            json.dump(listobj,file)
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt','r') as file:
            textdata=file.read()
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
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt','w') as file:
            file.write(myModifiedList)
        jsonData=json.load(open("C:\Users\Saqib\Desktop\Snake\Records.txt"))
        open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonData,indent=4))


    def removeStudent(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            if self.checkFileEmpty()==False:
                jsonfile=json.load(infile)
                nooftimes=input("How many student data u want to delete >>> ")
                for i in range(nooftimes):
                    found=False
                    #jsonfile=json.load(open("C:\Users\Saqib\Desktop\Snake\Records.txt"))
                    if jsonfile==[]:
                        print "Student Database already empty!!!No more members to delete"
                        break
                    self.nameToRemove=raw_input("Enter student name to be removed from Database >>> ")
                    for i in range(len(jsonfile)):
                        if jsonfile[i]["stu_name"]==self.nameToRemove :
                            jsonfile.pop(i)
                            print "%s deleted from Database "%self.nameToRemove
                            found=True
                            break
                    if found==False:
                        print "\n%s not in the DataBase\n" %self.nameToRemove
                    open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonfile,indent=4))


    def printListOfStudents(self):
        listObj=[]
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            if self.checkFileEmpty()==False:
                data=json.load(infile)
                for i in range(len(data)):
                    dictionary={"stu_name":data[i]['stu_name'],"stu_phoneno":data[i]['stu_phoneno'],"stu_marks":data[i]['stu_marks'],"stu_batch":data[i]['stu_batch']}
                    listObj.append(dictionary)
                with open('C:\Users\Saqib\Desktop\Snake\Info.txt','w') as readFile:
                    json.dump(listObj,readFile,indent=4)
                os.system('C:\Users\Saqib\Desktop\Snake\Info.txt')     
        infile.close()

    def modifyData(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            if self.checkFileEmpty()==False:
                jsonData=json.load(infile)
                self.dataToModify=raw_input("Enter student name whose data has to be modified >>> ")
                modification=True
                for i in range(len(jsonData)):
                    if jsonData[i]["stu_name"]==self.dataToModify :
                        print "Press 1 to modify Student Name"
                        print "Press 2 to modify Student phone_no"
                        print "Press 3 to modify Student marks"
                        print "Press 4 to modify Student batch"
                        modify_choice=input("Enter ur choice >>> ")
                        if modify_choice==1:
                            jsonfile[i]["stu_name"]=raw_input("Enter Modified Name:")
                            
                        elif modify_choice==2:
                            jsonfile[i]["stu_phone"]=raw_input("Enter Modified Phone no:")
                           
                        elif modify_choice==3:
                            jsonfile[i]["stu_marks"]=raw_input("Enter Modified marks :")
                            
                        elif modify_choice==4:
                            jsonfile[i]["stu_batch"]=raw_input("Enter new batch:")
                           
                        else:
                            print "Wrong choice"
                            modification=False

                        if modification==True:
                            print "Data Modified for %s"%self.dataToModify 
                        open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonfile,indent=4))
        infile.close()

    

# Interface to access data of coaching students
def accessStuData():
    while(True):
        print "Press 1 to Add Students to the Database"
        print "Press 2 to Remove students from the Database"
        print "Press 3 to Print all the students in the Database"
        print "Press 4 to modify the data of students"
        print "Press any other key to go back to the previous menu"
            
        obj=RattleSnake()
        inputchoice=input("Enter ur choice >>> ")

        if inputchoice==1:
            obj.addStudent()
                    
        elif inputchoice==2:
            obj.removeStudent()

        elif inputchoice==3:
            obj.printListOfStudents()

        elif inputchoice==4:
            obj.modifyData()

        else:
            break
    return
    