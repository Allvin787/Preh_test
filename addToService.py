import pyodbc
import random
import pytest
import sys
sys.stdout=open('test.txt', 'w+')

config = dict(
    DRIVER='{FreeTDS}',
    server='10.200.7.42',
    database='MODI_Technisat',
    UID='alla',
    PWD='Alla',
    PORT= '1433', 
    TDS_Version= '8'
   )

cnx = pyodbc.connect(**config)
cursor = cnx.cursor()
rng = random.randint(1, 10)
a1 = (''.join([random.choice(list('QWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(rng)]))
a2 = (''.join([random.choice(list('123456789')) for x in range(rng)]))
a3 = (''.join([random.choice(list('#$%*)@!~+')) for x in range(random.randint(1, 15))]))
b = int(a2)+1
Sn1 = a1+a2
Sn2 = a1+str(b)
SnrBoard11 = "NoRead", " ", Sn1, a3
SnrBoard12 = "NoRead", " ", Sn2, a3
SnrBoard1 = random.choice(list(SnrBoard11))
SnrBoard2 = random.choice(list(SnrBoard12))
SnrBoard = SnrBoard1, SnrBoard2

print(SnrBoard1")
print(SnrBoard2")
print("#############")

#sys.stdout=open('test.txt', 'w')
#with open('\root\', 'a') as f:
    #f.write(SnrBoard1+"\n")
    #f.write(SnrBoard2+"\n")
    #f.write("#############" + "\n")

def initial_data(SnrBoard,SnrBoard2):

    cursor.execute("insert into [MODI_Technisat].[dbo].[TechnisatResults] ([SnrBoard1],[SnrBoard2],[BackBoard1],[BackBoard2],[PanelCode],[State],[TestStartTime],[TestEndTime],[TestProgramName]) values(?, ?,'005D01228870','005D01228869','B02FA20010761',2,GETDATE(), GETDATE(),'HLP4 M N CD LED')", SnrBoard)
    cnx.commit()

    cursor.execute("exec MODI_Technisat.dbo.ModiInspectionJob")
    cnx.commit()

    sql = "SELECT * FROM [MODI_Technisat].[dbo].[TechnisatResults] where SnrBoard1 = '"+SnrBoard1+"'"
    #print(sql)
    for row in cursor.execute(sql):
        return row[6]


def test_ModiInspectionJob_select_status_3():
    assert initial_data(SnrBoard, SnrBoard1) == '3'
    #print(SnrBoard1, SnrBoard2)




