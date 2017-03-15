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
    sql = "SELECT * FROM [MODI_Technisat].[dbo].[TechnisatResults] where SnrBoard1 = '"+SnrBoard1+"'"
    print(sql)
    for row in cursor.execute(sql):
        return row[6]
except Exception as e:
    print ("Error: " + str(e))

