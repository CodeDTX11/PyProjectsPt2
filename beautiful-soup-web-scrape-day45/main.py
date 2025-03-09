from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_html =response.text

soup = BeautifulSoup(web_html,"html.parser")

title_tags = soup.find_all(name="h3", class_="title")

titles = [tag.getText() for tag in title_tags]

titles = titles[::-1]

# print(titles[58])

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in titles:
        file.write(f"{movie}\n")