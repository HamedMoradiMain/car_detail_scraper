import requests 
from bs4 import BeautifulSoup
import re 
class Scraper:
    titles = []
    def __init__(self):
        self.res = requests.get("https://caravanadvice.com.au/caravan-companies/")
        if self.res.status_code == "200":
            print("Connected!")
        else:
            print("Net Work Error!")
    def scraper(self):
        bs_obj = BeautifulSoup(self.res.text,features="html.parser")
        titles = bs_obj.find_all("article",{"class":re.compile(r"article-icon-entry av-iconlist-empty")})
        for title in titles:
            if title.get_text() not in self.titles:
                print(title.get_text())
                self.titles.append(title.get_text())
        with open("titles.txt","a",encoding="utf-8") as f:
            for item in self.titles:
                f.write(item)
                f.write("\n")
            f.close()
        print("Scraping has been done!")
if __name__ == "__main__":
    bot = Scraper()
    bot.scraper()