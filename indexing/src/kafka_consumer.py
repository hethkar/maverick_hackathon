from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import env
import sys

server_1 = env.kakfa_server_host_1 + ":" + str(env.kakfa_server_port_1)
server_2 = env.kakfa_server_host_2 + ":" + str(env.kakfa_server_port_2)
server_config = server_1 + "," + server_2
print(server_config)

conf = {'bootstrap.servers': server_config,
        'group.id': 'foo',
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

running = True

def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)

        while running:
            msg = consumer.poll(timeout=1.0)
            if msg is None: continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

def shutdown():
    running = False
    
def msg_process(msg):
    print('Received message: {}'.format(msg.value().decode('utf-8')))

if __name__ == "__main__":
    basic_consume_loop(consumer, [env.kakfa_topic_name])
