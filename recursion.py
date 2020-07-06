# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# num = int(input("Enter the number to find factorial : "))
# print("Factorial = ", fact(num))

#Fabonicci Series
def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)

num1 = int(input("Enter the number : "))
print(fab(num1))