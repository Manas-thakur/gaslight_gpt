from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf.csrf import CSRFProtect
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Change this in production
csrf = CSRFProtect(app)

def connect_db():
    conn = sqlite3.connect("mydb2.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        password = generate_password_hash(request.form.get('password'))

        if len(name) < 3:
            return jsonify({"success": False, "message": "❌ Name must be at least 3 characters!"})
        if not phone.isdigit() or len(phone) != 10:
            return jsonify({"success": False, "message": "❌ Phone must be 10 digits!"})
        if len(password) < 6:
            return jsonify({"success": False, "message": "❌ Password must be at least 6 characters!"})

        try:
            with connect_db() as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO users (name, phone, password) VALUES (?, ?, ?)",
                          (name, phone, password))
                conn.commit()
            return jsonify({"success": True, "message": "✅ Successfully Registered!"})
        except sqlite3.IntegrityError:
            return jsonify({"success": False, "message": "❌ Phone number already exists!"})
        
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')

        # Input validation
        if not phone or not password:
            return jsonify({"success": False, "message": "❌ All fields are required!"})
        if not phone.isdigit() or len(phone) != 10:
            return jsonify({"success": False, "message": "❌ Invalid phone number!"})

        try:
            with connect_db() as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM users WHERE phone = ?", (phone,))
                user = cur.fetchone()
                
                if user and check_password_hash(user['password'], password):
                    session['user_id'] = user['phone']
                    return jsonify({"success": True, "message": "✅ Login Successful!"})
                else:
                    return jsonify({"success": False, "message": "❌ Invalid credentials!"})
        except Exception as e:
            return jsonify({"success": False, "message": "❌ An error occurred. Please try again."})
        
    return render_template('signin.html')

@app.route('/main')
def main():
    if 'user_id' not in session:
        return redirect(url_for('signin'))
    return render_template('main.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    with connect_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                name TEXT NOT NULL,
                phone TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
    app.run(debug=True)