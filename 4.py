# define functions
def add(x, y):
    """This function adds two numbers"""
    return str(int(x) + int(y)) # here we need to change string input into integer


def subtract(x, y):
    """This function subtracts two numbers"""
    return str(int(x) - int(y))


def multiply(x, y):
    """This function multiplies two numbers"""
    return str(int(x) * int(y))

def divide(x, y):
    """This function divides two numbers"""
    return str(int(x) / int(y))


# ask for input from the user
while True:

    num1 = input("Enter a number (or a letter to exit): ")

    if num1.isalpha(): #check if it is a letter
        break

    elif num1.isdigit(): # check if it is a number

        operation = input("Choose an operation: ")

        if operation == '+' or operation == '-' or operation == '*' or operation == '/':

            num2 = input("Enter another number: ")

            if num2.isdigit():

                if operation == '+':
                    print("Result: ", add(num1, num2))

                elif operation == '-':
                    print("Result: ", subtract(num1, num2))

                elif operation == '*':
                    print("Result: ", multiply(num1, num2))

                elif operation == '/':
                    if num2 == "0":        #if sb decides to devide by 0
                        print("Do not mess with the rules of mathematics ;)")

                    else:
                        print("Result: ", divide(num1, num2))

            else:
                print("Next time choose a number.")
        else:
            print("Invalid sign.")
    else:
        print("Try with numbers.")

    print("") #leave one line before next loop