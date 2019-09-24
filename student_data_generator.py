## Author:     Ronan Wallace
## Project:    Algorithm Analysis Project
## Component:  Student Data Generator
## File Name:  student_data_generator.py

import random


# WORKS: DO NOT TOUCH #
def generateStudentData(numberOfStudents):
    # Data Format = [ [FIRST NAME, LAST NAME, SID, YEAR (FR,SO,JU,SE), MAJOR, GPA] , ['Ronan','Wallace',101083917,FR,COMP,3.6] ]
    firstNames = []
    middleInit = ['A.','B.','C.','D.','E.','F.','G.','H.','I.','J.','K.','L.','M.','N.','O.','P.','Q.','R.','S.','T.','U.','V.','W.','X.','Y.','Z.']
    lastNames = []
    year = ['Freshman','Sophomore','Junior','Senior']
    majors = []

    # Populates lists with names and majors; used to generate random students
    appendFirstNames(firstNames)
    appendLastNames(lastNames)
    appendMajors(majors)

    # Creates a file containing __(number)__ randomly generated students 
    studentData = open("student_data/student_data.txt","w")
    for i in range(numberOfStudents):
        studentData.write(getRandFirstN(firstNames)+','+getRandMiddleI(middleInit)+','+getRandLastN(lastNames)+','+generateSID()+','+generateYear(year)+','+generateMajor(majors)+','+generateGPA()+'\n')
    

# WORKS: DO NOT TOUCH #
def sampleStudent(firstNames,middleInit,lastNames,year,majors):
    print("NAME:",getRandFirstN(firstNames),getRandMiddleI(middleInit),getRandLastN(lastNames))
    print("SID:",generateSID())
    print("YEAR:",generateYear(year))
    print("MAJOR:",generateMajor(majors))
    print("GPA:",generateGPA())

# WORKS: DO NOT TOUCH #
def appendFirstNames(firstNames):
    femaleFirst = open("student_building_pieces/firstFemaleNames.txt","r")
    for i in femaleFirst:
        firstNames.append(i.rstrip())
    maleFirst = open("student_building_pieces/firstMaleNames.txt","r")
    for i in maleFirst:
        firstNames.append(i.rstrip())

# WORKS: DO NOT TOUCH #
def appendLastNames(lastNames):
    surnames = open("student_building_pieces/lastNames.txt","r")
    for i in surnames:
        lastNames.append(i.rstrip())

# WORKS: DO NOT TOUCH #
def getRandFirstN(firstNames):
    index = random.randint(0,99)
    name = firstNames[index]
    return name

# WORKS: DO NOT TOUCH #
def getRandMiddleI(middleInit):
    index = random.randint(0,25)
    name = middleInit[index]
    return name

# WORKS: DO NOT TOUCH #
def getRandLastN(lastNames):
    index = random.randint(0,99)
    name = lastNames[index]
    return name

# WORKS: DO NOT TOUCH #
def generateSID():
    studentID = "1010"+str(random.randint(10000,99999))
    return studentID

# WORKS: DO NOT TOUCH #
def generateYear(year):
    return year[random.randint(0,3)]

# WORKS: DO NOT TOUCH #
def appendMajors(majors):
    studies = open("student_building_pieces/majors.txt","r")
    for i in studies:
        majors.append(i.rstrip())

# WORKS: DO NOT TOUCH #
def generateMajor(majors):
    return majors[random.randint(0,37)]

# WORKS: DO NOT TOUCH #
def generateGPA():
    return str(round(2+2*random.random(),2))

# WORKS: DO NOT TOUCH #
def parseStudentData():
    return [line.strip().split(",") for line in open("student_data/student_data.txt","r")]

