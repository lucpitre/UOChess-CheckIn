import sqlite3
import os.path

conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')



def memberExists(id):
    return False

def addMember():
    return

def addVisit():
    return



### SQL commands to create tables###

#conn.execute('''CREATE TABLE MEMBERS
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         FIRST_YEAR     INT,
#         ACTIVE         BIT);''')

#conn.execute('''CREATE TABLE VISIT
#         (ID            INT     NOT NULL,
#         DAY            DATE    NOT NULL);''')