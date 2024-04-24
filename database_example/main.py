import pymysql
from pymongo import MongoClient
from config import MYSQL_CONFIG, MONGO_CONFIG

# MySQL connection
# def connect_to_mysql():
    # try:
    #     conn = pymysql.connect(
    #         host=MYSQL_CONFIG['host'],
    #         user=MYSQL_CONFIG['user'],
    #         password=MYSQL_CONFIG['password'],
    #         database=MYSQL_CONFIG['database']
    #     )
    #     print("Connected to MySQL database")
    #     return conn
    # except pymysql.Error as e:
    #     print(f"Error connecting to MySQL database: {e}")
    #     return None

# MongoDB connection
def connect_to_mongodb():
    try:
        client = MongoClient(
            host=MONGO_CONFIG['host'],
            port=MONGO_CONFIG['port']
        )
        db = client[MONGO_CONFIG['database']]
        collection = db[MONGO_CONFIG['collection']]
        print("Connected to MongoDB database")
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB database: {e}")
        return None

def main():
    # # Connect to MySQL
    # mysql_conn = connect_to_mysql()
    # if mysql_conn:
    #     # Create a table
    #     cursor = mysql_conn.cursor()
    #     cursor.execute("""
    #         CREATE TABLE IF NOT EXISTS users (
    #             id INT AUTO_INCREMENT PRIMARY KEY,
    #             name VARCHAR(255) NOT NULL,
    #             email VARCHAR(255) NOT NULL UNIQUE
    #         )
    #     """)
    #     mysql_conn.commit()
    #     cursor.close()
    #     mysql_conn.close()
    
    # Connect to MongoDB
    mongo_collection = connect_to_mongodb()
    if mongo_collection:
        # Insert a document
        document = {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
        result = mongo_collection.insert_one(document)
        print(f"Inserted document ID: {result.inserted_id}")

if __name__ == "__main__":
    main()
