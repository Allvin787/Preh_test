import pyodbc
import random
import pytest

config = dict(
    DRIVER='{PostgreSQL}',
    server='10.200.7.42',
    DATABASE='Alla_testy',
    UID='alla',
    PWD='Alla',
    Trusted_connection='yes'
   )

cnx = pyodbc.connect(**config)
cursor = cnx.cursor()
