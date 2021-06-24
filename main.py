import math
num1 = float(input('Enter the first number: '))
information = input("Select an operator from the list +,-,*,/: ")
num2 = float(input('Enter the second number: '))
if information == '+':
    print(num1 + num2)
elif information == '-':
    print(num1 - num2)
elif information == '*':
    print( num1 * num2)
elif information == '/':
    print(num1 / num2)
else:
    print(' There is no such operation !')
