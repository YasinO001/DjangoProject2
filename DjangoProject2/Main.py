from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/realtime-energie', methods=['GET'])
def realtime_energie():
    # Simuleer API-data
    data = {
        "total_power_import_kwh": 150.5,
        "total_power_export_kwh": 50.3,
        "active_power_w": 1200
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)  # Zorg ervoor dat het draait op poort 5000
