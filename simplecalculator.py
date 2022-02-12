import math

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
sum1 = int(num1) + int(num2)
product1 = int(num1) * int(num2)
divide = int(num1) / int(num2)
differnce = int(num1) - int(num2)
percentage = int(num1) / int(num2) * 100
square = int(num1) * int(num1)
sqrt = math.sqrt(num2)
cube = int(num2) * int(num2) * int(num2)
input1 = input('enter name of algebric exprssions: ')

if(input1=='sum'):
    print(sum1)

elif(input1=='product'):
    print(product1)

elif(input1=='divide'):
    print(divide)

elif(input1=='differnce'):
    print(differnce)

elif(input1=='percentage'):
    print(percentage,'%')
    
elif(input1=='square'):
    print(square)

elif(input1=='cube'):
    print(cube)
    
elif(input1=='sqrt'):
    print(sqrt)
 	
else:
    print("NA")
