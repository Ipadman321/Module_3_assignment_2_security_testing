from flask import Flask, request, jsonify, render_template
import psycopg2
import psycopg2.extras

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="webdb",
    user="postgres",
    password="admin"
)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['GET'])
def get_users():
    try:
        cur.execute("SELECT * FROM users;")
        rows = cur.fetchall()
        users = [dict(row) for row in rows]
        return jsonify(users)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route('/users_gpa', methods=['GET'])
def get_users_gpa():
    try:
        cur.execute("SELECT * FROM user_gpa;")
        rows = cur.fetchall()
        users = [dict(row) for row in rows]
        return jsonify(users)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    try:
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
        conn.commit()
        return jsonify({"status": "user added"}), 201
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route('/add_user_gpa', methods=['POST'])
def add_user_gpa():
    data = request.get_json()
    try:
        cur.execute("INSERT INTO user_gpa (name, gpa) VALUES (%s, %s)", (data['name'], data['gpa']))
        conn.commit()
        return jsonify({"status": "user and gpa added"}), 201
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return jsonify({"error": "User already exists"}), 400
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/users_views', methods=['GET'])
def get_users_from_view():
    try:
        cur.execute("SELECT * FROM user_as_concat;")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    
@app.route('/user_gpa_views', methods=['GET'])
def get_user_gpa_from_view():
    try:
        cur.execute("SELECT * FROM user_gpa_as_concat;")
        rows = cur.fetchall()
        return jsonify(rows)
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
