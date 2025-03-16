import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

elastic_server_host = os.environ.get('ELASTIC_SERVER_HOST')
elastic_server_port = os.environ.get('ELASTIC_SERVER_PORT')
opensearch_rest_username=os.environ.get('ELASTIC_USER_NAME')
opensearch_rest_password=os.environ.get('ELASTIC_USER_PASS')

if elastic_server_host == None:
    elastic_server_host = "localhost"
    
if elastic_server_port == None:
    elastic_server_port = 9200
    
if opensearch_rest_username == None:
    opensearch_rest_username = "admin"
    
if opensearch_rest_password == None:
    opensearch_rest_password = "R06ust@09"

    