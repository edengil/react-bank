# import main_db_accessor as q
from db.db_accessor import main_db_accessor as q

create_transactions_table = f"""
    CREATE TABLE IF NOT EXISTS transactions(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        amount INT,
        vendor VARCHAR(255),
        categoryId INT,
        userId INT,
        FOREIGN KEY(categoryId) REFERENCES categories(id),
        FOREIGN KEY(userId) REFERENCES users(id)
        );
    """


def query_insert_into_transactions(amount, vendor, categoryId, userId):
    return f"""
            INSERT INTO transactions VALUES
            (null, {amount}, '{vendor}', {categoryId}, {userId})
            """

def query_delete_transaction(transactionId):
    return f"""
                DELETE FROM transactions
                WHERE id = '{transactionId}'
                """

def add_transaaction(connection, amount, vendor, categoryId, userId):
    query = query_insert_into_transactions(amount, vendor, categoryId, userId)
    q.execute_query(connection, query)
    print("add transactions successfully")


def init_transactions_table(connection, transactions):
    for transaction in transactions:
        amount = transaction["amount"]
        vendor = transaction["vendor"]
        categoryId = transaction["categoryId"]
        userId = transaction["userId"]
        add_transaaction(connection, amount, vendor, categoryId, userId)
    print("initialized transactions table successfully")



def remove_transaction(connection,transactionId):
    query = query_delete_transaction(transactionId)
    q.execute_query(connection, query)
    