import json
import sys
import fileinput
listobj=[]

class RattleSnake:
    def __init__(self):
        self.nametoadd=""
        self.phone_no=""
        self.marks1=0
        self.marks2=0
        self.marks3=0
        
    def addStudent(self):
        count=0
        string=""
        myModifiedList=""
        nooftimes=input("How many students data u want to add:---")
        for i in range(nooftimes):
            self.nametoadd=raw_input("\nEnter student name to be added:")
            self.phone_no=raw_input("Enter phone no:")
            self.marks1=input("Enter marks1:")
            self.marks2=input("Enter marks2:")
            self.marks3=input("Enter marks3:")
            data= {"stu_name":obj.nametoadd,"stu_phoneno":obj.phone_no,"stu_marks1":obj.marks1,"stu_marks2":obj.marks2,"stu_marks3":obj.marks3}
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


    def removeStudent(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            data=json.load(infile)
            if data==[]:
                print "Students Database Empty"
                return
        nooftimes=input("How many students data u want to delete:---")
        for i in range(nooftimes):
            found=False
            jsonfile=json.load(open("C:\Users\Saqib\Desktop\Snake\Records.txt"))
            if jsonfile==[]:
                print "Students Database already empty\nNo more members to delete"
                break
            self.nameToRemove=raw_input("Enter student name to be removed from database:")
            for i in range(len(jsonfile)):
                if jsonfile[i]["stu_name"]==obj.nameToRemove :
                    jsonfile.pop(i)
                    print "%s deleted from database "%obj.nameToRemove
                    found=True
                    break
            if found==False:
                print "\n%s not in the list\n" %obj.nameToRemove
            open("Records.txt",'w').write(json.dumps(jsonfile,indent=4,))


    def printListOfStudents(self):
        with open('C:\Users\Saqib\Desktop\Snake\Records.txt') as infile:
            data=json.load(infile)
            if data==[]:
                print "Students Database Empty"
            else:
                print "\n",data

while(True):
    print "Press 1 to Add students"
    print "Press 2 to Remove students"
    print "Press 3 to Print all the students in the list"
    print "Press any other key to quit"
    print "\n"
    
    obj=RattleSnake()
    inputchoice=input("Enter ur choice:")

    if inputchoice==1:
        obj.addStudent()
            
    elif inputchoice==2:
        obj.removeStudent()

    elif inputchoice==3:
        obj.printListOfStudents()

    else:
        break
    print "\n\n"
