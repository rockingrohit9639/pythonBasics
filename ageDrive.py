print("What is your age : ", end="")
age = int(input())

if age > 18:
    print("Yes!!, You can drive.")
elif age == 18:
    print("You are 18 years old. You have to come our office.")
else:
    print("You are below 18. Hence you cannot drive.")