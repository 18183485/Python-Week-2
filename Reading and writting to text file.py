#Challenge 105
file = open("Numbers.txt","w")
file.write("1,2,3,4,5")
file.close()

file = open("Numbers.txt","r")
print(file.read())

#Challenge 106 and 107
filename = open("Names.txt", "w")
filename.write("Lethabo\n")
filename.write("Shani\n")
filename.write("Lani\n")
filename.write("Annie\n")
filename.write("Sam")
filename.close()

filename = open("Names.txt","r")
print(filename.read())

#Challenge 108
filename = open("Names.txt","a")
name = input("Enter name: ")
filename.write(name + "\n")
filename.close()

filename = open("Names.txt","r")
print(filename.read())
filename.close()

#Challenge 109
print("1) Create a new file\n"+ "2) Display the file\n"+ "3) Add new item to file")

selection = int(input("Make a selection: "))

if selection == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt","w")
    file.write(subject + "\n")
    file.close()
elif selection == 2:
    file = open("Subject.txt", "r")
    print(file.read())
elif selection == 3:
    file = open("Subject.txt", "a")
    subject = input("Enter school subject: ")
    file.write(subject + "\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
else:
    print("Invalid option.")




























































































































