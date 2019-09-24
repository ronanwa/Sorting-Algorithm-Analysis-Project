## Author:     Ronan Wallace
## Project:    Algorithm Analysis Project
## Component:  Sorting Functions
## File Name:  sorting_library.py

from student_data_generator import *
import time

###############################################################################################################################
# TIME ANALYSIS #
# WORKS: DO NOT TOUCH #
# Get time analysis of each singular sort (very simple and short, mostly for testing) #
def getTimeAnalysis(numberOfStudents,ans):
    timeRecord = []
    for i in range(10):
        generateStudentData(numberOfStudents)
        studentData = parseStudentData()
        # Bubble Sort Analysis #
        if ans == 1:
            timeRecord.append(bubbleTimeAnalysis(studentData))
        # Selection Sort Analysis #
        elif ans == 2:
            timeRecord.append(selectionTimeAnalysis(studentData))
        # Quick Sort Analysis #    
        elif ans == 3:
            timeRecord.append(quickTimeAnalysis(studentData))
        # Else, Error #
        else:
            print("Error")
    mean = 0
    for i in range(len(timeRecord)):
        mean += timeRecord[i]
    # Average Sorting Time 10 Times Over #
    return mean/len(timeRecord)


# AUTOMATED ANALYSIS FOR ALL THREE SORTS: Allows user to control number of students and number of repeated sorts to calculate a more accurate average #
# WORKS: DO NOT TOUCH #
def getTimeAnalysisAutomated(numberOfStudents,reps):
    algorithms = ["Bubble","Selection","Quick"]
    # Loop for the number of algorithms being analyzed (3)
    for i in range(len(algorithms)):
        listOfMeans = []
        alg = algorithms[i]
        # Loops for the number of student bodies to be tested (depends on user input)
        for j in range(len(numberOfStudents)):
            timeRecord = []
            # Number of sorts to be performed (more reps, higher accuracy)
            for k in range(reps):
                # Generate new student body each time to get a more accurate and realistic time (increases randomization and uniqueness to encounter serveral varaitions of student bodies)
                generateStudentData(numberOfStudents[j])
                studentData = parseStudentData()
                # Bubble Sort Analysis #
                if alg == "Bubble":
                    timeRecord.append(bubbleTimeAnalysis(studentData))
                # Selection Sort Analysis #
                elif alg == "Selection":
                    timeRecord.append(selectionTimeAnalysis(studentData))
                # Quick Sort Analysis #    
                elif alg == "Quick":
                    timeRecord.append(quickTimeAnalysis(studentData))
                # Else, Error #
                else:
                    print("Error")
            # Calculates means and appends to list for displaying
            mean = 0
            for l in range(len(timeRecord)):
                mean += timeRecord[l]
            listOfMeans.append([numberOfStudents[j],mean/len(timeRecord)])
        # Average Sorting Time at "reps" times #
        print("-"*40)
        print(alg,"Sort:")
        for m in range(len(numberOfStudents)):
            print("Number of Students:",listOfMeans[m][0])
            print("Number of Repetitions:",reps)
            print("Average Runtime:",listOfMeans[m][1],"\n")
    

