from db.db_accessor import main_db_accessor as q


create_users_table = f"""
    CREATE TABLE IF NOT EXISTS users(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        balance INT,
        PRIMARY KEY(id, name)
        );
    """

def query_insert_into_users(name, balance):
    return f"""
            INSERT INTO users VALUES
            (null, '{name}', {balance})
            """
   
def init_users_table(connection, users):
    for user in users:
        name = user["name"]
        balance = user["balance"]
        query = query_insert_into_users(name, balance)
        q.execute_query(connection,query)
    print("initialized users table successfully")
    
    
def update_balance(connection,user_id, add):
    query = f"""
        UPDATE users
        SET balance = balance + {-1 * add}
        WHERE id={user_id}
    """
    q.execute_query(connection,query)