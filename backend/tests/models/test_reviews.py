from api.models.reviews import Review
import pytest

@pytest.fixture
def create_review()->Review:
    values = ['10 Best Foods for You',"I like eat delicious food. That's I'm cooking food myself, case ""10 Best Foods"" helps lot, also ""Best Before (Shelf Life)",
              'Positive','1.0','0.5333333333333333']
    return Review(values)

def test_review_instance():
    values = ['10 Best Foods for You',"I like eat delicious food. That's I'm cooking food myself, case ""10 Best Foods"" helps lot, also ""Best Before (Shelf Life)",
              'Positive','1.0','0.5333333333333333']
    cols = ['id','app','translated_review','sentiment','sentiment_polarity','sentiment_subjectivity']
    my_review = Review(values)
    my_dict = dict(zip(cols,values))
    assert my_dict == my_review.__dict__
    assert isinstance(my_review, Review)

    