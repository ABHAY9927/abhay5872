"""This code based on python mysql 
    we create school_management database and create three tables 
    1st table == student(name, age, grade, email)
    2nd table == teacher(name, address, age, email, class)
    3rd table == class_name(subject, class, teacher_name(foreign key))
insert the data from csv files 
Programmer = Abhay kumar
Date = 01/02/2025
"""

import mysql.connector
import csv
def insert_data_from_csv(file_name, insert_query, conn):
    """This is the funtion to insert the data from csv files"""
    with open(file_name, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        cursor = conn.cursor()
        for row in csv_reader:
            cursor.execute(insert_query, row)
            conn.commit()
            
conn =mysql.connector.connect(host="localhost", port=3306, user="abhay", password="abhay",database="school_management") 
insert_students_query = "INSERT INTO student(name, age, grade, email) VALUES (%s, %s, %s, %s)"
insert_teachers_query = "INSERT INTO teacher(name, age, address, email, class) VALUES (%s, %s, %s, %s, %s)"
insert_classes_query = "INSERT INTO class_name(subject, class, teacher_name) VALUES (%s, %s, %s)"
insert_data_from_csv('/home/vboxuser/Documents/student.csv',insert_students_query,conn)
insert_data_from_csv('/home/vboxuser/Documents/teachers.csv',insert_teachers_query,conn)
insert_data_from_csv('/home/vboxuser/Documents/classes.csv',insert_classes_query,conn)
conn.close()
print("csv data imported successfully to mysql")
