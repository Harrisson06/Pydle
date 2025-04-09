# Task 1 Harrison Macdonald
# Student number: 28958802

#list to store all user inputted numbers
user_number_list = []
#list stores all Even numbers 
odd_number_list = []
#list stores all Odd numbers
even_number_list = []
#counts the number of unique numbers 
total_unique_numbers = 0
#true variable for simplicity
running = True

#function to gather user input, numbers and options
def user_numbers():
    global user_number_list
    while running:
        try: 
            print(f"Inputted Numbers are: {user_number_list}"
                   if user_number_list else "No Inputted Numbers")
            user_input = int(input("Please enter a positive integer: \n>"))
            #stops the user entering a non-positive number
            if user_input <= 0:
                print("Only enter Positive integers, Please try again.")
                continue
            #adds the users numbers to the list 
            user_number_list.append(user_input)
            print(f"Added {user_input} to the List.")
        except ValueError:
            print("Invalid Input. PLease pick a non-negative whole number only.")
            
        #options to allow the user to input more number
        try:
            options = int(input("Do you want to Add additional numbers?"
                                "[1. Yes] [2. No]"))
            if options== 2:
                break
        except ValueError:
            print("Invalid input. Please enter either 1 or 2.")

            
#function to seperate all duplicate numbers into another list
def duplicate_removal(numbers):
    global duplicate_numbers
    global seen_numbers

    duplicate_numbers = []
    seen_numbers = {}

    #looping throught all numbers to check duplicate 
    for number in numbers:
        if number not in duplicate_numbers:
            duplicate_numbers.append(number)
    removed_duplicate = len(numbers) - len(duplicate_numbers)
    print(f"Removed {removed_duplicate} numbers from the list")
    return duplicate_numbers

# Checking for unique numbers and assigning them to a dictionary.
# Counting the number of unique numbers.
def unique_numbers(numbers):
    number_counts = {}  
    unique_numbers_list = []
    for number in numbers:
        number_counts [number] =+ 1
        for number in numbers:
            if numbers in tuple(number_counts) == 1:
                unique_numbers_list.append(number)
        continue
    print(number_counts)

#function to move Odd and Even numbers into seperate lists
def even_odd_seperate(numbers):
    for number in numbers:
        if number % 2 == 0:
            even_number_list.append(number)
        else:
            odd_number_list.append(number)




#function to calculate the mean of the users numbers
def mean(numbers):
    total = 0
    count = 0

    for number in numbers:
        total += number
        count += 1
    return total / count

#function to calculate the product of the users numbers
def product(numbers):
    product = 1

    for number in numbers:
        product *= number
    return product

#function to calculate the variance of the users numbers
def variance(numbers):
    global means
    means = mean(numbers)
    squared_differences = 0
    count = 0

    for number in numbers:
        squared_differences += (number - means) ** 2
        count += 1 
    return squared_differences / count

#function to calculate the reange of the users numbers
def range(numbers):
    return numbers[-1] - numbers[0]
def main():
    #Execution of the functions to the user
    print("| Task 1 |")
    user_numbers()
    duplicate_removal(user_number_list)
    unique_numbers(user_number_list)
    even_odd_seperate(user_number_list)

    #all functions in use to provide all information required
    print(f"\nYour Numbers: \n{user_number_list}")
    print(f"Unique Numbers: {len(duplicate_numbers)}")
    print(f"Removed Numbers: {duplicate_numbers}")
    #telling the user if there are no odd or even numbers in the list
    if len(odd_number_list) == 0:
        print("There are no Odd Numbers")
    if len(even_number_list) == 0:
        print("There are no Even Numbers")
    print(f"product: {product(user_number_list)}")
    print(f"Range: {range(user_number_list)}")
    print(f"Variance {variance(user_number_list)}")
	
main()