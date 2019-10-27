import sqlite3

#attaches to database1.db, this could be turned into dynamic request
conn = sqlite3.connect('/home/hbudzik/python/class_py_web_programming/sqlite_code/database1.db')
c = conn.cursor()

#prints menu
def interface_menu():
    print(
        "\tMenu\n"
        "\t 1) Prints out current data\n"
        "\t 3) Enter Data Into Table\n"
        "\t 5) Quit"
         )
    user_interface_input = input("\t :> ")
    return user_interface_input

#create table
def create_table():
    c.execute("CREATE TABLE table1(Day TEXT, Hours REAL, Tot REAL)")

#adds data to database/tables
def dynamic_enter_data():                    
    print("...\tdynamic_enter_data() init")

#create/ read database
def read_database():
    sql = "SELECT * FROM table1"
    for row in c.execute(sql):
        print(row)

    



##### interface #####
opt = interface_menu()
if opt == "1":
    print("\tyou selected 1")
elif opt == "2":
    print("\tyou selected 2")
elif opt == "3":
    print("\tyou selected 3")
else:
    print("\tIncorrect selection!!!")

#user_interface_input = input("Please select your option: ")
#while x == False:

    

#print("...\tCreating table1")
#create_table()

#prints out the whole database
print("... read_database() init")
read_database()

#closes database
print("... conn.close() init")
conn.close()