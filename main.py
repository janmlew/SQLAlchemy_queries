# Imports
import psycopg2
from sqlalchemy import create_engine

# Engine setup
engine = create_engine("postgresql://postgres@/postgres")
conn = engine.connect()
conn.execute("commit")
conn.execute("create database test")
conn.close()
