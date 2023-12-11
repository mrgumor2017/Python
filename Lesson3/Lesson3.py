number=int(input('Enter number:'))
if number%2==0:
    print('Even number')
else:
    print('Odd number')


number=int(input('Enter number:'))
if number%7==0:
    print('Number is a multiple of 7')
else:
    print('Number is not a multiple of 7')

number1=int(input('Enter first number:'))
number2=int(input('Enter second number:'))
if number1>number2:
    print(number1)
elif number2>number1:
    print(number2)
else:
    print('Числа однакові')

number1=int(input('Enter first number:'))
number2=int(input('Enter second number:'))
if number1<number2:
    print(number1)
elif number2<number1:
    print(number2)
else:
    print('Числа однакові')

number1=int(input('Enter first number:'))
number2=int(input('Enter second number:'))
print('1.суму двох чисел\n2.різницю двох чисел\n3.середньоарифметичне\n4.добуток двох чисел')
diya=input('Enter diya:')
if diya=='1':
    print(number1+number2)
elif diya=='2':
    print(number1-number2)
elif diya=='3':
    print((number1+number2)/2)
elif diya=='4':
    print(number1*number2)
else:
    print('Error')