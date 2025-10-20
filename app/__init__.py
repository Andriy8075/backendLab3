from flask import Flask
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # Basic database config (SQLite by default)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty@db:5432/db'
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Ensure models are imported so migrations can detect them
    from app.models.user import User  # noqa: F401

    # Import and register blueprints
    from app.routes.general import general_bp
    from app.routes.user import user_bp
    from app.routes.category import category_bp
    from app.routes.record import record_bp
    
    app.register_blueprint(general_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(record_bp)
    
    return app

# Create app instance for Flask CLI
app = create_app()
