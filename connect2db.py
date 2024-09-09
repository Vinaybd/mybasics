import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="Vinay",password="2641",database="Vinay")


mycursor = mydb.cursor()


mycursor.execute("select * from student")

result=mycursor.fetchall()

for i in mycursor:
	print(i)
	show(i)