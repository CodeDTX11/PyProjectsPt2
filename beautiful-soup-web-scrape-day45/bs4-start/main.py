from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup_yc = BeautifulSoup(yc_web_page, "html.parser")

articles = soup_yc.select(selector=".titleline")
article_texts = []
article_links = []

# print(articles[0].getText())

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get("href")
    article_texts.append(text)
    article_links.append(link)


# article_upvotes = [int(score.getText().split()[0]) for score in soup_yc.find_all(name="span", class_="score")]
#
# index = article_upvotes.index(max(article_upvotes))

# print(article_texts[index])
print(article_texts)
# print(article_links[index])
print(article_links)
# print(article_upvotes[index])



# with open("website.html") as webfile:
#     contents = webfile.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# anchor_tags = soup.find_all(name="a")
#
# for tag in anchor_tags:
#     print(tag.get("href"))
