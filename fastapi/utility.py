# Import the pyodbc library for working with Microsoft SQL Server
import pyodbc
# Import database configuration parameters (SERVER, DATABASE, USERNAME, PASSWORD, DRIVER)
from db_config import SERVER, DATABASE, USERNAME, PASSWORD, DRIVER


# Define a function 'get_mssql_data' to fetch data from the MSSQL database
def get_mssql_data():
    # Create a connection string to connect to the database using the specified parameters
    connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    
    # Establish a database connection using the connection string
    connection = pyodbc.connect(connection_string)
    # Create a cursor to interact with the database
    cursor = connection.cursor()
    # Define an SQL query to retrieve data from the 'your_table' table
    query = "SELECT * FROM your_table"
    # Execute the query using the cursor
    cursor.execute(query)
    # Fetch the result set containing the data
    result = cursor.fetchall()
    # Close the database connection
    connection.close()
    # Return the fetched data
    return result

def insert_data(name, description):
    connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = "INSERT INTO your_table (name, description) VALUES (?, ?)"
    cursor.execute(query, name, description)
    connection.commit()
    connection.close()

def update_data(item_id, name, description):
    connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = "UPDATE your_table SET name = ?, description = ? WHERE id = ?"
    cursor.execute(query, name, description, item_id)
    connection.commit()
    connection.close()

def delete_data(item_id):
    connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    query = "DELETE FROM your_table WHERE id = ?"
    cursor.execute(query, item_id)
    connection.commit()
    connection.close()