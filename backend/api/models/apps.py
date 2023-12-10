class App:
    cols = ['id', 'app', 'category','rating','reviews','app_size',
            'installs', 'app_type', 'price', 'content_rating','genre',
            'last_updated', 'current_ver', 'android_ver']
    
    def __init__(self, values):
        self.__dict__ = dict(zip(self.cols,values))
        