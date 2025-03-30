from flask import Flask, send_from_directory
from api_routes import api_blueprint

# Initialize Flask app
app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(api_blueprint)

# Serve the frontend HTML file
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)