import mariadb
import sys

def test_db():
    try:
        conn = mariadb.connect(
            host="serverless-us-central1.sysp0000.db2.skysql.com",
            port=4000,
            ssl_verify_cert=True,
            user="dbpgf29754552",
            password="Lam2409@"
        )
        print("Kết nối thành công tới cơ sở dữ liệu MariaDB!")

        #con trỏ 
        cursor = conn.cursor()

        # Thực thi truy vấn
        cursor.execute("SELECT * FROM members ")
        result = cursor.fetchone()
        print(f"Kết nối thành công: {result[0]}")

        cursor.close()
        conn.close()
    except mariadb.Error as e:
        print(f"Lỗi kết nối: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_db()
