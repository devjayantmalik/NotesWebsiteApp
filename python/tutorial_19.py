# ==================================================
# ==================================================
#          Sqlite Database using Python
# ==================================================
# ==================================================


# ======================================
# Connecting or creating an sqlite database.
# Creating a cursor: a cursor allows to traverse through the info.
# Deleting a table if it exists via query
# Creating a table by executing query on db
# Inserting data in a table
# Retrieving information from a table by creating seperate function
# Update information in a table by creating seperate function
# Delete Individual row from a table.
# Reverse last transaction on database: rollback the transaction
# Alter a table previously created: such as adding columns to it.
# Use cursor and query to receive table info from a database file.
# Get no of rows in the database using query
# Get Sqlite version using query
# Using Dictionary Cursor: to retrieve records in a dictionary (use with statement)
# Backing up data to a file
# Closing an sqlite database connection


def print_db():
    try:
        # Retrieve the data from the database.
        querySelect = 'SELECT FName, LName, Age, Address, Salary, HireDate FROM Employees;'
        data = conn.execute(querySelect)
        conn.commit()

        for row in data:
            print(row)

    except sqlite3.OperationalError as ex:
        print("Retrieve Operation Failed.")
        print("Error:", ex)

def update_db():
    try:
        queryUpdate = "UPDATE Employees SET Address='123, Main St. Delhi' WHERE ID=1"
        conn.execute(queryUpdate)
        conn.commit()

    except sqlite3.OperationalError as ex:
        print(ex)
        print("Update Failed")
    except:
        print("Exception occured in update.")
    finally:
        print("You can use finally to close the database.")


# Importing module to use sqlite
import sqlite3

# Connecting to database
conn = sqlite3.connect('/home/hp/temp/test.db3')
print("Database Connected.")

# Creating a cursor
cur = conn.cursor()

# Deleting a table
queryDeleteTable = 'DROP TABLE IF EXISTS Employees;'
conn.execute(queryDeleteTable)
conn.commit()
print("Table Deleted.")

# Creating a table
queryCreateTable = r"CREATE TABLE Employees(" \
        r"ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," \
        r"FName TEXT NOT NULL," \
        r"LName TEXT NOT NULL," \
        r"Age INTEGER NOT NULL," \
        r"Address TEXT NOT NULL," \
        r"Salary REAL," \
        r"HireDate TEXT);"
try:

    # Executing the query
    conn.execute(queryCreateTable)
    conn.commit()
    print("Table Created.")
except sqlite3.OperationalError as ex:
    print("Table Creation failed.")
    print(ex)

# Inserting data in a table
queryInsertInTable = "INSERT INTO Employees" \
                     "(FName, LName, Age, Address, Salary, HireDate)" \
                     " VALUES" \
                     "('Jayant', 'Malik', 21, '123 DELHI', 103000, date('now'))"
# Cursor can also be used in place of conn
conn.execute(queryInsertInTable)
conn.commit()

# Retrieve information from a database.
print("="*30, "\nNew Information")
print_db()
print("="*30)

# Update Information in a database.
update_db()
print("="*30)
print("Updated Information")
print_db()
print("="*30)
'''
# Delete row from a table.
try:
    conn.execute("DELETE FROM Employees WHERE ID=1;")
    conn.commit()
    print("Employee with id 1 deleted successfully.")
except Exception as ex:
    print("Error occured while deleting an employee.")
    print(ex)

# Reverse the last transaction.
conn.rollback()
print("Rollback Completed.")
'''
# Add columns to a table.
queryAlterTable = "ALTER TABLE Employees ADD COLUMN 'Image' BLOB DEFAULT NULL;"
conn.execute(queryAlterTable)
conn.commit()
print("Table Altered.")

# Receive Tables from a database.
queryTableInfo = "PRAGMA TABLE_INFO(Employees)"
cur.execute(queryTableInfo)
colNames = [ record[1] for record in cur.fetchall()]
print(colNames)

# Get info realted to table
queryRecordCount = "SELECT COUNT(ID) FROM Employees"
cur.execute(queryRecordCount)
count = cur.fetchall()
print("No of Rows:", count[0][0])

# Get sqlite version
cur.execute("SELECT SQLITE_VERSION()")
version = cur.fetchone()
print("Sqlite version:", version)

# Using a dictionary Cursor
with conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Writing the query
    allEmps = cur.execute("SELECT * FROM Employees")
    rows = cur.fetchall()

    for row in rows:
        print(row['FName'], row['LName'])


# Backup data to a file
with open("/home/hp/temp/backup.sql", mode='w') as file:
    for line in conn.iterdump():
        file.write(line + "\n")
# Closing connection to database
conn.close()
print("Database Closed.")