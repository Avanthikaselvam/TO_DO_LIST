import logging
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger(__name__)

db = SQLAlchemy()

def init_db(app):
    db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
    if not db_uri and not app.config.get('TESTING'):
        raise RuntimeError("DATABASE_URL is not configured. Please set DATABASE_URL in your .env file.")

    db.init_app(app)
    if db_uri:
        with app.app_context():
            # Import models so SQLAlchemy creates tables
            from models import user, task, schedule, history
            try:
                db.create_all()
            except Exception as e:
                if app.config.get('TESTING'):
                    raise
                else:
                    logger.debug(f"Database table verification deferred: {e}")
