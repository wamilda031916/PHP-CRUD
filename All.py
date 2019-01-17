import pymysql
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='autograph_book',
    )



def create():
   
    fname = input("Enter your First Name: ")
    lname = input("Enter your Last Name:  ")
    address=input("Enter our Address:  ");
    age = input("Enter your Age: ")
    gender = input("Enter your Gender: ")

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (`first_name`, `last_name`, `address`, `age`,`gender`) VALUES (%s, %s, %s, %s ,%s)"
            try:
                cursor.execute(sql, (fname, lname, address,age,gender))
                print("Task added successfully")
            except Exception as e:
                print("Oops! Something wrong")
                print (e);
 
            connection.commit()
    finally:
        connection.close()

def read():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users "
            try:
                cursor.execute(sql)
                result = cursor.fetchall()
 
                print("Id\t\t First Name\tLast Name\tAdress\tAge\tGender")
                print("---------------------------------------------------------------------------")
                for row in result:
                    print(str(row[0]) + "\t\t" + row[1] + "\t\t" + row[2] + "\t\t" +row[3]+"\t"+str(row[4])+"\t"+row[5])
 
            except Exception as e:
                print("Oops! Something wrong")
                print (e)
 
            connection.commit()
    finally:
        connection.close()

def update():
    
    studid=input("Input Id to Edit: ")
    print("What to Update\n1. Fname\n2. Lname\n3. Adress\n4. Age\n5. Gender")
    choice=int(input())

    if choice==1:
        new=input("Enter The New First Name:  ")
        sql = "UPDATE users SET first_name=%s WHERE `id` = %s"
    elif choice==2:
        new=input("Enter The New Last Name:  ")
        sql = "UPDATE users SET last_name=%s WHERE `id` = %s"
    elif choice==3:
        new=input("Enter The New Adress:  ");
        sql = "UPDATE users SET address=%s WHERE `id` = %s"
        
    elif choice==4:
        new=input("Enter The New Age:  ")
        sql = "UPDATE users SET age=%s WHERE `id` = %s"
    elif choice==5:
        new=input("Enter The New Gender:  ")
        sql = "UPDATE users SET gender=%s WHERE `id` = %s"
    else:
        print("Invalid Input")



    try:
        with connection.cursor() as cursor:
            
            try:
                cursor.execute(sql, (new,studid))
                print("Successfully Updated...")
            except Exception as e:
                print("Oops! Something wrong")
                print (e)
     
        connection.commit()
    finally:
        connection.close()
def delete():
    id=input("Input Id to be Deleted: ")

    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM users WHERE id = %s"
            try:
                cursor.execute(sql, (id,))
                print("Successfully Deleted...")
            except Exception as e:
                print("Oops! Something wrong")
                print (e)
 
        connection.commit()
    finally:
        connection.close()

print("----Simple Student CRUD program in Python----");
print("1. Create\n2. Read\n3. Update\n4. Delete");
choice=int(input("Enter Your Choice:   "))

if choice==1:
    create()
elif choice==2:
    print("List of Student: ")
    read()
elif choice==3:
    
    update()
elif choice==4:
    
    delete()
else:
    print("Invalid Input");




