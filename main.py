## Author:     Ronan Wallace
## Project:    Algorithm Analysis Project
## Component:  Main Function
## File Name:  main.py

from student_data_generator import *
from sorting_library import *
import time


def main():
    print("-"*51)
    print("---"," "*5,"Sorting Algorithm Time Analyzer"," "*5,"---")
    print("-"*51,"\n")
    print("Choose your path:\n")
    print("1: General Sorting")
    print("2: Time Analysis Testing\n")
    ans0 = eval(input("1 or 2? "))

    if ans0 == 1:
        numberOfStudents = eval(input("\nHow many students would you like to generate? "))
        #student_data = []
        print("\nBeginning random student body generation...")
        start = time.time()
        # Creates a .txt file of n students
        generateStudentData(numberOfStudents)
        print("Student body successfully generated.\n")
        print("Beginning student parse...")
        # Reads .txt file and defines assigns as a list to a variable
        studentData = parseStudentData()
        end = time.time()
        print("Parsing complete.")
        print("\n",len(studentData),"unsorted students have been randomly generated in",str(end-start),"seconds and are ready to be sorted.")
        print("-"*50)
        
        # Presents options to perform #
        # Performs the sort, returns the time it took #
        print("Sorts:")
        print("1: Bubble Sort")
        print("2: Selection Sort")
        print("3: Quick Sort")
        # compare original array with sorted array #
        print("\nTesting (Best when 9 < N < 51):")
        print("4: Bubble Sort Testing")
        print("5: Selection Sort Testing")
        print("6: Quick Sort Testing\n")
        
        ans = eval(input("Which sort would you like to use? "))
        # Sorts #
        if ans == 1:
            seconds = bubbleTime(studentData)
            print("Bubble sorted in",seconds,"seconds")
        elif ans == 2:
            seconds = selectionTime(studentData)
            print("Selection sorted in",seconds,"seconds")
        elif ans == 3:
            seconds = quickTime(studentData)
            print("Quick sorted in",seconds,"seconds")
        elif ans == 4:
            compareBubbleData(numberOfStudents)
        elif ans == 5:
            compareSelectionData(numberOfStudents)
        elif ans == 6:
            compareQuickData(numberOfStudents)
        else:
            print("Incorrect Input")
            
    elif ans0 == 2:
        # Mostly used for quick 10 rep. testing to make sure averages are being properly calculated #
        print("\nRuntime Analysis:")
        print("1: Bubble Sort Analysis")
        print("2: Selection Sort Analysis")
        print("3: Quick Sort Analysis")

        # The one that does the heavy lifting #
        print("\nAutomated Analysis:")
        print("4: Triple Sorting Algorithm Analysis\n")

        ans1 = eval(input("Which analysis would you like to use? "))

        # Bubble sort quick analysis #
        if ans1 == 1:
            numberOfStudents = eval(input("\nHow many students would you like to generate? "))
            average = getTimeAnalysis(numberOfStudents,ans1)
            print("\nBubble Sort Analysis:")
            print("Number of students sorted:",numberOfStudents)
            print("Number of times ran: 10")
            print("Average runtime (seconds):",average)
        # Selection sort quick analysis #
        elif ans1 == 2:
            numberOfStudents = eval(input("\nHow many students would you like to generate? "))
            average = getTimeAnalysis(numberOfStudents,ans1)
            print("\nSelection Sort Analysis:")
            print("Number of students sorted:",numberOfStudents)
            print("Number of times ran: 10")
            print("Average runtime (seconds):",average)
        # Quick sort quick analysis #
        elif ans1 == 3:
            numberOfStudents = eval(input("\nHow many students would you like to generate? "))
            average = getTimeAnalysis(numberOfStudents,ans1)
            print("\nQuick Sort Analysis:")
            print("Number of students sorted:",numberOfStudents)
            print("Number of times ran: 10")
            print("Average runtime (seconds):",average)
        # Automated Runtime Analysis #
        elif ans1 == 4:
            amounts = []
            x = 1
            while x == 1:
                amounts.append(eval(input("\nHow many students do you want to sort? ")))
                if input("More students? (y/n) ") == "n":
                    reps = eval(input("\nHow many sorts (iterations) to calculate average? "))
                    x = 0
            print("\nBeginning Automated Sorting Runtime Analysis...")
            getTimeAnalysisAutomated(amounts,reps)
            print("-"*40)
            print("Automated Sorting Runtime Analysis Complete.")
        else:
            print("Error. Please restart the program and type one of the listed prompts.")
    else:
        print("Error. Please restart the program and type either 1 or 2")

main()
