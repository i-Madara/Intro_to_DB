import mysql.connector
from mysql.connector import Error

# Function to create a database
def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Change this if your MySQL server is on a different host
            user='root',       # Your MySQL username
            password='password'  # Your MySQL password
        )

        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:  # Catch MySQL-specific exceptions
        print(f"Error: {e}")
    
    finally:
        # Close the connection if it was successful
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to create the database
create_database()
