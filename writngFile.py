#Writing mode- removes all previous data of file
# f = open("rohit.txt", "w")
# f.write("Hello this is writing to file 'rohit.txt' \n")
# f.close()

#Appending mode - Keeps previous data of file
# f = open("rohit2.txt", "a")
# f.write("Hello this is writing to file 'rohit2.txt' \n")
# f.close()

# f = open("rohit2.txt", "r+")
# print(f.read())
# f.write("This is reading and writing mode both.")
# f.close()

with open("rohit.txt") as f:
    print(f.readlines())