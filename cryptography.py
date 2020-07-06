import os
file_path = input("Input file path : ")
os.chdir(file_path)
file = os.listdir()
original_name = file[0]

while True:
    # print(file)
    print("Enter Option : ")
    print("1.Encrypt\n2.Decrypt\n3.Exit")
    _input = input()
    if _input == "1":
        os.rename(file[0], "xuv4huci")
        print("Encryption successful.")
    elif _input == "2":
        files = os.listdir()
        os.rename(files[0], original_name)
        print("Decryption successful.")
    elif _input == "3":
        break
    else:
        print("Please Enter correct option ...")
