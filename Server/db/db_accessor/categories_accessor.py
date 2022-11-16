import db_accessor.main_db_accessor as q
create_categories_table = f"""
    CREATE TABLE IF NOT EXISTS categories(
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255),
        PRIMARY KEY(id, name)
        );
    """
 
 
def query_insert_into_categories(name):
    return f"""
            INSERT INTO categories VALUES
            (null, '{name}')
            """

def add_category(connection,name):
    query = query_insert_into_categories(name)
    q.execute_query(connection,query)    
    
def init_categories_table(connection, categories):
    for categor in categories:
        name = categor["name"]
        add_category(connection,name)
    print("initialized categories table successfully")
    
    
def get_category_name(connection, categoryId):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    SELECT DISTINCT name
                    FROM categories AS c 
                    WHERE c.id = '{categoryId}'
                    """
            cursor.execute(query)
            result = cursor.fetchall()
            return [e["name"] for e in result]
    except Exception as e:
        print(e)
 