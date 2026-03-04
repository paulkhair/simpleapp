from flask import Flask, jsonify

# This name MUST be 'app' because your test is looking for 'from app.main import app'
app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "online",
        "asset_id": "VPP-UNIT-DE-01"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)