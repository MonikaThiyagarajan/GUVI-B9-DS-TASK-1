import mysql.connector
mydb = mysql.connector.connect(host = "localhost",user="root",password="",database="marks")

#def 1
def Addstudent(Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade):
    mycursor = mydb.cursor()
    sql = "INSERT INTO student (Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade)   
    mycursor.execute(sql,val)
    mydb.commit()
    print("Student added successfully")

#def 2
def GetStudent(id):
    mycursor = mydb.cursor()
    sql = "SELECT ID,Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade from student where id =%s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    print(myresult)
    
#def 3
def GetAllStudent():
    mycursor = mydb.cursor()    
    sql = "SELECT ID,Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade from student"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)

#def 4
def UpdateStudent(Name,School,Class,Tamil,English,Math,Science,Social,ID):
    mycursor = mydb.cursor() 
    sql = "Update Student set Name=%s,School=%s,Class=%s,Tamil=%s,English=%s,Math=%s,Science=%s,Social=%s where id =%s"
    val = (Name,School,Class,Tamil,English,Math,Science,Social,ID)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Student updated successfully")

#def 5
def DeleteStudent(a):
    mycursor = mydb.cursor() 
    sql = "Delete from Student where id=%s"
    val=(a,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Student deleted successfully")

#def 6
def Exit():
    pass

while True:
        print("Menu")
        print("1.Add a Student")
        print("2.Get a student")
        print("3.Get all students")
        print("4.Update a student")
        print("5.Delete a student")
        print("6.Exit")
        choice=int(input("Enter your choice: "))
        mydb = mysql.connector.connect(host = "localhost",user="root",password="",database="marks")
        
#Menu 1 add a student
    
        if choice ==1 :
            Name = input("Name: ")
            School = input("School: ")
            Class = int(input("Class: "))
            Tamil = int(input("Tamil: "))
            English = int(input("English: "))
            Math = int(input("Math: "))
            Science = int(input("Science: "))
            Social = int(input("Social: "))
            Total = Tamil+English+Math+Science+Social
            print("Total: "+ str(Total))
            Average = Total/5
            print("Average: "+str(Average))
            Grade =''
            if (Average>=0 and Average <35):
                Grade = "C"
                print("Grade C")
            elif (Average>=35 and Average <70):
                Grade = "B"
                print("Grade B")
            elif (Average>=70 and Average <=100):
                Grade = "A"
                print("Grade A")
            Addstudent(Name,School,Class,Tamil,English,Math,Science,Social,Total,Average,Grade)
  
#Menu 2 Get a student    
    
        elif choice == 2:
            id = input("Enter the ID: ")
            GetStudent(id)
            
            
#Menu 3 Get all students 
    
        elif choice == 3:
            GetAllStudent()

#Menu 4 Update a student
    
        elif choice == 4:
            ID = int(input("ID:"))
            Name = input("Name: ")
            School = input("School: ")
            Class = int(input("Class: "))
            Tamil = int(input("Tamil: "))
            English = int(input("English: "))
            Math = int(input("Math: "))
            Science = int(input("Science: "))
            Social = int(input("Social: "))
            UpdateStudent(Name,School,Class,Tamil,English,Math,Science,Social,ID)

#Menu 5 Delete a student
   
        elif choice == 5:
            a = input("Enter student Id: ")  
            DeleteStudent(a)

#Menu 6 Exit 
    
        elif choice == 6:
            print("EXIT")
            
        else:
            print("Enter valid choice") 

    
    

       
