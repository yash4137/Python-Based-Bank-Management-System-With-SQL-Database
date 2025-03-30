import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="HrB123@$",
    database="bank_management"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            name VARCHAR(20) NOT NULL,
            age INTEGER NOT NULL,
            city VARCHAR(20) NOT NULL,
            balance INTEGER NOT NULL,
            account_no INTEGER NOT NULL,
            status BOOLEAN NOT NULL
        )
    ''')
    mydb.commit()

if __name__ == "__main__":
    createcustomertable()
