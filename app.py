# app.py
from flask import Flask, jsonify
import mariadb
import sys
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Kết nối với SkySQL
def get_db_connection():
    try:
        conn = mariadb.connect(
            host=app.config['DB_HOST'],
            port=app.config['DB_PORT'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            database=app.config['DB_NAME'], 
            ssl_verify_cert=app.config['DB_SSL_VERIFY']
        )
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

# Route kiểm tra kết nối cơ sở dữ liệu
@app.route('/db-test')
def db_test():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Thực hiện một truy vấn cơ bản
    cursor.execute("SELECT * FROM members")
    row = cursor.fetchone()
    
    conn.close()
    
    return jsonify(message=row[0])

@app.route('/members')
def get_members():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Truy vấn lấy tất cả dữ liệu từ bảng members
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()  # Lấy tất cả dòng dữ liệu

    # Tạo danh sách các dict chứa dữ liệu của mỗi member
    member_list = []
    for member in members:
        member_list.append({
            'id': member[0],
            'Member_id': member[1],
            'Password': member[2],
            'Club_id': member[3],
            'Full_name': member[4],
            'Birthday': member[5],
            'Address': member[6],
            'Member_image': member[7],
            'Gender': member[8],
            'Join_date': member[9],
            'Rank_id': member[10],
            'Received_rank': member[11],
            'Bio': member[12],
            'Created': member[13],
            'Updated': member[14]
        })

    conn.close()
    
    # Trả về dữ liệu dưới dạng JSON
    return jsonify(members=member_list)

if __name__ == "__main__":
    app.run(debug=True)