###############################################################################################################################
# BUBBLE SORT #
# WORKS: DO NOT TOUCH #
def bubbleSort(studentData):
    # Sorting by last name, then first, then middle initial
    for i in range(len(studentData)):
        for j in range(0,len(studentData)-i-1):
            # If last names are the same, perform these steps to make a comparison and switch if necessary #
            if studentData[j][2] == studentData[j+1][2]:
                # If first names are the same, perform these steps #
                if studentData[j][0] == studentData[j+1][0]:
                    # If middle initial is not the same, compare weight and switch #
                    if studentData[j][1] > studentData[j+1][1]:
                        temp = studentData[j]
                        studentData[j] = studentData[j+1]
                        studentData[j+1] = temp
                    # Elif middle initial is the same, do nothing #
                    elif studentData[j][1] == studentData[j+1][1]:
                        continue
                    elif studentData[j][1] < studentData[j+1][1]:
                        continue
                    # Else, error #
                    else:
                        print("Error 1")
                # Elif first name exists inside the other, perform the switch based on length weight #
                elif studentData[j+1][0] in studentData[j][0]:
                    temp = studentData[j]
                    studentData[j] = studentData[j+1]
                    studentData[j+1] = temp
                # Elif first names are NOT the same, perform these steps #
                elif studentData[j][0] != studentData[j+1][0]:
                    x = 1
                    y = -1
                    while x == 1:
                        y+=1
                        try:
                            if studentData[j][0][y] > studentData[j+1][0][y]:
                                temp = studentData[j]
                                studentData[j] = studentData[j+1]
                                studentData[j+1] = temp
                                x = 0
                            # If the letters are the same, continue to next letter #
                            elif studentData[j][0][y] == studentData[j+1][0][y]:
                                continue
                            # If the letter is weighted less than the other, move on to the next student #
                            elif studentData[j][0][y] < studentData[j+1][0][y]:
                                x = 0
                        except:
                            x = 0
                # Else, error #
                else:
                    print("Error 2")
                    break
            # If last names are NOT the same, perform these steps to make a comparison and switch if necesarry #
            elif studentData[j][2] != studentData[j+1][2]:
                # If last name exists inside the other, perform this switch (know the weight) #
                if studentData[j+1][2] in studentData[j][2]:
                    temp = studentData[j]
                    studentData[j] = studentData[j+1]
                    studentData[j+1] = temp
                # Elif last names does NOT exist inside the other, compare all letters until a letter has greater weight (possible while loop) #
                elif studentData[j+1][2] not in studentData[j][2]:
                    x = 1
                    y = -1
                    # Loop for letter comparison #
                    while x == 1:
                        y+=1
                        try:
                            # If letter is weighted greater than other, switch #
                            if studentData[j][2][y] > studentData[j+1][2][y]:
                                temp = studentData[j]
                                studentData[j] = studentData[j+1]
                                studentData[j+1] = temp
                                x = 0
                            # If the letters are the same, continue to next letter #
                            elif studentData[j][2][y] == studentData[j+1][2][y]:
                                continue
                            # If the letter is weighted less than the other, move on to the next student #
                            elif studentData[j][2][y] < studentData[j+1][2][y]:
                                x = 0
                        except:
                            x = 0
                # Else, error #
                else:
                    print("Error 3")
                    break
            # Else, there's an error happening #
            else:
                print("Error 4")
                break
    return studentData

# WORKS: DO NOT TOUCH #
# Testing function to see if sorted (best when 9 < n < 51) #
def compareBubbleData(numberOfStudents):
    generateStudentData(numberOfStudents)
    studentData = parseStudentData()
    temp1 = []
    for i in range(len(studentData)):
        temp1.append(studentData[i][0]+" "+studentData[i][1]+" "+studentData[i][2])
    bubbleData = bubbleSort(studentData)
    temp2 = []
    for i in range(len(bubbleData)):
        temp2.append(bubbleData[i][0]+" "+bubbleData[i][1]+" "+bubbleData[i][2])
    print("\n",temp1)
    print("\n",temp2)

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time #
def bubbleTime(studentData):
    print("\nBeginning Bubble Sort on Student Data...")
    start1 = time.time()
    bubbleSort(studentData)
    end1 = time.time()
    print("Bubble Sort Complete.\n")
    return end1-start1

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time; used for automated time analysis #
def bubbleTimeAnalysis(studentData):
    start1 = time.time()
    bubbleSort(studentData)
    end1 = time.time()
    return end1-start1

