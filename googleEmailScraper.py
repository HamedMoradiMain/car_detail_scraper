try:
    import os # os module 
    import sys # sys module
    from bs4 import BeautifulSoup
    from selenium import webdriver # webdriver
    from selenium.webdriver import Chrome # chrome 
    from selenium.webdriver.common.keys import Keys # keys
    from selenium.webdriver.common.by import By # by
    from selenium.webdriver.support.ui import WebDriverWait # webdriverwait
    from selenium.webdriver.support import expected_conditions # expected conditions
    from selenium.common.exceptions import TimeoutException # time out exception
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC # options
    from selenium.webdriver.common.proxy import Proxy, ProxyType
    import time # time module 
    import re
    import json
    import random
    import requests # request img from web
    import shutil # save img locally
    import numpy as np  
    print("all modules are loaded!")
except ModuleNotFoundError as e:
    print(e)
class CompanyDetails:
    final = []
    def __init__(self):
        with open("user_agent.txt","r") as f:
            user_agents = [agent for agent in f.readlines()]
            f.close()
    link = "https://www.google.com/search?q=3d+house+making+company+list+china+%28%22email%22%29+OR+%28%22contact%22%29+OR+%28%22phone%22%29&sxsrf=ALiCzsZpHr6gYsgr6QAnQ0UShgEgVMWq0w%3A1672430255079&ei=r0KvY5y-BNSakdUP6LmfgAI&ved=0ahUKEwjc0Y-akKL8AhVUTaQEHejcByAQ4dUDCBA&uact=5&oq=3d+house+making+company+list+china+%28%22email%22%29+OR+%28%22contact%22%29+OR+%28%22phone%22%29&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzoHCCMQrgIQJzoFCCEQoAFKBAhBGABKBAhGGABQAFjO6AFg6_wBaAtwAXgAgAG-BIgB1EeSAQgzLTIwLjEuM5gBAKABAcABAQ&sclient=gws-wiz-serp"
    def scraper(self):
        options = Options()
        options.add_argument(f'user-agent={random.choice(self.user_agents)}')
        driver = webdriver.Chrome(executable_path=r"chromedriver.exe",options=options)
        driver.set_window_size(500,700)
        driver.get(self.link)
        #WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'//*[@id="tsuid_9"]/div/div/div/a[1]')))
        while True:
            i = 200
            shops = []
            titles = []
            while i < 2000:
                driver.execute_script(f"window.scrollTo(0, {int(i)});")
                time.sleep(2)
                bs_obj = BeautifulSoup(driver.page_source,features="html.parser")
                titless = bs_obj.find_all("div",{"class":re.compile("CCgQ5 vCa9Yd QfkTvb MUxGbd v0nnCb")})
                infos = bs_obj.find_all("div",{"class":re.compile("kvH3mc BToiNc UK95Uc")})
                for info in infos:
                    shop = f"{info.get_text()}".strip()
                    if shop is not None:
                        if shop not in shops:
                            shops.append(f"{shop}")
                            print(shop)
                            print("\n")
                for title in titless:
                    title_ = f"{title.get_text()}".rstrip().lstrip()
                    if title_ not in titles:
                        if title_ is not None:
                            titles.append(f"{title_}")
                            print(title_)
                            print("\n")
                self.final.append([f"{shops}*!*!{titles}"])
                i = i + i
            try:
                next_page = driver.find_element(By.XPATH,'//*[@id="pnnext"]/span[2]')
                next_page.click()
            except:
                print(f"Scraping Done! \n Total data {len(shops)}")
                break
        print("File Saved Successfully!")
    def cleaner(self):
        final_data_emails = []
        final_data_insta_ids = []
        with open("data.txt","r",encoding="utf-8") as f:
            data = f"{f.readlines()}".split(":::::")
            shops = [shop for shop in data]
            for item in shops:
                emails = []
                numbers = []
                insta_ids = []
                #print(item)
                if item.lower().startswith("how"):
                    shops.remove(item)
                elif item.lower().startswith("where"):
                    shops.remove(item)
                insta_pattern = re.compile(r"@([a-zA-Z0-9]+)")
                pattern = re.compile(r"([a-zA-Z0-9]+)\@([a-zA-Z0-9]+)\.(com|org|edu)")
                matches = pattern.finditer(item)
                for email in matches:
                    if email.group() is not None:
                        if email.group() not in emails:
                                emails.append(email.group())
                inst_matches =insta_pattern.finditer(item)
                for item in inst_matches:
                    if item.group() is not None:
                        if item.group() not in insta_ids:
                            if item.group().lower().strip() != "@gmail":
                                if item.group().lower().strip() != "@the":
                                    if item.group().lower().strip() != "@hotmail":
                                        insta_ids.append(item.group())
                final_data_emails.append(emails)
                final_data_insta_ids.append(insta_ids)
            with open("insta.txt","w",encoding="utf-8") as f:
                for item in final_data_insta_ids:
                    for item1 in item:
                        f.write(item1)
                        f.write("\n") 
                f.close()
            with open("emails.txt","w",encoding="utf-8") as f:
                for item in final_data_emails:
                    for item1 in item:
                        f.write(item1)
                        f.write("\n") 
                f.close()              
    def data_clening(self):
        emails = []
        address = []
        numbers = []
        company_names = []
        with open("data.txt","r",encoding="utf-8") as f:
                raw_data = [data for data in f.readlines()]
                for item in raw_data:
                    item=item.split("*!*!")
                    print(item[1])
                    print("\n")

    def run(self):
        '''self.scraper()
        with open("data.txt","w",encoding="utf-8")as f:
            for item in self.final:
                f.write(f"{item}")
                f.write(":::::")
            f.close()'''
        self.data_clening()
if __name__ == "__main__":
    bot = SneakerScraper()
    bot.run()