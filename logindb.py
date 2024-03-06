import sqlite3 as sql
try:
    #to use the sqlite module we start by creating a variable (object) to hold to the path of the folder
    with sql.connect("SQL database/login.db") as dbconnect:
        # this is used to malipualte(sql queries) tables ine  in database 
     dbCursor= dbconnect.cursor() # this is uesed to execute sql statment
except sql.OperationalError as e:
   print(f"connection failed: {e}") # raise sql error




