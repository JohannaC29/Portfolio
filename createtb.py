from  logindb import *

"""dbCursor.execute("""
CREATE TABLE "loginNew"(               
"fname" TEXT,
"Lname" TEXT,
"email" TEXT,
"password" TEXT,
PRIMARY KEY("fname") 
)""")"""


# GP DATA 
""""dbCursor.execute("""
CREATE TABLE "GpBooking"(               
"bookingID" INTEGER NOT NULL UNIQUE,
"date" TEXT,
"time" TEXT,
"fullname" TEXT,
"email" TEXT,
"dr" TEXT,
"aditionalInfo" BLOB,
PRIMARY KEY("bookingID" AUTOINCREMENT) 
)""")"""


#MOT Data

dbCursor.execute("""
CREATE TABLE "MOTBooking"(               
"bookingID" INTEGER NOT NULL UNIQUE,
"fullname" TEXT,
"address" TEXT,
"postcode" TEXT,
"mobile" INTEGER,
"email" TEXT,
"additional" BLOB,
PRIMARY KEY("bookingID" AUTOINCREMENT) 
)""")

"""#SURGERY DATA
dbCursor.execute("""
CREATE TABLE "surgeryBooking"(               
"bookingID" INTEGER NOT NULL UNIQUE,
"date" INTERGER,
"time" INTERGER,
"fullname" TEXT,
"email" TEXT,
 "BEFORE/AFTER" TEXT,
"aditionalInfo" BLOB,
PRIMARY KEY("bookingID" AUTOINCREMENT) 
)""")""" 

dbCursor.execute("""
CREATE TABLE "MOTBooking"(               
"bookingID" INTEGER NOT NULL UNIQUE,
"fullname" TEXT,
"address" TEXT,
"postcode" TEXT,
"mobile" INTEGER,
"email" TEXT,
"additional" BLOB,
PRIMARY KEY("bookingID" AUTOINCREMENT) 
)""")