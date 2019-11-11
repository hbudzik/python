import sqlite3


#attaches to database1.db, this could be turned into dynamic request
conn = sqlite3.connect(':memory:')
c = conn.cursor()


#prints menu
def interface_menu():
    print(
        "\n\tMenu\n"
        "\t 1) Prints out current data\n"
        "\t 2) Enter Data Into Table\n"
        "\t 3) Delete Data From Table\n"
        "\t 4) Update table entry\n"
        "\t 5) Quit"
         )
    user_interface_input = input("\t :> ")
    return user_interface_input


#create table
def create_table():
    c.execute("CREATE TABLE table1(     Key_id INTEGER,     "
                                "       First_name TEXT,    "
                                "       Last_name TEXT,     "
                                "       Salary REAL        )"
             )
    c.execute("INSERT INTO table1 (Key_id, First_name, Last_name, Salary) VALUES (?, ?, ?, ?)", 
        (1, 'FIRST NAME', 'LAST NAME', 'SALARY'))
    conn.commit()


#adds data to database/tables
def dynamic_enter_data():                    
    print("...\tdynamic_enter_data() init")
 
    key_id = int(input("id: "))
    name_first = input("First Name: ")
    name_last = input("Last Name:  ")
    salary_var = int(input("salary: "))

    c.execute("INSERT INTO table1 (Key_id, First_name, Last_name, Salary) VALUES (?, ?, ?, ?)", 
        (key_id, name_first, name_last, salary_var))
    conn.commit()


#create/ read database
def read_database():
    #print("...\tread_database() init")

    sql = "SELECT * FROM table1"
    for row in c.execute(sql):
        print(row)


##### interface #####
#start main 

create_table() 
    #creates table in database named 'table1' and adds initial rows with columns

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
        print("\t you selected 3")
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
