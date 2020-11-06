import urllib.request
from bs4 import BeautifulSoup
import csv



class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        with open("google_news.csv", "w", newline='') as f:
            w = csv.writer(f)
            news_l = []

            for tag in sp.find_all("a"):
                url = tag.get("href")
                if url is None:
                    continue
                if "./articles" in url:
                    news_l.append(url)

            for i in news_l:
                w.writerow([i])
            print(news_l)

news = "https://news.google.com/"
Scraper(news).scrape()