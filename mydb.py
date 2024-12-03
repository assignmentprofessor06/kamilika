import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = '0734719142liwindi',
	# auth_plugin='mysql_native_password'
	)

cusorObject = dataBase.cursor()
cusorObject.execute('CREATE DATABASE kamilikadb')

print("All done!")