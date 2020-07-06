"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - Process of Iterator and Iterable
"""
def fibo(m):
    n1 = 1
    n2 = 1
    for i in range(m):
        n3 = n1
        n1 = n2
        n2 = n1 + n3
        yield n3


def facto(n):
    n1 = 1
    for i in range(1,n+1):
        n1 *= i
        yield n1

def main():
    print("---------MENU--------")
    print("1 : Fibonnaci Series")
    print("2 : Factorial ")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        m = int(input("Enter Number : "))
        fibo(m)
        a = fibo(m)
        for i in range(0,m):
            print(a.__next__())

    elif choice == 2:
        n = int(input("Enter Number : "))
        facto(n)
        for i in facto(n):
            print (i)
    else:
        print("Invalid Input !!! Choose from the Menu")


if __name__ == '__main__':
    main()
