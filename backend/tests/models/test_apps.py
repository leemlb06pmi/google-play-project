from api.models.apps import App
import pytest

@pytest.fixture
def create_app()->App:
    values = ['Digital Falak','TOOLS','4.7','3408','15M','"50,000+"','Free','0','Everyone','Tools',
              '"May 30, 2018"','2.1.1','4.1 and up']
    return App(values)

def test_app_instance():
    values = ['Digital Falak','TOOLS','4.7','3408','15M','"50,000+"','Free','0','Everyone','Tools',
              '"May 30, 2018"','2.1.1','4.1 and up']
    cols = ['id', 'app', 'category','rating','reviews','app_size',
            'installs', 'app_type', 'price', 'content_rating','genre',
            'last_updated', 'current_ver', 'android_ver']
    my_app = App(values)
    my_dict = dict(zip(cols, values))
    assert my_dict == my_app.__dict__
    assert isinstance(my_app, App)





