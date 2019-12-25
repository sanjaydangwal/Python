import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "dangwal680")
print(mydb.connection_id)
curr = mydb.cursor()
# curr.execute("CREATE TABLE class(rollno integer(4),name varchar(20))")