from kafka import KafkaConsumer


def consumer1Init():
	consumer = KafkaConsumer('test')
	for message in consumer:
		processMsg(message) 
    
'''
ConsumerRecord(topic=u'test', partition=0, offset=93, timestamp=1532942913092, 
	timestamp_type=0, key=None, value='this message was sent from peter', 
	checksum=None, serialized_key_size=-1, serialized_value_size=32)

'''

def processMsg(message): 
	print message.timestamp, ' , ', message.value  



consumer1Init()



