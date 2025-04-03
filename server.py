from flask import Flask, request, jsonify

app = Flask(__name__)

# Store sensor data & threshold
data_store = {
    "temperature": 0,
    "humidity": 0,
    "soil_moisture": 0,
    "threshold": 30  # Default threshold (can be updated from PC)
}

# 📡 Endpoint for sensors to send data
@app.route('/update', methods=['POST'])
def update_data():
    global data_store
    data = request.json
    data_store["temperature"] = data.get("temperature", 0)
    data_store["humidity"] = data.get("humidity", 0)
    data_store["soil_moisture"] = data.get("soil_moisture", 0)
    return jsonify({"status": "updated", "data": data_store})

# 📡 Endpoint for M5Core2 to fetch data
@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data_store)

# 📡 Endpoint to update threshold from PC
@app.route('/set_threshold', methods=['POST'])
def set_threshold():
    global data_store
    data_store["threshold"] = request.json.get("threshold", 30)
    return jsonify({"status": "Threshold updated", "threshold": data_store["threshold"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)