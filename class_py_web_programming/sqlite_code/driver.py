import sqlite3


#attaches to database1.db, this could be turned into dynamic request
conn = sqlite3.connect('/home/hbudzik/python/class_py_web_programming/sqlite_code/database1.db')
c = conn.cursor()


#prints menu
def interface_menu():
    print(
        "\n\tMenu\n"
        "\t 1) Prints out current data\n"
        "\t 2) Enter Data Into Table\n"
        "\t 3)\n"
        "\t 4) create new table\n"
        "\t 5) Quit"
         )
    user_interface_input = input("\t :> ")
    return user_interface_input


#create table
def create_table():
    #table_name = input("New table name: ")
    #column_name1 = input("Column name1: ")
    #column_name2 = input("Column name2: ")
    #column_name3 = input("Column name3: ")

    c.execute("CREATE TABLE table1( column_name1 VARCHAR,   "
                                "       column_name2 VARCHAR,   "
                                "       column_name3 VARCHAR)   " )
    conn.commit()


#adds data to database/tables
def dynamic_enter_data():                    
    print("...\tdynamic_enter_data() init")

    day = input("Enter day: ")
    hours = input("hours: ")
    tot = input("total$: ")

    c.execute("INSERT INTO table1 (Day, Hours, Tot) VALUES (?, ?, ?)", (day, hours, tot))
    conn.commit()


#create/ read database
def read_database():
    #print("...\tread_database() init")

    sql = "SELECT * FROM table1"
    for row in c.execute(sql):
        print(row)


##### interface #####
loop_var = False
while loop_var == False:
    opt = interface_menu()
    if opt == "1":
        #prints out the whole database
        print("... \tread_database() init")
        read_database()
    elif opt == "2":
        dynamic_enter_data()
    elif opt == "3":
        print("\tyou selected 3")
    elif opt == "4":
        create_table()
    elif opt == "5":
        loop_var = True
    else:
        print("\tIncorrect selection!!!")

#user_interface_input = input("Please select your option: ")
#while x == False:

    

#print("...\tCreating table1")
#create_table()



#closes database
print("... conn.close() init")
conn.close()