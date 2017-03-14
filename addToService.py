import pyodbc
import random
import pytest

config = dict(
    DRIVER='{ODBC Driver 13 for SQL Server}',
    server='10.200.7.42',
    DATABASE='Alla_testy',
    UID='alla',
    PWD='Alla',
    Trusted_connection='yes'
   )

cnx = pyodbc.connect(**config)
cursor = cnx.cursor()
