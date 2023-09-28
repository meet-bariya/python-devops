from src.wiki import summary,search

def test_summary():
    assert 'manchester city' in summary('Manchester_city').lower()

def test_search():
    assert 'Manchester' in search('Manchester_city')