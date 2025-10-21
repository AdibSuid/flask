from flask import Flask

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for session/cart

from app import routes
