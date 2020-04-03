import sqlite3
import datetime

def showdev():
    try:
        #sqliteConnection = sqlite3.connect('SQLite_Python.db')
        sqliteConnection = sqlite3.connect('SQLite_Python.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # get developer detail
        sqlite_select_query = """SELECT id, name, joiningDate from new_developers ORDER BY id;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            num = row[0]
            developer = row[1]
            joining_Date = row[2]
            print("Dev:", developer, " joined on", joining_Date)
            print("Id:", num)

        # get firs and last date in table
        # here SQLite is working on localtime area - but its a Python work so its hashed
        #min_date = """SELECT datetime(joiningDate, 'localtime') as dt from new_developers 
        #            where dt=(SELECT min(datetime(joiningDate, 'localtime')) from new_developers);"""
        #max_date = """SELECT datetime(joiningDate, 'localtime') as dt from new_developers 
        #            where dt=(SELECT max(datetime(joiningDate, 'localtime')) from new_developers);"""
        #.strftime("%Y-%m-%d %H:%M:%S")
        min_date = """SELECT joiningDate as dt from new_developers 
                    where dt=(SELECT min(joiningDate) from new_developers);"""
        max_date = """SELECT joiningDate as dt from new_developers 
                    where dt=(SELECT max(joiningDate) from new_developers);"""
        
        cursor.execute(min_date)
        rec1 = cursor.fetchone()
        cursor.execute(max_date)
        rec2 = cursor.fetchone()
        print(type(rec1[0]))
        print("Time is MAX:", rec2[0].strftime("%Y-%m-%d %H:%M:%S"))
        print("Time is MIN:", rec1[0].strftime("%Y-%m-%d %H:%M:%S"))
       
        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

showdev()
