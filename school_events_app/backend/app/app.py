from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from dotenv import load_dotenv
import os
from . import database as db

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your_default_secret_key')

# Supabase configuration
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events')
def events():
    events = db.get_events()
    return jsonify(events)


if __name__ == '__main__':
    app.run(debug=True)
