import pymysql
from db_accessor import transactions_accessor
connection = pymysql.connect(
    host="localhost", 
    user="root",
    password="",
    db="bank",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_all_transactions_from_db():
    cursor = connection.cursor()
    cursor.execute("SELECT amount,vendor,categoryId,userId FROM transactions")
    return [e for e in cursor]


def add_transactions_to_db(amount, vendor, categoryId, userId):
    transactions_accessor.add_transaaction(connection, amount, vendor, categoryId, userId)
