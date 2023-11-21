from app import app, db

# Create the Flask app
application = app

# Create an application context before initializing the database
with application.app_context():
    # Initialize the database
    db.create_all()

# Run the application
if __name__ == '__main__':
    application.run(debug=True)
