from azure.core.exceptions import ResourceNotFoundError
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import logging
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="get_resume_counter")
def get_resume_counter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        DATABASE_NAME = "AzureResume"
        CONTAINER_NAME = "Counter"
        client = CosmosClient.from_connection_string(os.getenv("CosmosDbConnectionSetting"))
        database = client.get_database_client(DATABASE_NAME)
        container = database.get_container_client(CONTAINER_NAME)
        item = container.read_item("1","1")
        logging.info(item["count"])
        item["count"] += 1
        container.upsert_item(item)
        

        return func.HttpResponse(f"This website has been visited: {item['count']} times!", status_code=200)
    
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"Error connecting to Cosmos DB: {e}")
        return func.HttpResponse(f"Failed to connect to Cosmos DB: {str(e)}", status_code=500)
