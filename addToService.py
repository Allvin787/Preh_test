import pyodbc
import random
import pytest

config = dict(
    DRIVER='{ODBC Driver 13 for SQL Server}',
    server='10.200.7.42',
    DATABASE='Alla_testy',
    UID='POLEN\a.vinnikova',
    PWD='Preh1515',
    Trusted_connection='yes'
   )

cnx = pyodbc.connect(**config)
cursor = cnx.cursor()
