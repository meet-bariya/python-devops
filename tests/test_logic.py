from src.logic import wiki
def test_wiki():
    assert 'manchester city' in wiki().lower()