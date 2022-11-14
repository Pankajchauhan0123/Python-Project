import pymysql
db=None
cur=None

def connectdb():
    global db,cur
    db=pymysql.connect(host='localhost',user='root',password='',database='pankaj',port=3306)
    cur=db.cursor()

    #Disconnect Database

def disconnectdb():
    db.close()
    cur.close()

    #Login of user from Database

def insertrecord(name,mobile_no,acc_no):
    connectdb()
    query = f"insert into emp_data(name,mobile_no,acc_no) values('{name}',{mobile_no},{acc_no})"
    cur.execute(query)
    db.commit()
    disconnectdb()

    
    #Seacrching of records of each user

def searchrecord(id):
    connectdb()
    query=f'select * from emp_data where id={id}'
    try:
        cur.execute(query)
        result=cur.fetchone()
        print(f'ID: {result[0]}\nName: {result[1]}\nAcc_no: {result[2]}\nbranch: {result[3]}\nMobile no: {result[4]}')
    finally:
        disconnectdb()

    #Updating of Name,Mobile no

def updatename(id,name,mobile_no):
    connectdb()
    query = f'update emp_data set name="{name}",mobile_no="{mobile_no}" where id={id}'
    cur.execute(query)
    db.commit()
    disconnectDB()


    #Delete Records from database


def deleterecord(id):
    connectdb()
    query = f'delete from emp_data where id={id}'
    cur.execute(query)
    db.commit()
    disconnectdb()

    #Execution of Project line by line

while True:
    print('''Welcome To ITVEDANT Banking World:\n
            1. Search user Records
            2. Update User Records
            3. Insert Records
            4. Delete User Records
            0. Exit''')
    choice = int(input('Enter Your Choice: '))
    if choice==0:
        break
    elif choice==1:
        id = int(input('Provide the ID of the User:- '))
        searchrecord(id)
    elif choice==2:
        id = int(input('Provide the ID of the User:- '))
        print('''
                What do you want to update?
                a. Name
                b. Mobile No:
                ''')
        updatechoice = input('Enter Your Choice: ')
        if updatechoice in 'aA':
            name = input('Enter New Name: ')
            updatename(id,name)
        elif updatechoice in 'Bb':
            mobile_no = int(input('Enter New Mobile no: '))
            updatename(id,mobile_no)

    
    elif choice==3:
         name = input('Enter Name: ')
         mobile_no = int(input('Enter mobile_no: '))
         acc_no = int(input('Enter Your Acc_no :'))
         insertrecord(name,mobile_no,acc_no)
    elif choice==4:
        id = int(input('Provide the ID of the User : '))
        deleterecord(id)
    else:
        print('Enter Correct Value for Choice')