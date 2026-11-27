import mysql.connector
mydb=mysql.connector.connect(
    user='user',password='password',host='localhost',port='port',database='python'
)
mycursor=mydb.cursor()
sql='create table if not exists workers (work_id int primary key auto_increment,name varchar(90),age int,department varchar(90))'
mycursor.execute(sql)
mydb.commit()

class Worker:
    def __init__(self,name=None,age=None,department=None):
        self.name=name
        self.age=age
        self.department=department

    def addwork(self):
        name=input("enter the name:").strip()
        try:
            age = int(input("Enter the age: "))
        except ValueError:
            print("Age must be a number.")
            return
        if age<0 or age>110:
             print("invalid age")
             return

        department = input("Enter the department: ").strip()
        if name == "" or department == "":
            print("Name and department cannot be empty.")
            return

        sql = 'insert into workers (name, age, department) values (%s, %s, %s)'
        val = (name, age, department)

        mycursor.execute(sql, val)
        mydb.commit()
        print("Worker added successfully.")
    def viewwork(self):
         print("1. View All Workers\n"
               "2. Search Worker by ID")

         try:
            choice = int(input("Enter your choice: "))
         except ValueError:
            print("Invalid input")
            return

         if choice == 1:
            mycursor.execute('select * from workers')
            found=False
            for i in mycursor:
                print(i)
                found=True
            if not found:
                print("No workers found.")
         elif choice==2:
               try:
                    id = int(input("Enter Worker ID: "))
               except ValueError:
                    print("Invalid ID")
                    return

               sql = "select * from workers where work_id=%s"
               mycursor.execute(sql, (id,))
               for i in mycursor:
                    print(i)
                    found=True
               if not found:
                         print("No workers found.")

         else:
              print("invalid choice")

    def updatework(self):

        try:
            id = int(input("Enter ID to update: "))
        except ValueError:
            print("ID must be a number.")
            return

        field = input("Enter field to update (name,age,department):").strip().lower()

        allowed_fields = {"name", "age", "department"}

        if field not in allowed_fields:
            print("Invalid field.")
            return

        if field == "age":
            try:
                new_value = int(input("Enter new age: "))
            except ValueError:
                print("Age must be a number.")
                return

            if new_value <= 0 or new_value>=110:
                print("invalid age.")
                return

        else:

            new_value = input("Enter new value: ").strip()
            if new_value == "":
                print("Value cannot be empty.")
                return

        sql = f"update workers set {field}=%s where work_id=%s"
        val = (new_value, id)

        mycursor.execute(sql, val)
        mydb.commit()

        if mycursor.rowcount == 0:
            print("No worker updated")
        else:
            print("Worker updated successfully")

    def deletework(self):
        try:
            id = int(input("Enter ID to delete: "))
        except ValueError:
            print("ID must be a number.")
            return

        sql = 'delete from workers where work_id=%s'
        val = (id,)

        mycursor.execute(sql, val)
        mydb.commit()

        if mycursor.rowcount == 0:
            print("No worker found with that ID.")
        else:
            print("Worker deleted successfully.")
    def filterwork(self):
            
            department = input("Enter department: ").strip()
            sql = 'select * from workers where department=%s'
            val=(department,)
            mycursor.execute(sql,val)
            found=False
            for i in mycursor:
                 print(i)
                 found=True
            if not found:
                 print("No workers found.")
obj=Worker()
while True:
     print( "1. Add workers\n"
            "2. View workers\n"
            "3. Update workers\n"
            "4. Delete workers\n"
            "5. filter by department\n"
            "0. Exit\n")
     try:
        choice = int(input("Enter Your Choice: "))
     except ValueError:
        print("Please enter a valid number.")
        continue

     if choice==1:
             obj.addwork()
     elif choice==2:
             obj.viewwork()
     elif choice==3:
             obj.updatework()
     elif choice==4:
             obj.deletework()
     elif choice==5:
             obj.filterwork()
     elif choice==0:
              print("exiting")
              break      
     else:
           print("invalid choice")

mycursor.close()
mydb.close() 