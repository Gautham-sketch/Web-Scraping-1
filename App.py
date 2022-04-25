from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/vinee/OneDrive/Desktop/Python/C-127/Web_Scraping_Class/chromedriver_win32")
browser.get(start_url)
time.sleep(10)

def scraping_data():
    headers = ["Name","Distance","Mass","Radius"]
    star_data = []
    for i in range(0,1):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for tr in soup.find_all("tr"):
            td_tag = tr.find_all("td")
            list = []
            for index,td in enumerate(td_tag):
                if(index == 0):
                    list.append(td.contents[0])
            star_data.append(list)
    with open("Scarp.csv","w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerow(star_data)

scraping_data()