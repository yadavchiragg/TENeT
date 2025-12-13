from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configure CORS to allow requests from frontend
CORS(app, origins=os.environ.get('CORS_ORIGINS', 'http://localhost:5173').split(','))

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
        'description': 'Telehealth Effectiveness and Necessity Tracker',
        'focus': 'Alaska telecommunications infrastructure',
        'version': '0.1.0'
    }), 200

if __name__ == '__main__':
    app.run(debug=os.environ.get('FLASK_DEBUG') == '1', host='0.0.0.0', port=5000)