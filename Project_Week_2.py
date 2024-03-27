from datetime import datetime

def signup():
    print("Please enter user name")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_information(username, password)
    print("WELCOME TO LOGIN PAGE! ")
    login()

def user_information(ussnm, pssd):
    name = input("Name: ")
    address = input("Address: ")
    age = input("Age: ")
    ussnm_ = ussnm + " task.txt"

    file = open(ussnm_, "a")
    file.write(pssd)
    file.write("\nName: ")
    file.write(name)
    file.write("\n")
    file.write("Address: ")

    file.write(address)
    file.write("\n")
    file.write("Age: ")
    file.write(age)
    file.write("\n")
    file.close()

def login():
    print("Please enter your username ")
    user_nm = input("Enter username: ")
    
    #Login password
    pssd_wr = (input("Enter password: ")) + "\n"
    try:
        usernm = user_nm + " task.txt"
        f_ = open(usernm, "r")

        k = f_.readlines(0)[0]
        f_.close()

        if pssd_wr == k:
            print('''1) View your data \n2) Add task \n3) Update task status \n4) View task status''')
            a = input()
            if a == '1':
                view_data(usernm)
            elif a == '2':
                task_information(usernm)
            elif a == '3':
                task_update(user_nm)
            elif a == '4':
                task_update_viewer(user_nm)
            else:
                print("Incorrect Input!")
        else:
            print("Incorrect password or username, Please try again!")
            login()
    except Exception as e:
        print(e)
        login()

def view_data(username):
    ff = open(username, "r")
    print(ff.read())
    ff.close()

def task_information(username):
    print("Enter no. of tasks you want to add.")
    j = int(input())
    f1 = open(username, "a")

    for i in range(1, j+1):
        task = input("Enter task: ")
        target = input("Enter Target: ")
        pp = "TASK " + str(i) + " :"
        qq = "TARGET " + str(i) + " :"

        f1.write(pp)
        f1.write(task)
        f1.write('\n')
        f1.write(qq)
        f1.write(target)
        f1.write('\n')

        print("STOP: Space bar or ENTER: Continue")
        s = input()
        if s == ' ':
            break
    f1.close()
    #login()

def task_update(username):
    username = username + " TASK.txt"
    print("Enter completed tasks: ")

    task_completed = input()
    print("Enter tasks not started yet: ")

    task_not_started = input()
    print("Enter tasks you're still doing: ")

    task_ongoing = input()
    fw = open(username, "a")
    DT = str(datetime.now())

    fw.write(DT)
    fw.write("\n")
    fw.write("COMPLETED TASK\n")
    fw.write(task_completed)
    fw.write("\n")
    fw.write("ONGOING TASK\n")
    fw.write(task_ongoing)
    fw.write("\n")
    fw.write("NOT YET STARTED\n")
    

def task_update_viewer(username):
    ussnm = username + " TASK.txt"
    o = open(ussnm, "r")
    print(o.read())
    o.close()

if __name__ == '__main__':
    print("WELCOME TO LETHABO'S TASK MANAGER!!! \n")
    print("Are you a new user? \n")
    a = int(input("Enter 1 to sign up or Enter 0 to login: "))

    if a == 1:
        signup()
    elif a == 0:
        login()
    else:
        print("You have entered wrong input!")