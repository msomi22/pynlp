

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092']) 

# Asynchronous by default
future = producer.send('test', b'this message was sent from peter') 

# Block for 'synchronous' sends
try:
    record_metadata = future.get(timeout=10)
except KafkaError:
    # Decide what to do if produce request failed...
    log.exception()
    pass

# Successful result returns assigned partition and offset
print 'topic: ',record_metadata.topic, ' , partition:' ,record_metadata.partition, ' , offset: ', record_metadata.offset
