def particular_age(years):
    year = int(input("Enter year : "))
    return year - years


if __name__ == '__main__':
    while True:
        _input = int(input("Enter your age or year of birth : "))
        if _input >0 and _input < 100:
            print(f"After {100 - _input} years you will be hundred.")
            op = input("Do you want to know your age in particular year(yes/no) : ")
            if op == 'yes' or 'y':
                age = 2020 - _input
                print(f"Your age will be {particular_age(age)}")
            elif op == 'no' or op == 'n':
                print("Ok Thank You")
            else:
                print("Wrong Choice")
        elif _input > 1900 and _input <2020:
            age = 2020 - _input
            print(f"After {100 - age} years you will be hundred..")
            op = input("Do you want to know your age in particular year(yes/no) : ")
            if op == 'yes' or op == 'y':
                print(f"Your age will be {particular_age(_input)}")
            elif op == 'no' or op == 'n':
                print("Ok Thank You")
            else:
                print("Wrong Choice")
        else:
            print("Your age is not valid.")
