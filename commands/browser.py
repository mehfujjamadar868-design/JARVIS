import webbrowser
# Used to open websites

from urllib.parse import quote
# Used to safely convert text into a URL


def open_website(website):
    # Opens the given website
    webbrowser.open(website)


def google_search(query):
    # Searches the given query on Google
    search_url = "https://www.google.com/search?q=" + quote(query)
    webbrowser.open(search_url)


def youtube_search(query):
    # Searches the given query on YouTube
    search_url = "https://www.youtube.com/results?search_query=" + quote(query)
    webbrowser.open(search_url)
