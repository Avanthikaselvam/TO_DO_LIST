import os
from datetime import timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

# Load environment variables
load_dotenv()

from database.db import db, init_db
from routes import register_routes

def create_app(test_config=None):
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'ai-todo-secure-dev-secret-key-2026')
    
    # Load and normalize PostgreSQL DATABASE_URL
    database_url = os.getenv('DATABASE_URL', '').strip()
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

    if test_config:
        app.config.update(test_config)

    # Initialize DB & Models (verifies connection and creates tables if they don't exist)
    init_db(app)

    # Register Route Blueprints
    register_routes(app)

    # Main SPA Entry Point
    @app.route('/')
    def index():
        return render_template('index.html')

    # Health Check API
    @app.route('/api/health')
    def health():
        return jsonify({
            'status': 'healthy',
            'app': 'AI-Powered Personalized To-Do List Manager',
            'database': 'PostgreSQL' if 'postgresql' in str(app.config.get('SQLALCHEMY_DATABASE_URI', '')) else 'SQLite'
        }), 200

    return app

try:
    app = create_app()
except Exception:
    app = None

if __name__ == '__main__':
    if app is None:
        app = create_app()
    port = int(os.getenv('PORT', 5000))
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    print(f">> AI-Powered Personalized To-Do List Manager running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
