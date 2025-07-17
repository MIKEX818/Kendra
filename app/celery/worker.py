from app.web import create_app

# Create the Flask app instance
flask_app = create_app()

# Get the Celery app registered with Flask
celery_app = flask_app.extensions["celery"]

# Optional: for debugging/visibility, print Celery config
if __name__ == "__main__":
    print("Celery configuration:", celery_app.conf)
