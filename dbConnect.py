import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="system",
  database="BE",
  autocommit=True
)

cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE BE")

#cursor.execute("CREATE TABLE news (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,stock_name VARCHAR(50), sentiment VARCHAR(30) , prev_close FLOAT, pred_price FLOAT)")

cursor.execute('SELECT * FROM news')
for i in cursor:
  print(i)