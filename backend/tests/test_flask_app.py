import pytest
from api import create_app
from api.models import Review, App
from api.src.connection import *

@pytest.fixture(scope = 'module')
def app():
    flask_app = create_app('google_play_test', 'miles')

    with flask_app.app_context():
        app_values = ['Digital Falak','TOOLS','4.7','3408','15M','"50,000+"','Free','0','Everyone','Tools',
              '"May 30, 2018"','2.1.1','4.1 and up']
        app_values_2 = ['The Divine Feminine App: the DF App',
              'LIFESTYLE','5.0','8','6.7M',"1,000+",'Free','0','Everyone','Lifestyle',"May 16, 2016",'0.0.4','4.1 and up']
        app_cols = ['app', 'category','rating','reviews','app_size',
            'installs', 'app_type', 'price', 'content_rating','genre',
            'last_updated', 'current_ver', 'android_ver']
        
        review_values = ["10 Best Foods for You",'I like eat delicious food. That''s I''m cooking food myself, case ""10 Best Foods"" helps lot, also Best Before (Shelf Life)',
              "Positive","1.0","0.5333333333333333"]
        review_values_2 = ["11st","Horrible ID verification","Negative","-1.0","1.0"]
        review_cols = ['app','translated_review','sentiment','sentiment_polarity','sentiment_subjectivity']

        app_table = 'apps'
        review_table = 'app_reviews'

        conn = build_connection(flask_app.config['DATABASE'],flask_app.config['USER'])
        cursor = get_cursor(conn)
        add_records(cursor,app_table,app_cols,app_values)
        add_records(cursor,app_table,app_cols,app_values_2)
        add_records(cursor,review_table, review_cols, review_values)
        add_records(cursor,review_table, review_cols, review_values_2)
        conn.commit()
        close_conn(conn)
    yield flask_app

    with flask_app.app_context():
        close_conn(conn)
        conn = build_connection(flask_app.config['DATABASE'],flask_app.config['USER'])
        cursor = get_cursor(conn)
        drop_records(cursor, app_table)
        drop_records(cursor, review_table)
        close_conn(conn)

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_root(client):
    response = client.get('/')
    #breakpoint()
    assert b'A basic homepage.' in response.data

# def test_all_apps():
#         cursor = get_cursor(app.config['DATABASE'],app.config['USER'])
#         cursor.execute('SELECT * FROM apps order by app;')
#         results = cursor.fetchall()
#         return [App(result).__dict__ for result in results]
    
# def test_all_reviews():
#         conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['USER'])
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM app_reviews;')
#         results = cursor.fetchall()
#         return [Review(result).__dict__ for result in results]

