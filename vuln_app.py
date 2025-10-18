from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import time

app = Flask(__name__)

USERS = {
    "alice": generate_password_hash("alice123"),
    "bob": generate_password_hash("password"),
    "admin": generate_password_hash("admin2025")
}

FAILED_ATTEMPTS = {}
LOCKOUT_THRESHOLD = 5
LOCKOUT_DURATION = 60

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get('username', '')
    password = data.get('password', '')
    rec = FAILED_ATTEMPTS.get(username)
    now = time.time()
    if rec:
        count, last_ts = rec
        if count >= LOCKOUT_THRESHOLD and (now - last_ts) < LOCKOUT_DURATION:
            return jsonify({"success": False, "error": "account_locked"}), 403
        elif (now - last_ts) >= LOCKOUT_DURATION:
            FAILED_ATTEMPTS.pop(username, None)
    pw_hash = USERS.get(username)
    if pw_hash and check_password_hash(pw_hash, password):
        FAILED_ATTEMPTS.pop(username, None)
        return jsonify({"success": True, "message": "login_success"}), 200
    else:
        count, _ = FAILED_ATTEMPTS.get(username, (0, 0))
        FAILED_ATTEMPTS[username] = (count + 1, now)
        return jsonify({"success": False, "error": "invalid_credentials"}), 401

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"users": list(USERS.keys()), "lockout_threshold": LOCKOUT_THRESHOLD, "lockout_duration": LOCKOUT_DURATION}), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
