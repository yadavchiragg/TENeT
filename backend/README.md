# TENeT Backend

Flask-based API Gateway for TENeT project.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
python app.py
```

The API will be available at http://localhost:5000

## Available Endpoints

- `GET /api/health` - Health check
- `GET /api/info` - Project information