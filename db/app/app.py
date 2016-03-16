from flask import Flask
from flask import render_template
from flask import request

import psycopg2
import psycopg2.extras
import sys

con = None

app = Flask(__name__)

try:
	#con = psycopg2.connect("dbname='test_DB' user='nakatsuka'")
	#cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
	#cursor.execute("SELECT * FROM kadai")
	#users = cursor.fetchmany(3)

	@app.route('/')
	def index():
		users=[]
		"""
		Return users and display with table format according to
		the GET parameter from the client
		"""
		con = psycopg2.connect("dbname='test_DB' user='nakatsuka'")
		cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
		
		args = request.args
		request_iterable = args.keys()
		#s="SELECT * FROM kadai"
		for i in request_iterable:
			if args.get(i) != '':
				if type(i)=='int':
					s="SELECT * FROM kadai WHERE {} = {}".format(i,args[i])
				else:
					s="SELECT * FROM kadai WHERE {} = '{}'".format(i,args[i])
				cursor.execute(s)
				users = cursor.fetchall()
		#cursor.execute(s)
		#users = cursor.fetchall()
		#print (args)
		# example of users
		"""
		users = [
		    {
		        'name': 'foo',
		        'bday': '1990/1/1',
		        'age': 123,
		        'state': 'WA'
		    },
		    {
		        'name': 'bar',
		        'bday': '1990/11/11',
		        'age': 10,
		        'state': 'CA'
		    }
		]
		"""
		return render_template("index.html", users=users)

except psycopg2.DatabaseError:
	#print 'Error %s' % e
	sys.exit(1)

finally:
	if con:
		con.close()

if __name__ == '__main__':
    app.run(host='10.24.2.146',port=8000,debug=True)
