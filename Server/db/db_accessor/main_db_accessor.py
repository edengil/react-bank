import json



       
def get_data_from_json():
    data_file = open("Server/db/data.json")
    data = json.load(data_file)
    data_file.close()
    return data

def execute_query(connection, query):
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(e)
 


