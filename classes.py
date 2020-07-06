class Students:

    def print_details(self):
        print(f"Name : {self.name}\nRoll No : {self.roll_no}\nSection : {self.sec}")

std1 = Students()
std1.name = input("Enter name of student : ")
std1.roll_no = input("Enter roll no : ")
std1.sec = input("Enter section : ")


std1.print_details()


