from flask import Flask, jsonify, render_template
from api.models.apps import App
from api.models.reviews import Review
from api.src.connection import *
import psycopg2

def create_app(database,user)->Flask:
    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE=database,
        USER=user
    )
    
    @app.route('/')
    def index():
        return "A basic homepage."
    
    @app.route('/all_apps')
    def all_apps():
        cursor = get_cursor(app.config['DATABASE'],app.config['USER'])
        cursor.execute('SELECT * FROM apps order by app;')
        results = cursor.fetchall()
        return [App(result).__dict__ for result in results]
    
    @app.route('/all_reviews')
    def all_reviews():
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM app_reviews;')
        results = cursor.fetchall()
        return [Review(result).__dict__ for result in results]
    
    @app.route('/<application>/reviews')
    def specific_reviews(application):
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM app_reviews where app = %s and ;',(application,))
        results = cursor.fetchall()
        reviews = [Review(result).__dict__ for result in results]
        return render_template('app_reviews.html', results=reviews)
    
    return app