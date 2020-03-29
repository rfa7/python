import sqlite3
import datetime

def showdev():
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        #sqliteConnection = sqlite3.connect('SQLite_Python.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # get developer detail
        sqlite_select_query = """SELECT id, name, datetime(joiningDate, 'localtime') from new_developers ORDER BY id;"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            num = row[0]
            developer = row[1]
            joining_Date = row[2]
            print("Dev:", developer, " joined on", joining_Date)
            print("Id:", num)

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

showdev()
