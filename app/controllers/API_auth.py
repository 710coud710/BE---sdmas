from flask import Blueprint, jsonify
from app.models.Members import Members  # Import model Members
from app import db 

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/members', methods=['GET'])
def get_members():
    try:
        # Truy vấn tất cả các thành viên từ database
        members = Members.query.all()

        # Chuyển đổi kết quả sang dạng JSON
        return jsonify({"success": True, "data": [member.serialize() for member in members]}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@auth_bp.route('/check_db', methods=['GET'])
def check_db_connection():
    try:
        # Thực hiện một truy vấn đơn giản để kiểm tra kết nối
        db.session.execute('SELECT 1')
        return jsonify({"success": True, "message": "Kết nối database thành công!"}), 200
    except Exception as e:
        # Nếu có lỗi, trả về thông báo lỗi
        return jsonify({"success": False, "error": str(e)}), 500