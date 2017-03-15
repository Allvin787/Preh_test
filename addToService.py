import pyodbc

config = dict(
    DRIVER='{FreeTDS}',
    server='10.200.7.42',
    database='Alla_testy',
    UID='a.vinnikova',
    PWD='Preh1515',
    PORT= '1433', 
    TDS_Version= '8'
   )

try:
    cnx = pyodbc.connect(**config)
    cursor = cnx.cursor()
    print("SUCCESS")
    sql = "SELECT * FROM [Alla_Testy].[dbo].[result]"
    print(sql)
    for row in cursor.execute(sql):
        print(row[6])
except Exception as e:
    print ("Error: " + str(e))

