from sqlalchemy import create_engine

# Đường dẫn đến file chứng chỉ SSL
SSL_CERT = "certs/skysql_server_cert.pem"

# Chuỗi kết nối
DB_URI = (
    "mysql+pymysql://dbpgf20945856:*2:D0XqFk6Gqkqg-1glY"
    "@serverless-us-central1.sysp0000.db2.skysql.com:4005/sdmas_db"
    "?ssl_ca={}".format(SSL_CERT)
)

# Tạo engine SQLAlchemy
engine = create_engine(DB_URI)

# Kiểm tra kết nối
try:
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
        print("Kết nối thành công:", result.scalar())
except Exception as e:
    print("Lỗi kết nối:", e)
