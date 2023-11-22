from app import app, db

application = app

with application.app_context():
    # Initialize database
    db.create_all()

# Run application
if __name__ == '__main__':
    application.run(debug=True)
