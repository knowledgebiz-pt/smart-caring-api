import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
    connect_str = os.getenv('AZURE_STORAGE')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    print(blob_service_client)

    # Quickstart code goes here

except Exception as ex:
    print('Exception:')
    print(ex)