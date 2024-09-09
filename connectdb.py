import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='Vinay',password='2641',database="telusuko")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

result=mycursor.fetchone()

for i in mycursor:
	print(i)