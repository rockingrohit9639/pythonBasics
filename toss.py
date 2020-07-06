import random
l = []

print("Enter names of Players : ")
print("Press 0 if done")
while True:
    names = input()
    l.append(names)
    if names == "0":
        break

winner = random.choice(l)
print("Winner is : ",winner)