###############################################################################################################################
# SELECTION SORT #
# WORKS: DO NOT TOUCH #
def selectionSort(studentData):
    for i in range(len(studentData)):
        minIndex = i
        for j in range(i+1,len(studentData)):
            # If last names are the same, perform these steps to find min names #
            if studentData[minIndex][2] == studentData[j][2]:
                # If first names are the same, perform these steps to find min names #
                if studentData[minIndex][0] == studentData[j][0]:
                    # If middle initial is not the same and is more than right adjacent, grab min index of right adjacent #
                    if studentData[minIndex][1] > studentData[j][1]:
                        minIndex = j
                    # Elif middle initial is the same, do nothing #
                    elif studentData[minIndex][1] == studentData[j][1]:
                        continue
                    # Elif middle init is less than right adjacent, do nothing? (because the min is already assigned?) #
                    elif studentData[minIndex][1] < studentData[j][1]:
                        continue
                    # Else, error #
                    else:
                        print("Error 1") 
                # Elif first name exists inside the other, grab index of shorter name #
                elif studentData[j][0] in studentData[minIndex][0]:
                    minIndex = j
                # Elif first names are NOT the same, perform these steps #
                elif studentData[minIndex][0] != studentData[j][0]:
                    x = 1
                    y = -1
                    while x == 1:
                        y+=1
                        try:
                            if studentData[minIndex][0][y] > studentData[j][0][y]:
                                minIndex = j
                                x = 0
                            # If the letters are the same, continue to next letter #
                            elif studentData[minIndex][0][y] == studentData[j][0][y]:
                                continue
                            # If the letter is weighted less than the other, move on to the next student (keep current index) #
                            elif studentData[minIndex][0][y] < studentData[j][0][y]:
                                x = 0
                        except:
                            x = 0
                # Else, error #
                else:
                    print("Error 2")
                    break
            # If last names are NOT the same, perform these steps to make a comparison and switch if necesarry #
            elif studentData[minIndex][2] != studentData[j][2]:
                # If last name exists inside the other, perform this switch (know the weight) #
                if studentData[j][2] in studentData[minIndex][2]:
                    minIndex = j
                # Elif last names does NOT exist inside the other, compare all letters until a letter has greater weight (possible while loop) #
                elif studentData[j][2] not in studentData[minIndex][2]:
                    x = 1
                    y = -1
                    # Loop for letter comparison #
                    while x == 1:
                        y+=1
                        try:
                            # If letter is weighted greater than other, switch #
                            if studentData[minIndex][2][y] > studentData[j][2][y]:
                                minIndex = j
                                x = 0
                            # If the letters are the same, continue to next letter #
                            elif studentData[minIndex][2][y] == studentData[j][2][y]:
                                continue
                            # If the letter is weighted less than the other, move on to the next student #
                            elif studentData[minIndex][2][y] < studentData[j][2][y]:
                                x = 0
                        except:
                            x = 0
                # Else, error #
                else:
                    print("Error 3")
                    break
            # Else, there's an error happening #
            else:
                print("Error 4")
                break
        studentData[i], studentData[minIndex] = studentData[minIndex], studentData[i]
    return studentData

# WORKS: DO NOT TOUCH #
# Testing function to see if sorted (best when 9 < n < 51) #
def compareSelectionData(numberOfStudents):
    generateStudentData(numberOfStudents)
    studentData = parseStudentData()
    temp1 = []
    for i in range(len(studentData)):
        temp1.append(studentData[i][0]+" "+studentData[i][1]+" "+studentData[i][2])
    selectionData = selectionSort(studentData)
    temp2 = []
    for i in range(len(selectionData)):
        temp2.append(selectionData[i][0]+" "+selectionData[i][1]+" "+selectionData[i][2])
    print("\n",temp1)
    print("\n",temp2)

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time #
def selectionTime(studentData):
    print("\nBeginning Selection Sort on Student Data...")
    start1 = time.time()
    selectionSort(studentData)
    end1 = time.time()
    print("Selection Sort Complete.\n")
    return end1-start1

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time; used for automated time analysis #
def selectionTimeAnalysis(studentData):
    start1 = time.time()
    selectionSort(studentData)
    end1 = time.time()
    return end1-start1

###############################################################################################################################
# QUICK SORT #
# WORKS: DO NOT TOUCH #
def getQuickSortData(studentData,low,high):
    quickSort(studentData,low,high)
    return studentData

# WORKS: DO NOT TOUCH #
def quickSort(studentData,low,high):
    if low < high:
        # Partition Index
        pI = partition(studentData,low,high)
        #Sorts elements before partition and after partition
        quickSort(studentData,low,pI-1)
        quickSort(studentData,pI+1,high)

