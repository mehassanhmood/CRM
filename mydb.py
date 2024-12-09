# import mysql.connector
# dataBase = mysql.connector.connect(
#     host = "localhost",
#     user = "root"
#     passwd = "password"
# )
# prepare the cursor object:
# cursorObject = dataBase.cursor()

# Make a database:
# cursorObject.execute("CREATE DATABASE crmDb")
# print("All Done")

import sqlite3
connection = sqlite3.connect("crmDb.sqlite3")

# prepare cursor object:
# cursor = connection.cursor()

print("Data Base Made in sqlite!")
