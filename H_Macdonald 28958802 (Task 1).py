# Task 1 Harrison Macdonald
# Student number: 28958802
import numpy
#list to store all user inputted numbers
NumberList = []
#list stores all Even numbers 
OddNumberList = []
#list stores all Odd numbers
EvenNumberList = []
#counts the number of unique numbers 
TotalUniqueNumbers = []
#true variable for simplicity
Running = True

#function to gather user input, numbers and options
def user_numbers():
    global NumberList
    while Running:
        try: 
            print(f"Inputted Numbers are: {NumberList}"
                   if NumberList else "No Inputted Numbers")
            UserInput = int(input("Please enter a positive integer: \n>"))
            #stops the user entering a non-positive number
            if UserInput <= 0:
                print("Only enter Positive integers, Please try again.")
                continue
            #adds the users numbers to the list 
            NumberList.append(UserInput)
            print(f"Added {UserInput} to the List.")
        except ValueError:
            print("Invalid Input. PLease pick a non-negative whole number only.")
            
        #options to allow the user to input more number
        try:
            Options = int(input("Do you want to Add additional numbers?"
                                "[1. Yes] [2. No]"))
            if Options == 2:
                break
        except ValueError:
            print("Invalid input. Please enter either 1 or 2.")

            
#function to seperate all duplicate numbers into another list
def duplicate_removal(NumberList):
    global DuplicateNumbers
    global RemoveDuplicates

    DuplicateNumbers = []
    RemoveDuplicates = []
    #looping throught all numbers to check duplicate 
    for Number in NumberList:
        if Number not in DuplicateNumbers:
            DuplicateNumbers.append(Number)

    if Number in NumberList and DuplicateNumbers:
        RemoveDuplicates.append(Number)

    print(f"Removed {RemoveDuplicates} numbers from the list")
    return DuplicateNumbers

# Checking for unique numbers and assigning them to a dictionary.
# Counting the number of unique numbers.
def unique_numbers(NumberList):
    NumberCounts = {}  
    UniqueNumbersList = []

    for number in NumberList:
        NumberCounts [number] =+ 1

    for number in NumberCounts:
        UniqueNumbersList.append(number)
    if number not in UniqueNumbersList:
        TotalUniqueNumbers.append(number)
    print(NumberCounts)

#function to move Odd and Even numbers into seperate lists
def even_odd_seperate(Numbers):
    for Number in Numbers:
        if Number % 2 == 0:
            EvenNumberList.append(Number)
        else:
            OddNumberList.append(Number)

#function to calculate the mean of the users numbers
def mean(Numbers):
    Total = 0
    Count = 0

    for Number in Numbers:
        Total += Number
        Count += 1
    return Total / Count

#function to calculate the product of the users numbers

#function to calculate the variance of the users numbers
def variance(Numbers):
    global Means
    Means = mean(Numbers)
    SquaredDifferences = 0
    count = 0

    for Number in Numbers:
        SquaredDifferences += (Number - Means) ** 2
        count += 1 
    return SquaredDifferences / count

#function to calculate the reange of the users numbers
def range(Numbers):
    return Numbers[-1] - Numbers[0]

def main():
    #Execution of the functions to the user
    print("| Task 1 |")
    user_numbers()
    duplicate_removal(NumberList)
    unique_numbers(NumberList)
    even_odd_seperate(NumberList)

    #all functions in use to provide all information required
    print(f"\nYour Numbers: \n{NumberList}")
    print(f"Unique Numbers: {len(RemoveDuplicates)}")
    print(f"Removed Numbers: {DuplicateNumbers}")

    #telling the user if there are no odd or even numbers in the list
    if len(OddNumberList) == 0:
        print("There are no Odd Numbers")

    if len(EvenNumberList) == 0:
        print("There are no Even Numbers")

    #print(f"product: {product(UserNumberList)}")
    print(f"Range: {range(NumberList)}")
    print(f"Variance {variance(NumberList)}")
	
main()