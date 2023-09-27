import wikipedia


def wiki(name="Manchester City", length=1):
    """Wikipedia fetcher function"""
    summary = wikipedia.summary(name, length)
    return summary
