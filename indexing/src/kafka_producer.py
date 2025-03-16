from confluent_kafka import Producer
import socket
import env

server_1 = env.kakfa_server_host_1 + ":" + str(env.kakfa_server_port_1)
server_2 = env.kakfa_server_host_2 + ":" + str(env.kakfa_server_port_2)
server_config = server_1 + "," + server_2
print(server_config)

conf = {'bootstrap.servers': server_config,
        'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print('Message produced: {}'.format(msg.value().decode('utf-8')))

msgBody = "{\"applicationid\":\"1\",\"fname\":\"Sandeep\",\"lname\":\"Kumar\",\"address\":\"60 Prestatyn Close Stevenage SG1 2AJ\",\"compositevector\":\"Sandeep Kumar 60 Prestatyn Close Stevenage SG1 2AJ\"}"

producer.produce(env.kakfa_topic_name, key="key", value=msgBody, callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)