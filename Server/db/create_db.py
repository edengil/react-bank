import pymysql
from db_accessor import main_db_accessor as q 
from db_accessor import categories_accessor,users_accessor,transactions_accessor


def create_db():
    connection = pymysql.connect(host="localhost", user="root", password="")
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            DROP DATABASE IF EXISTS bank;
            """)
            cursor.execute(f"""
            CREATE DATABASE IF NOT EXISTS bank
            """)
            print("db created successfully")
            connection.commit()
    except Exception as e:
        print(e)

def create_tables(connection):

    try:
        with connection.cursor() as cursor:
            cursor.execute(users_accessor.create_users_table)
            print("create users table successfully")
            cursor.execute(categories_accessor.create_categories_table)
            print("create categories table successfully")
            cursor.execute(transactions_accessor.create_transactions_table)
            print("create transactions table successfully")
            connection.commit()
    except Exception as e:
        print(e)






def init_tables(connection):
    data = q.get_data_from_json()
    users = data["users"]
    categories = data["categories"]
    transactions = data["transactions"]
    users_accessor.init_users_table(connection,users)
    categories_accessor.init_categories_table(connection,categories)
    transactions_accessor.init_transactions_table(connection,transactions)
    
    
if __name__ == "__main__":
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="bank",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
    )
    create_db()
    create_tables(connection)
    init_tables(connection)