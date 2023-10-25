import requests
import os

NEWS_APIKEY = os.environ.get("NEWS_APIKEY")


class NewsApiClient:
    def __init__(self):
        self.n_parameters = {
            "country": "us",
            "q": "tesla",
            "apiKey": NEWS_APIKEY,
        }

        url = "https://newsapi.org/v2/top-headlines"
        self.n_response = requests.get(url, params=self.n_parameters)
        self.n_response.raise_for_status()
        self.n_data = self.n_response.json()

    def get_articles(self):
        title = self.n_data['articles'][0]['title']
        brief = self.n_data['articles'][0]['content']
        url = self.n_data['articles'][0]['url']
        info = [title, brief, url]
        return info
