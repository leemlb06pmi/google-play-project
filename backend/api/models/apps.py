import api.src.orm as orm 
import api.models.reviews as rev  

class App:
    attributes = ['id', 'app', 'category','rating','reviews','app_size',
            'installs', 'app_type', 'price', 'content_rating','genre',
            'last_updated', 'current_ver', 'android_ver']
    
    # def __init__(self, values):
    #     self.__dict__ = dict(zip(self.cols,values))
    
    def reviews(self,cursor):
        cursor.execute("SELECT app,translated_review FROM app_reviews WHERE translated_review != 'nan' and app = %s",(self.app,))
        return orm.build_from_records(rev.Review(),cursor.fetchall())
        