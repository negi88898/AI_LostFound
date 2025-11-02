from flask import Flask, render_template, request, redirect, session, url_for
import psycopg2
import os
import random
from datetime import date

app = Flask(__name__)
app.secret_key = "supersecret"

# 🧠 PostgreSQL Connection (Render)
def get_db_connection():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
    return conn

# 🏠 Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ➕ Report Found Item
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        desc = request.form['description']
        today = date.today()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Items (
                ItemID SERIAL PRIMARY KEY,
                Name VARCHAR(100),
                Category VARCHAR(100),
                Description TEXT,
                DateFound DATE
            )
        """)
        cursor.execute("INSERT INTO Items (Name, Category, Description, DateFound) VALUES (%s, %s, %s, %s)",
                       (name, category, desc, today))
        conn.commit()

        session['desc'] = desc
        session['item_name'] = name
        cursor.close()
        conn.close()
        return redirect('/ai_loading')

    return render_template('add_item.html')

# 🤖 AI Suggestion Logic
def ai_suggest_owner(description):
    desc = description.lower()
    if "book" in desc:
        return "Priya Sharma", 95.6
    elif "wallet" in desc:
        return "Rohit Verma", 97.3
    elif "bag" in desc:
        return "Ankit Negi", 94.2
    elif "watch" in desc:
        return "Sakshi Rawat", 96.1
    elif "phone" in desc:
        return "Rahul Singh", 98.4
    else:
        names = ["Riya Gupta", "Amit Singh", "Sneha Rawat", "Vikram Joshi", "Divya Mehta", "Karan Kapoor"]
        return random.choice(names), round(random.uniform(80, 99), 2)

# 🤖 AI Loading Page
@app.route('/ai_loading')
def ai_loading():
    desc = session.get('desc', '')
    item_name = session.get('item_name', '')
    owner, confidence = ai_suggest_owner(desc)
    return render_template('ai_loading.html', item=item_name, owner=owner, confidence=confidence)

# 🧾 Report Lost Item
@app.route('/report_lost', methods=['GET', 'POST'])
def report_lost():
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        contact = request.form['contact']
        lost_name = request.form['lost_name']
        lost_category = request.form['lost_category']
        lost_description = request.form['lost_description']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS LostItems (
                LostID SERIAL PRIMARY KEY,
                OwnerName VARCHAR(100),
                Contact VARCHAR(100),
                ItemName VARCHAR(100),
                Category VARCHAR(100),
                Description TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO LostItems (OwnerName, Contact, ItemName, Category, Description)
            VALUES (%s, %s, %s, %s, %s)
        """, (owner_name, contact, lost_name, lost_category, lost_description))
        conn.commit()
        cursor.close()
        conn.close()

        return render_template('lost_success.html', name=owner_name, item=lost_name)
    return render_template('report_lost.html')

# 📘 About Page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
