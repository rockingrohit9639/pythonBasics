#Functions are the building blocks which contains some code which cn be used anywhere in the program
#Docstring is the string in a functions which tells what a function will do
def addition(a, b, c):
    """This functions adds three numbers"""
    d = a+b+c
    return d

try:
    num1 = int(input("Enter No. 1 : "))
    num2 = int(input("Enter No. 2 : "))
    num3 = int(input("Enter No. 3 : "))
    result = addition(num1, num2, num3)
    print("Addition of numbers =", result)
except Exception as a:
    print(a)

print(addition.__doc__)