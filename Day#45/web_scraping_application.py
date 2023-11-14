"""
This is a basic web scraping application.
As control in the robot.txt of the webpage, this is allowed as part of the webpage.
This is only an example of how web scraping works and is fully legal.
This application is used for only personal practice for the user. 
It cannot be used for other purposes.
"""

from bs4 import BeautifulSoup
import requests

#get the all webpage information
response = requests.get(url="https://news.ycombinator.com/news")
#turn a webpage into a text format
yc_web_page = response.text
#parsing the webpage 
soup = BeautifulSoup(yc_web_page, "html.parser")

#finding the all news titles.
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    article_text = article_tag.get_text()
    article_texts.append(article_text)
    article_link = article_tag.find(name="a").get("href")
    article_links.append(article_link)

#finding the votes of the news. 
article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]


#finding the highest number of votes on the news and getting its info.
num = max(article_upvote)
index_of_max = article_upvote.index(num)
max_article = article_texts[index_of_max + 1]
max_link = article_links[index_of_max + 1]

print(max_article)
print(max_link)















