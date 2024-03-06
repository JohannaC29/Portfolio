from logindb import *


dbCursor.execute("""DROP TABLE GpBooking""")


dbCursor.execute("""
CREATE TABLE "GpBooking"(               
"bookingID" INTEGER NOT NULL UNIQUE,
"fullname" TEXT,
"address" TEXT,
"postcode" TEXT,
"mobile" INTEGER,
"email" TEXT,
"serviceOptions" TEXT,
"additional" BLOB,
PRIMARY KEY("bookingID" AUTOINCREMENT) 
)""")