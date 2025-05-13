#Task 1 - Understanding Python Exceptions
while True:
    try:
        user_input = input("Enter a number: ")
        user_number = float(user_input)
        result = 100 / user_number
        print(f"100 divided by {user_number} is {result}")
        break
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Task 2 - Types of Exceptions
#IndexError 
try:
    pass #remove to attempt this block
    my_list = [1, 2, 3]
    print(my_list[5]) 
except IndexError:
    print("IndexError occurred! List index out of range.")
#KeyError 
try:
    pass #remove to attempt this block
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["gender"])  # Key does not exist
except KeyError:
    print("KeyError occurred! Key not found in the dictionary.")
#TypeError 
try:
    pass #remove to attempt this block
    result = "Age: " + 25  # Cannot add string and integer
except TypeError:
    print("TypeError occurred! Unsupported operand types.")

#Task 3 - Using try...except...else...finally
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
else:
    print(f"The result is {result}.")
finally:
    print("This block always executes.")