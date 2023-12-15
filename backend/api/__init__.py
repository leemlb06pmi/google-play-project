from flask import Flask, jsonify, render_template
import api.models.apps as apps
import api.models.reviews as revs
import api.src.connection as connex
import api.src.orm as orm

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
        conn = connex.build_connection(app.config['DATABASE'],app.config['USER'])
        cursor = connex.get_cursor(conn)
        cursor.execute("SELECT * FROM apps order by app;")
        rets = orm.build_from_records(apps.App, cursor.fetchall())
        return [ret.__dict__ for ret in rets]
    
    @app.route('/all_reviews')
    def all_reviews():
        conn = connex.build_connection(app.config['DATABASE'],app.config['USER'])
        cursor = connex.get_cursor(conn)
        cursor.execute("SELECT * FROM app_reviews WHERE translated_review != 'nan';")
        rets = orm.build_from_records(revs.Review, cursor.fetchall())
        return [ret.__dict__ for ret in rets]
    
    # @app.route('/<application>/reviews')
    # def specific_reviews(application):
    #     conn = connex.build_connection(app.config['DATABASE'],app.config['USER'])
    #     cursor = connex.get_cursor(conn)
    #     cursor.execute("SELECT * FROM app_reviews where app = %s and ;",(application,))
    #     results = cursor.fetchall()
    #     reviews = [Review(result).__dict__ for result in results]
    #     return render_template('app_reviews.html', results=reviews)
    
    return app