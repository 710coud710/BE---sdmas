from flask import Blueprint, jsonify
import mariadb

auth_bp = Blueprint('auth_bp', __name__)

# API lấy danh sách thành viên
@auth_bp.route('/members', methods=['GET'])
def get_members():
    try:
        # Kết nối cơ sở dữ liệu
        conn = mariadb.connect(
            host="serverless-us-central1.sysp0000.db2.skysql.com",
            port=4000,
            user="dbpgf29754552",
            password="Lam2409@",
            database="sdmas_db",
            ssl_verify_cert=True
        )

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM members")  
        members = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify({"success": True, "data": members}), 200

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@auth_bp.route('/check_db', methods=['GET'])
def check_db_connection():
    try:
        conn = mariadb.connect(
            host="serverless-us-central1.sysp0000.db2.skysql.com",
            port=4000,
            user="dbpgf29754552",
            password="Lam2409@",
            database="sdmas_db",
            ssl_verify_cert=True
        )

        cursor = conn.cursor()
        cursor.execute('SELECT 1')
        cursor.close()
        conn.close()

        return jsonify({"success": True, "message": "Kết nối database thành công!"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
