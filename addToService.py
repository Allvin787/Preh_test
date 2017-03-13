import pyodbc
import random
import pytest

config = dict(
    DRIVER='{SQL Server}',
    server='10.200.7.42',
    Trusted_connection='yes'
   )

cnx = pyodbc.connect(**config)
cursor = cnx.cursor()
