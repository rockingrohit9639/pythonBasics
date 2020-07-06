d1 = {
    "Rohit":"Saini",
    "Lalit":"Singh",
    "Abhinav":"Baliyan",
    "Shubham":"Singh",
    "Khushi":"Sharma"
}
#print("Surname of Rohit is",d1["Rohit"])
x = d1.setdefault("Khushi", "Sharma")
print(x)
print(d1)