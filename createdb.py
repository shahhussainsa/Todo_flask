from app import db, app

# Create the application context
with app.app_context():
    db.create_all()
