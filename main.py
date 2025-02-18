from azure.storage.blob import BlobServiceClient,BlobClient,ContainerClient

connection_string = "https://github.com/naushadnandoliya/play-around-azure-storage-acc/security/secret-scanning/unblock-secret/2silkL5HgNxg9dvP9A0l09ZHk9Z"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

#blob_service_client.create_container("container1")
#blob_service_client.create_container("container2")
#blob_service_client.create_container("container3")

container_list = blob_service_client.list_containers()

for container_name in container_list:
    container_client = blob_service_client.get_container_client(container_name)
    for blob_name in container_client.list_blob_names():
        print(blob_name)
    