# WORKS: DO NOT TOUCH #
def partition(studentData,low,high):
    i = low-1
    pivot = studentData[high]
    for j in range(low,high):
        # If last names are the same, perform these steps to find min names #
        if pivot[2] == studentData[j][2]:
            # If first names are the same, perform these steps to find min names #
            if pivot[0] == studentData[j][0]:
                # If middle initial is not the same and is more than right adjacent, grab min index of right adjacent #
                if pivot[1] > studentData[j][1]:
                    i+=1
                    studentData[i], studentData[j] = studentData[j], studentData[i]
                # Elif middle initial is the same, do nothing #
                elif pivot[1] == studentData[j][1]:
                    continue
                # Elif middle init is less than right adjacent, do nothing? (because the min is already assigned?) #
                elif pivot[1] < studentData[j][1]:
                    continue
                # Else, error #
                else:
                    print("Error 1") 
            # Elif first name exists inside the other, grab index of shorter name #
            elif studentData[j][0] in pivot[0]:
                i+=1
                studentData[i], studentData[j] = studentData[j], studentData[i]
            # Elif first names are NOT the same, perform these steps #
            elif pivot[0] != studentData[j][0]:
                x = 1
                y = -1
                while x == 1:
                    y+=1
                    try:
                        if pivot[0][y] > studentData[j][0][y]:
                            i+=1
                            studentData[i], studentData[j] = studentData[j], studentData[i]
                            x = 0
                        # If the letters are the same, continue to next letter #
                        elif pivot[0][y] == studentData[j][0][y]:
                            continue
                        # If the letter is weighted less than the other, move on to the next student (keep current index) #
                        elif pivot[0][y] < studentData[j][0][y]:
                            x = 0
                    except:
                        x = 0
            # Else, error #
            else:
                print("Error 2")
                break
        # If last names are NOT the same, perform these steps to make a comparison and switch if necesarry #
        elif pivot[2] != studentData[j][2]:
            # If last name exists inside the other, perform this switch (know the weight) #
            if studentData[j][2] in pivot[2]:
                i+=1
                studentData[i], studentData[j] = studentData[j], studentData[i]
            # Elif last names does NOT exist inside the other, compare all letters until a letter has greater weight (possible while loop) #
            elif studentData[j][2] not in pivot[2]:
                x = 1
                y = -1
                # Loop for letter comparison #
                while x == 1:
                    y+=1
                    try:
                        # If letter is weighted greater than other, switch #
                        if pivot[2][y] > studentData[j][2][y]:
                            i+=1
                            studentData[i], studentData[j] = studentData[j], studentData[i]
                            x = 0
                        # If the letters are the same, continue to next letter #
                        elif pivot[2][y] == studentData[j][2][y]:
                            continue
                        # If the letter is weighted less than the other, move on to the next student #
                        elif pivot[2][y] < studentData[j][2][y]:
                            x = 0
                    except:
                        x = 0
            # Else, error #
            else:
                print("Error 3")
                break
        # Else, there's an error happening #
        else:
            print("Error 4")
            break
    studentData[i+1], studentData[high] = studentData[high], studentData[i+1] 
    return (i+1)

# WORKS: DO NOT TOUCH #
# Testing function to see if sorted (best when 9 < n < 51) #
def compareQuickData(numberOfStudents):
    generateStudentData(numberOfStudents)
    studentData = parseStudentData()
    temp1 = []
    for i in range(len(studentData)):
        temp1.append(studentData[i][0]+" "+studentData[i][1]+" "+studentData[i][2])
    quickData = getQuickSortData(studentData,0,len(studentData)-1)
    temp2 = []
    for i in range(len(quickData)):
        temp2.append(quickData[i][0]+" "+quickData[i][1]+" "+quickData[i][2])
    print("\n",temp1)
    print("\n",temp2)

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time #
def quickTime(studentData):
    print("\nBeginning Quick Sort on Student Data...")
    start1 = time.time()
    quickData = getQuickSortData(studentData,0,len(studentData)-1)
    end1 = time.time()
    print("Quick Sort Complete.\n")
    return end1-start1

# WORKS: DO NOT TOUCH #
# Performs sort and keeps time; used for automated time analysis #
def quickTimeAnalysis(studentData):
    start1 = time.time()
    quickData = getQuickSortData(studentData,0,len(studentData)-1)
    end1 = time.time()
    return end1-start1
