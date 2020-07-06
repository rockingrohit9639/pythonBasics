f = open("readable.txt", "r")
# line1 = f.readline() reads first line of file
# line2 = f.readline() reads second line of file and so on
# print(content)

# for line in f:
#     print(line, end="")  reading line by line using for loops
# print(line1) print first line of file
# print(line2) print second line of file

# print(f.readline()) prints line by line

list_of_lines = f.readlines() #reads contents as a list

print(list_of_lines)

f.close()
