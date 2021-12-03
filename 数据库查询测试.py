import sqlite3

conn = sqlite3.connect('university.db')
c = conn.cursor()
a="李蝶红"
cursor = c.execute("""SELECT student_id, student_name, student_college
 From students
 WHERE student_name="%s" """%(a))

for row in cursor:
   print("ID = ", row[0]) 
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
conn.close()