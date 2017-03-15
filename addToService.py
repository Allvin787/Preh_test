import pyodbc

config = dict(
    DRIVER='{/usr/local/lib/libtdsodbc.so}',
    server='mssql',
    database="Alla_testy",
    username="alla",
    password="Alla",
    Trusted_connection='yes'
   )

try:
    cnx = pyodbc.connect(**config)
    cursor = cnx.cursor()
    print("SUCCESS")
    sql = "SELECT * FROM [MODI_Technisat].[dbo].[TechnisatResults] where SnrBoard1='017220000023'"
    print(sql)
    for row in cursor.execute(sql):
        print(row[6])
except Exception as e:
    print ("Error: " + str(e))

