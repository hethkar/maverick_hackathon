import os
from dotenv import load_dotenv
load_dotenv(verbose=True)

elastic_server_host = os.environ.get('ELASTIC_SERVER_HOST')
elastic_server_port = os.environ.get('ELASTIC_SERVER_PORT')
opensearch_rest_username=os.environ.get('ELASTIC_USER_NAME')
opensearch_rest_password=os.environ.get('ELASTIC_USER_PASS')

kakfa_server_host_1=os.environ.get('KAFKA_SERVER_HOST_1')
kakfa_server_port_1=os.environ.get('KAFKA_SERVER_PORT_1')
kakfa_server_host_2=os.environ.get('KAFKA_SERVER_HOST_2')
kakfa_server_port_2=os.environ.get('KAFKA_SERVER_PORT_2')

kakfa_topic_name=os.environ.get('KAFKA_TOPIC_NAME')

if elastic_server_host == None:
    elastic_server_host = "localhost"
    
if elastic_server_port == None:
    elastic_server_port = 9200
    
if opensearch_rest_username == None:
    opensearch_rest_username = "admin"
    
if opensearch_rest_password == None:
    opensearch_rest_password = "R06ust@09"

if kakfa_server_host_1 == None:
    kakfa_server_host_1 = "localhost"
    
if kakfa_server_port_1 == None:
    kakfa_server_port_1 = 29092
    
if kakfa_server_host_2 == None:
    kakfa_server_host_2 = "localhost"
    
if kakfa_server_port_2 == None:
    kakfa_server_port_2 = 39092

if kakfa_topic_name == None:
    kakfa_topic_name = "consumer_data"