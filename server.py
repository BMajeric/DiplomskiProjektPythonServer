from flask import Flask, request, jsonify

app = Flask(__name__)

gps_data = {}

@app.route('/send', methods=['POST'])
def receive_data():
    global gps_data
    data = request.json
    gps_data = data
    print(f"Received data: {gps_data}")
    return jsonify({"message": "Data received successfully"}), 200

@app.route('/get', methods=['GET'])
def send_data():
    global gps_data
    return jsonify(gps_data), 200

if __name__ == '__main__':
    # Run the server on your local IP
    app.run(host='0.0.0.0', port=5000, debug=True)
