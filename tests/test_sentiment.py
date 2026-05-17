from scripts.task2_nlp import get_sentiment

def test_positive():
    label, score = get_sentiment("I love this app")
    assert label == "positive"

def test_negative():
    label, score = get_sentiment("This app is terrible")
    assert label == "negative"