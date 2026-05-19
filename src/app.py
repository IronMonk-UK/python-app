from flask import Flask, jsonify
import datetime, socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = socket.gethostname()
    return jsonify({
        'time': time, 
        'hostname': hostname
        }), 200

@app.route('/api/v1/health')
def health():
    response = 'OK'
    return jsonify({'status': response}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# '/api/v1/details'
# '/api/v1/health'