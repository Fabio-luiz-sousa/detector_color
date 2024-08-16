import sqlite3
import os

DB_NAME = 'infos.sqlite3'

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.close()
conn.close()