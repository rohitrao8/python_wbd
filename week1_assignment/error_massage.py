user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print("You entered the integer:", number)
except ValueError:
    print("Error: That is not a valid number.")
