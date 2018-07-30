

'''
pip install cassandra-driver
'''

from cassandra.cluster import Cluster

cluster = Cluster()
session = cluster.connect("nlpdb") 


def selectAll():
	rows = session.execute('SELECT * FROM rawdata')
	for data in rows:
		print data


def newRecord(data_id, topic, message, type, score):
	session.execute(""" INSERT INTO rawdata (data_id, topic, message, type, score) VALUES (%s, %s, %s, %s, %s) """, (data_id, topic, message,type,score)
)




#newRecord(3,'#LifeAtADC','joram: lets wait and see whether they will do something this month','sentiment','neg:0,pos:0,net:50')

print 'insert executing ....'
newRecord(3,'#LifeAtADC','joram: lets wait and see whether they will do something this month','sentiment','neg:0,pos:0,net:50')
print 'select executing ....'
selectAll()






