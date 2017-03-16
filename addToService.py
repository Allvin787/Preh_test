import pyodbc

config = dict(
    DRIVER='{FreeTDS}',
    server='10.200.7.42',
    database='MODI_Technisat',
    UID='alla',
    PWD='Alla',
    PORT= '1433', 
    TDS_Version= '8'
   )

try:
    cnx = pyodbc.connect(**config)
    cursor = cnx.cursor()
    print("SUCCESS")
    sql = "SELECT TOP 10 [ID],[SnrBoard1],[SnrBoard2],[BackBoard1],[BackBoard2],[PanelCode] ,[State],[TestStartTime] ,[TestEndTime] ,[TestProgramName] ,[FailElementID],[FailReason],[TechniSatFailMessage] ,[TesterID] FROM [MODI_Technisat].[dbo].[TechnisatResults]"
    print(sql)
    for row in cursor.execute(sql):
        print(row[6])
except Exception as e:
    print ("Error: " + str(e))

