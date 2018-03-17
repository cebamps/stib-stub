import os
from time import time

from flask import Flask, jsonify, abort


app = Flask(__name__)

app.config['PORT'] = int(os.environ.get('STIBSTUB_PORT', 0)) or None

# Selected by hand; these form kind of a clockwise circular arc around
# Brussels.
stub_stops = [
    '1914',
    '5021',
    '5159',
    '2218',
    '8722',
    '4014',
    '1053',
    '4252',
    '2238',
    '3410',
]


@app.route('/token', methods=['POST'])
def token():
    return jsonify({
        "access_token": "deadbeef62ac1cbd2112556a813f11ae",
        "scope": "am_application_scope default",
        "token_type": "Bearer",
        "expires_in": 3600
    })


@app.route('/OperationMonitoring/1.0/VehiclePositionByLine/<lines_string>')
def vehicle_position(lines_string):
    lines = lines_string.split(',')
    # Only return data for the first requested line.
    line = lines[0]
    index = int(time()) // 20 % len(stub_stops)
    return jsonify({
        "lines": [{
            "lineId": line,
            "vehiclePositions": [
                {"pointId": pid} for pid in stub_stops[index:index+3]
            ]
        }]
    })


@app.route('/OperationMonitoring/1.0/PassingTimeByPoint/<lines_string>')
@app.route('/Files/2.0/Gtfs')
@app.route('/Files/2.0/Shapefiles')
def not_implemented(**kwargs):
    abort(501)


if __name__ == '__main__':
    app.run(port=app.config['PORT'])
