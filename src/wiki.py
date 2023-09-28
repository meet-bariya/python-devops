import wikipedia


def summary(name="Manchester City", length=1):
    """Wikipedia fetcher function"""
    result = wikipedia.summary(name, length)
    return result


def search(name):
    """Search Wikipedia for Names"""
    results = wikipedia.search(name)
    return results
