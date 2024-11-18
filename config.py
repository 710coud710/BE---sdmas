# config.py
import os

class Config:
    # Kết nối đến SkySQL
    DB_HOST = os.getenv('DB_HOST', 'serverless-us-central1.sysp0000.db2.skysql.com')
    DB_PORT = os.getenv('DB_PORT', 4005)
    DB_USER = os.getenv('DB_USER', 'dbpgf20945856')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '*2:D0XqFk6Gqkqg-1glY')
    DB_NAME = os.getenv('DB_NAME', 'sdmas_db')
    DB_SSL_VERIFY = True
