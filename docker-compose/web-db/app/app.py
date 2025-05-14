from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DB']
        )
        return "Connected to MySQL successfully!"
    except Exception as e:
        return f"MySQL connection failed: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
