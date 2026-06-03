from dotenv import load_dotenv
import os 
import mariadb

load_dotenv()

connection_db = mariadb.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASS"),
    database = os.getenv("DB_NAME"),
    port=3306
)
if connection_db:
    print('conectado')
