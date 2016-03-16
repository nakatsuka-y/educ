import psycopg2
import sys

con=None

dictlist=[]
d={}
s=""

try:
	con=psycopg2.connect("dbname='test_DB' user='nakatsuka'")

	cur=con.cursor()

	with open('data.csv') as f:
		data=f.readlines()
		for i in data:
			#i.lstrip('\n')
			l=i.strip('\n').split(',')
			#print(l)
			d={"name":l[0],"bday":l[1],"age":l[2],"state":l[3]}
			dictlist.append(d)
			#print(d)

	for l in dictlist:
		#print(l.get("name"))
		# c.f http://www.tutorialspoint.com/postgresql/postgresql_string_functions.htm
		s+="('{}','{}',{},'{}')".format(l.get("name").replace("\'","\'\'"),l.get("bday"),l.get("age"),l.get("state"))+','

	#print(s)
	#s.replace("\'","\'\'")
	#print("I'm lovin' it".replace("\'","\'\'"))
	#cur.execute('SELECT QUOTE_INDENT(E{})'.format(s))
	cur.execute('INSERT INTO kadai(name,bday,age,state) VALUES'+s.strip(','))
	con.commit()

except psycopg2.DatabaseError:
	if con:
		con.rollback()

	#print 'Error %s'%e
	sys.exit(1)

finally:
	if con:
		con.close()
