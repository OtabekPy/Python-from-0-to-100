import math
print("There is oly +,-,/,*,Sqr,power")
chooses=input("Choose: ")
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
chooses=chooses.capitalize()
if chooses == "+":
    print(number1+number2)
elif chooses == "-":
    print(number1-number2)
elif chooses == "*":
    print(number1*number2)
elif chooses == "/":
    print(number1/number2)
elif chooses == "^":
    print(number1**number2)
elif chooses=="Sqr":
    print(math.sqrt(number1))
    print(math.sqrt(number2))
else:
    print("Invalid input")