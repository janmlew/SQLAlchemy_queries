# Imports
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy-utils import database_exists, create_database

# Engine setup
engine = create_engine("postgresql://postgres@/postgres")
conn = engine.connect()
conn.execute("commit")
conn.execute("create database test")
conn.close()
