
from flask import Blueprint, request, jsonify

reminder_bp = Blueprint('reminder', __name__)
reminders = []

@reminder_bp.route('/reminders', methods=['GET', 'POST'])
def manage_reminders():
    if request.method == 'POST':
        reminders.append(request.json.get('reminder'))
    return jsonify(reminders)
