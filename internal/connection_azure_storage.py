import os
import base64
from azure.storage.blob import BlobServiceClient, ContentSettings
import imghdr


def upload_image(image, id_image, type_image):
    """
    upload image in azure storage
    :param id_image:
    :param type_image:
    :param image:
    :return:
    """
    try:
        connection_string = os.getenv('AZURE_STORAGE')

        base_64_data = image

        container = "smart-caring"

        azure_endpoint = "https://smartcaringstorage.blob.core.windows.net/"

        # Azure Storage Blob takes bytes-object
        coded = base64.decodebytes(base_64_data.encode())

        ext = imghdr.what(None, coded)

        if ext is None:
            if type_image == "video":
                ext = "mp4"

        file_name = id_image + "." + ext

        # Create a new instance of BlobServiceClient; we will use this to create a Blob Client
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        blob_client = blob_service_client.get_blob_client(container=container, blob=file_name)

        if ext == "jpeg":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="image/jpeg"))
        elif ext == "png":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="image/png"))
        elif ext == "jpg":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="image/jpg"))
        elif ext == "gif":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="image/gif"))
        elif ext == "bmp":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="image/bmp"))
        elif ext == "mp4":
            # Upload
            blob_client.upload_blob(coded, blob_type="BlockBlob", overwrite=True,
                                    content_settings=ContentSettings(content_type="video/mp4"))
        else:
            raise Exception("Invalid image format")

        # Get the object URL
        url = azure_endpoint + container + "/" + blob_client.get_blob_properties().name
        return url
    except Exception:
        return None
