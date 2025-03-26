from flask import Flask
from app.routes import pdf_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(pdf_routes)  # Register routes

if __name__ == "__main__":
    app.run(debug=True)
