from fastapi import FastAPI, HTTPException
from utility import get_mssql_data,insert_data,update_data,delete_data
from schema import Item

# Create an instance of the FastAPI class and assign it to the variable 'app'
app = FastAPI()


# Define a GET endpoint at the path '/data'
@app.get("/data")
def read_data():
    # Call the 'get_mssql_data' function to fetch data from the database and store it in 'data'
    data = get_mssql_data()
    # Return a JSON response with the fetched data
    return {"data": data}


# Define a POST endpoint at the path '/data' for creating new data
@app.post("/create_data", response_model=Item)
def create_data(item: Item):
    # Call the 'insert_data' function to insert data into the database and get the inserted ID
    data = insert_data(item.name,item.age,item.designation, item.description)
    # Return a JSON response with the ID and data from the request
    return {"id": data, **item.dict()}

# Define a PUT endpoint at the path '/data/{item_id}' for updating existing data
@app.put("/update_data/{item_id}", response_model=Item)
def update_data_endpoint(item_id: int, item: Item):
    # Call the 'update_data' function to update data in the database based on 'item_id'
    updated_data = update_data(item_id, item.name, item.description)
    # If the item is not found, raise an HTTPException with a 404 status code
    if not updated_data:
        raise HTTPException(status_code=404, detail="Item not found")
    # Return a JSON response with the updated item's ID and data
    return {"id": item_id, **item.dict()}

# Define a DELETE endpoint at the path '/data/{item_id}' for deleting data
@app.delete("/delete_data/{item_id}", response_model=Item)
def delete_data_endpoint(item_id: int):
    # Call the 'delete_data' function to delete data from the database based on 'item_id'
    deleted_data = delete_data(item_id)
    # If the item is not found, raise an HTTPException with a 404 status code
    if not deleted_data:
        raise HTTPException(status_code=404, detail="Item not found")
    # Return a JSON response indicating that the data has been deleted successfully
    return {"message": "Data deleted successfully"}












# # Check if this script is being run as the main program
# if __name__ == "__main__":
#     # Import the 'uvicorn' library for running the FastAPI application
#     import uvicorn

#     # Run the FastAPI application on host '127.0.0.1' and port 8000
#     uvicorn.run(app, host="127.0.0.1", port=8000)

