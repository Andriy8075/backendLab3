from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from app.routes.general import general_bp
    from app.routes.user import user_bp
    from app.routes.category import category_bp
    
    app.register_blueprint(general_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(category_bp)
    
    return app

# Create app instance for Flask CLI
app = create_app()
