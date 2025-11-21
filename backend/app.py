from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS to allow requests from frontend
CORS(app, origins=["http://localhost:5173"])

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to verify API is running"""
    return jsonify({
        'status': 'healthy',
        'message': 'TENeT API Gateway is running'
    }), 200

@app.route('/api/info', methods=['GET'])
def project_info():
    """Returns project information"""
    return jsonify({
        'project': 'TENeT',
        'description': 'Telecommunication Network Topology Visualization',
        'focus': 'Alaska telecommunications infrastructure',
        'version': '0.1.0'
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)