import pyodbc

config = dict(
    DRIVER='{FreeTDS}',
    server='10.200.7.42',
    database='Alla_Testy',
    UID='alla',
    PWD='Alla',
    PORT= '1433', 
    TDS_Version= '8'
   )

try:
    cnx = pyodbc.connect(**config)
    cursor = cnx.cursor()
    print("SUCCESS")
    sql = "SELECT TOP 10 [ID],[Mand],[TimeStamp] ,[SerialNum],[PCBNum],[OrderNum],[Result],[StationID],[rowguid] FROM [Alla_Testy].[dbo].[result]"
    print(sql)
    for row in cursor.execute(sql):
        print(row[6])
except Exception as e:
    print ("Error: " + str(e))

