import json
import os
listobj=[]

class RattleSnake:
    def __init__(self):
        self.nametoadd=""
        self.phone_no=""
        self.marks=0
        
    def addStudent(self):
        listobj=[]
        count=0
        string=""
        myModifiedList=""
        noofStudents=input("How many students data u want to add:")
        for i in range(noofStudents):
            self.nametoadd=raw_input("\nEnter student name to be added:")
            self.phone_no=raw_input("Enter phone no:")
            self.marks=input("Enter marks:")
            data= {"stu_name":obj.nametoadd,"stu_phoneno":obj.phone_no,"stu_marks":obj.marks}
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
            file.close()
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt','w') as file:
            file.write(myModifiedList)
        jsonfile=json.load(open("C:\Users\Saqib\Desktop\Snake\Records.txt"))
        open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonfile,indent=4))


    def removeStudent(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            jsonfile=json.load(infile)
            if jsonfile==[]:
                print "Students Database Empty"
                infile.close()
                return
            nooftimes=input("How many student data u want to delete:")
            for i in range(nooftimes):
                found=False
                #jsonfile=json.load(open("C:\Users\Saqib\Desktop\Snake\Records.txt"))
                if jsonfile==[]:
                    print "Student Database already empty\nNo more members to delete"
                    break
                self.nameToRemove=raw_input("Enter student name to be removed from database:")
                for i in range(len(jsonfile)):
                    if jsonfile[i]["stu_name"]==obj.nameToRemove :
                        jsonfile.pop(i)
                        print "%s deleted from database "%obj.nameToRemove
                        found=True
                        break
                if found==False:
                    print "\n%s not in the DataBase\n" %obj.nameToRemove
                open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonfile,indent=4))


    def printListOfStudents(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            data=json.load(infile)
            if data==[]:
                print "Students Database Empty"
            else:
                print "\n",data
                os.system('C:\Users\Saqib\Desktop\Snake\Records.txt')
            infile.close()

    def modifyData(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            jsonfile=json.load(infile)
            if jsonfile==[]:
                print "Students Database Empty"
                infile.close()
                return
            self.dataToModify=raw_input("Enter student name whose data has to be modified:")
            modification=True
            for i in range(len(jsonfile)):
                if jsonfile[i]["stu_name"]==obj.dataToModify :
                    print "Press 1 to modify Student Name"
                    print "Press 2 to modify Student phone_no"
                    print "Press 3 to modify Student marks"
                    modify_choice=input("Enter ur choice:")
                    if modify_choice==1:
                        self.stu_name=raw_input("Enter Modified Name:")
                        jsonfile[i]["stu_name"]=self.stu_name
                    elif modify_choice==2:
                        self.stu_phoneno=raw_input("Enter Modified Phone no:")
                        jsonfile[i]["stu_phone"]=self.stu_phoneno
                    elif modify_choice==3:
                        self.stu_marks=raw_input("Enter Modified marks :")
                        jsonfile[i]["stu_marks"]=self.stu_marks
                    else:
                        print "Wrong choice"
                        modification=False

                    if modification==True:
                        print "Data Modified for student %s"%self.dataToModify 
            open("C:\Users\Saqib\Desktop\Snake\Records.txt",'w').write(json.dumps(jsonfile,indent=4,))


# Main Interface
while(True):
    print "Press 1 to Add students to the Database"
    print "Press 2 to Remove students from the Database"
    print "Press 3 to Print all the students in the Database"
    print "Press 4 to modify the data of students"
    print "Press any other key to quit"
    print "\n"
        
    obj=RattleSnake()
    inputchoice=raw_input("Enter ur choice:")

    if int(inputchoice)==1:
        obj.addStudent()
                
    elif int(inputchoice)==2:
        obj.removeStudent()

    elif int(inputchoice)==3:
        obj.printListOfStudents()

    elif int(inputchoice)==4:
        obj.modifyData()

    else:
        break
    print "\n"
#return
    
