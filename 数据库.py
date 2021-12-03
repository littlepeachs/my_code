import sqlite3

db = sqlite3.connect("university.db")
cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students
(id integer PRIMARY KEY,
name text NOT NULL, 
gender text NOT NULL,
age ineger NOT NULL);""")
insert_student=("INSERT INTO students(id, name, gender, age)""VALUES(?,?,?,?)")
dese = (1,'zhangsan','male',18)
cursor.execute(insert_student, dese)
db.commit()
db.close()





