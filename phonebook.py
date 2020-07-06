f = open("phonebook.csv", "a")
name = input("Enter name : ")
number = input("Enter number : ")

f.write(name)
f.write("\t")
f.write(number)
f.write("\n")
f.close()