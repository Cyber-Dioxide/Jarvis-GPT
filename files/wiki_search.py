import wikipedia

def search(query):
    results = wikipedia.summary(query , sentences = 2)
    return results

