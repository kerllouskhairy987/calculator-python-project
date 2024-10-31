# Calculator Function: This program performs basic arithmetic operations based on user input.

try:
    FNum = float(input("Enter Your First Number: "))
    operator = input("Enter Your Operator: ")
    SNum = float(input("Enter Your Second Number: "))
    def calc(num1, num2, operator):
        if operator == "+":
            return(num1 + num2)
        elif operator == "-":
            return(num1 - num2)
        elif operator == "*":
            return(num1 * num2)
        elif operator == "/":
            return(num1 / num2)
        elif operator == "^" or operator == "pow":
            return(num1 ** num2)
        else:
            return("Enter A Valid Operator")
    print(calc(FNum, SNum, operator))
# Handle the case where division by zero is attempted.
except ZeroDivisionError:
    print("Zero Division Error ...")
# Handle any other errors such as invalid input (non-numeric).
except:
    print("Enter A Valid Number ...")