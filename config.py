from urllib.parse import quote_plus

class Config:
    SECRET_KEY = 'bimatic'

    password = quote_plus("*2:D0XqFk6Gqkqg-1glY")
      
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+pymysql://dbpgf20945856:{password}@serverless-us-central1.sysp0000.db2.skysql.com:4005/sdmas_db'
        # f'mysql+pymysql://root:123@localhost:3306/sdmas_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
