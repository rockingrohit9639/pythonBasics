list1 = [int, float,"Rohit", 1, 67, "Ninja", 22, 0,1,4,"etc"]

for item in list1:
    if str(item).isnumeric() and item > 6:
        print(item)