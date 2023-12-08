from flask import Flask, jsonify
import psycopg2

def create_app(database,user)->Flask:
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database,
        USER=user
    )

    @app.route('/')
    def homepage():
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM apps order by id limit 1;')
        return cursor.fetchall()
    
    return app