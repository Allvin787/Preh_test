import pyodbc

host = "10.200.7.42"
database = "Alla_testy"
username = "alla"
password = "Alla"

print ("DB CONNECT ATTEMPT")
try:
    cs = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (host, username, password, database)
    cnxn = pyodbc.connect(cs)
    print ("SUCCESS")
except Exception as e:
    print ("Error: " + str(e))

