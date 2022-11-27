import pymysql
import db.db_accessor.transactions_accessor as transactions_accessor
import db.db_accessor.users_accessor as users_accessor
userId = 1


# need to do open and close for every contction

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="bank",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_all_transactions_from_db():
    try:
        cursor = connection.cursor()
        cursor.execute(
            " id,amount,vendor,categoryId,userId FROM transactions")
        return [e for e in cursor]
    except Exception as error:
        raise error

def get_all_categories_from_db():
    cursor = connection.cursor()
    cursor.execute("SELECT id,name FROM categories")
    return [e for e in cursor]




def get_transaction_by_id(transactionId):
    try:
        connection.ping()
        with connection.cursor() as cursor:
            query = f"""
                    SELECT *
                    FROM transactions
                    WHERE id={transactionId}"""
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


def add_transactions_to_db(amount, vendor, categoryId, userId):
    users_accessor.update_balance(connection, userId, -1 * amount)
    transactions_accessor.add_transaaction(
        connection, amount, vendor, categoryId, userId)

# להקצות קונקשיין אחר לשתי הפעולות כי הם קורות אחת אחרי השניה


def get_user(user_id):
    try:
        connection.ping()
        with connection.cursor() as cursor:
            query = f"""
                    SELECT *
                    FROM users
                    WHERE id={user_id}"""

            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        
        
def remove_transaction(transactionId):
    query = get_transaction_by_id(transactionId)
    try:
        amount = query[0]["amount"]
    except Exception as e:
        raise MyError(e)
    users_accessor.update_balance(connection, userId, amount)
    transactions_accessor.remove_transaction(connection, transactionId)



# def remove_transaction(transactionId):
#     query = get_transaction_by_id(transactionId)
#     try:
#         amount = query[0]["amount"]
#         if amount >600000:
#             raise MyError
#     except Exception as e:
#         raise MyError(e)
#     users_accessor.update_balance(connection, userId, amount)
#     transactions_accessor.remove_transaction(connection, transactionId)


def get_categories_breakdown():
    try:
        connection.ping()
        with connection.cursor() as cursor:
            query = f"""
                SELECT c.name as category, CAST(SUM(t.amount) as DECIMAL(10,2)) as total
                FROM transactions AS t JOIN categories AS c
                ON c.id = t.categoryId
                GROUP BY t.categoryId"""
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)



class MyError(Exception):
    pass 