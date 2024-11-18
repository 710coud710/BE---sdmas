from flask import Blueprint, jsonify
from app.models.Members import Members  
from app import db 

auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/members', methods=['GET'])
def get_members():
    try:
        members = Members.query.all()  
        return jsonify({"success": True, "data": [member.serialize() for member in members]}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@auth_bp.route('/check_db', methods=['GET'])
def check_db_connection():
    try:
        db.session.execute('SELECT 1') 
        return jsonify({"success": True, "message": "Kết nối thành công!"}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
