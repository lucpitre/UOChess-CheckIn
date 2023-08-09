import sqlite3
import os.path
import datetime


#function to return 
def memberExists(id):
    conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')

    cursor = conn.execute('SELECT * FROM MEMBERS')
    
    for member in cursor:
        if(member[0] == id):
            conn.close()
            return True
    
    conn.close()
    return False

def addMember(id, name, firstYear):
    conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')

    if(memberExists(id)): #if member already exists, don't add
        conn.close()
        return False
    
    #SQL code to add new member
    query = '''INSERT INTO MEMBERS (ID,NAME,FIRST_YEAR,ACTIVE) 
               VALUES (''' + str(id) + ''',\'''' + name +  '''\',''' + str(firstYear) + ''',1);'''
    conn.execute(query)
    conn.commit()

    conn.close()
    return memberExists(id) #returns true if member added successfully

def addVisit(id):
    conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')
    
    #SQL code to add new member
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    query = '''INSERT INTO VISIT (ID,DAY) 
               VALUES (''' + str(id) + ''',\'''' + date +  '''\');'''
    conn.execute(query)
    conn.commit()

    conn.close()

def resetDBs(): #only for development testing to be removed
    conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')

    conn.execute('''DROP TABLE MEMBERS;''')
    conn.execute('''DROP TABLE VISIT;''')
    conn.execute('''DROP TABLE VISITS;''')

    conn.execute('''CREATE TABLE MEMBERS
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             FIRST_YEAR     INT,
             ACTIVE         BIT);''')

    conn.execute('''CREATE TABLE VISITS
             (ID            INT     NOT NULL,
             DAY            DATE    NOT NULL);''')
    
    conn.commit()

    conn.close()

addVisit(1)