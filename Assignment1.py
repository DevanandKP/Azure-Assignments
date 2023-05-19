from flask import Flask, render_template
from azure.storage.blob import ContainerClient,BlobClient
import os

app = Flask(__name__)

def listfolders():
    res = []
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=devassignment;AccountKey=8YpOLSWDJegnOVlvZzuFpwShdoAPmZpc5Ws4PTz4w6R7sN4WCD+9JgNTs00YgQTxjNfmWVokZ5AE+ASthmNG3g==;EndpointSuffix=core.windows.net'
    blob_service_client = ContainerClient.from_connection_string(connect_str,container_name="assignment1")
    blob_list = blob_service_client.list_blobs()
    print(blob_service_client)
    print(blob_list)
    for blob in blob_list:
        temp = str(blob.name)
        fol, fil = temp.split('/')
        if fol not in res:
            res.append(fol)
        res.append(blob.name)
    print(res)
    return res


@app.route('/')
def home():
    objectlist = listfolders()
    return render_template('index.html', bucketlist=objectlist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug =True)