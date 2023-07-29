import mysql.connector

i = 1

if (i == 0):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    )
    cursor = mydb.cursor()

    cursor.execute("CREATE DATABASE new_schema")
    str = 'CREATE TABLE `new_schema`.`db` (`roll` INT NOT NULL,`first_name` VARCHAR(45) NULL,`last_name` VARCHAR(45) NULL,`present` INT NULL,`timesofattendance` TIMESTAMP NULL,PRIMARY KEY (`roll`),UNIQUE INDEX `roll_UNIQUE` (`roll` ASC) VISIBLE);'
    cursor.execute(str)
else:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "new_schema"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM new_schema.db;")
    for x in cursor:
        print(x)
# print(cursor)