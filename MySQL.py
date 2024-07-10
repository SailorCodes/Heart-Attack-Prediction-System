import mysql.connector
from tkinter import messagebox


def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        mydb = mysql.connector.connect(host='localhost',user='root',password="992922")
        mycursor = mydb.cursor()
        print("Connection stablished!")

    except:
        messagebox.showerror("Connection","Database connection not stablished!")

    try:
        command = "Create database Heart_Data"
        mycursor.execute(command)

        command = "Use Heart_Data"
        mycursor.execute(command)

        command = "Create table data(user int auto_increment key not null, Name varchar(50), Data varchar(100), Dob varchar(100), age varchar(100), sex varchar(100), Cp varchar(100), trestbps varchar(100), chol varchar(100), fbs varchar(100), restecg varchar(100), thalach varchar(100), exang varchar(100), oldpeak varchar(100), slope varchar(100), ca varchar(100), thal varchar(100), result varchar(100))"
        mycursor.execute(command)

        command="insert into data(Name,Date,Dob,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Resgister","New user added sucessfully!")
    
    except:
        mycursor.execute("use Heart_Data")
        mydb=mysql.connector.connect(host="localhost",user='root',password='992922',database='Heart_Data')
        mycursor=mydb.cursor()

        command="insert into data(Name,Date,Dob,age,sex,Cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,Result) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(command,(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Resgister","New user added sucessfully!")



# Save_Data_MySql('mr unknown',"08/08/2023","1970","44","1","1","233","223","1","1","233","1","233.0","0","2","1","0")