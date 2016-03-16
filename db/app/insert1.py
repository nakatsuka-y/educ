import psycopg2
import sys

#database is already created

con=None

dictlist=[]
d={}

try:
	con=psycopg2.connect("dbname='test_DB' user='nakatsuka'")

	cur=con.cursor()

	with open('data.csv') as f:
		data=f.readlines()
		for i in data:
			#i.lstrip('\n')
			l=i.strip('\n').split(',')
			#print(l)
			s="INSERT INTO kadai (name,birth,age,state) VALUES (%s %d %d %s)"
			cur.execute(s,l)
			#d={"name":l[0],"birth":l[1],"age":l[2],"state":l[3]}
			#dictlist.append(d)
			#print(d)

#	for l in dictlist:
#		#print(l.get("name"))
#		s="INSERT INTO kadai VALUES ('{}',{},{},'{}')".format(l.get("name"),l.get("birth"),l.get("age"),l.get("state"))
#		cur.execute(s)
#
	con.commit()

except psycopg2.DatabaseError,e:
	if con:
		con.rollback()

	print 'Error %s'%e
	sys.exit(1)

finally:
	if con:
		con.close()
