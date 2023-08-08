import sqlite3
import os.path

conn = sqlite3.connect(os.path.dirname(__file__) +'/../db/members.db')



def memberExists(id):
    cursor = conn.execute('SELECT * FROM MEMBERS')
    for member in cursor:
        if(member[0] == id):
            return True
    return False

def addMember(id, name, firstYear):
    if(memberExists(id)): #if member already exists, don't add
        return False
    
    #SQL code to add new member
    conn.execute('''INSERT INTO MEMBERS (ID,NAME,FIRST_YEAR,ACTIVE)
                    VALUES (''' + str(id) + ''',''' + name +  ''',''' + str(firstYear) + ''', 1);''')
    conn.commit()

    return memberExists(id) #returns true if member added successfully

def addVisit(id):
    return


#conn.execute('''INSERT INTO MEMBERS (ID,NAME,FIRST_YEAR,ACTIVE)
#                VALUES (8263817, 'Lucas Pitre', 2019, 1);''')

x = memberExists(8263817)
print(x)

conn.close()

### SQL commands to create tables###

#conn.execute('''CREATE TABLE MEMBERS
#         (ID INT PRIMARY KEY     NOT NULL,
#         NAME           TEXT    NOT NULL,
#         FIRST_YEAR     INT,
#         ACTIVE         BIT);''')

#conn.execute('''CREATE TABLE VISIT
#         (ID            INT     NOT NULL,
#         DAY            DATE    NOT NULL);''')