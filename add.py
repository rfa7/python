import sqlite3
from datetime import datetime

#def addDeveloper(name, joiningDate):
def addDeveloper(name):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS new_developers (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        joiningDate timestamp);'''

        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_create_table_query)

        # insert developer detail
        sqlite_insert_with_param = """INSERT INTO 'new_developers'
                                    ('name', 'joiningDate')
                                    VALUES(?,?);"""

        #data_tuple = (id, name, joiningDate)
        data_tuple = (name, datetime.now())
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Developer added succesfully \n")

        # get developer detail
        sqlite_select_query = """SELECT name, joiningDate from new_developers where id = last_insert_rowid();"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            developer = row[0]
            joining_Date = row[1]
            print(developer, " joined on", joining_Date)
            print("joining date type is", type(joining_Date))

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")

addDeveloper(input('Dev Name:'))
