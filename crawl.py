import sys
from bs4 import BeautifulSoup
import urllib.request
import requests
import re
import Computer
import json


class Computer:


    def __init__(self, name="", chip="", monitor="", origin=""):
        self.name = name
        self.chip = chip
        self.monitor = monitor
        self.origin = origin

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_chip(self):
        return self.chip

    def set_chip(self, chip):
        self.chip = chip

    def get_monitor(self):
        return self.monitor

    def set_monitor(self, monitor):
        self.monitor = monitor

    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin

# function to extract html document from given url
def getHTMLdocument(url):

    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text

link = []
domain = "https://www.anphatpc.com.vn"
for i in range(1,4):
    url_to_scrape = 'https://www.anphatpc.com.vn/may-tinh-xach-tay-laptop.html?page=%i' %i
    html_document = getHTMLdocument(url_to_scrape)
    soup = BeautifulSoup(html_document, 'html.parser')
    divs = soup.find_all("div", {"class": "p-item js-p-item"})
    for div_name in divs:
        link.append(domain+div_name.find('a', {'class': 'p-img'}).get("href"))

for i in range(len(link)):
    html = getHTMLdocument(link[i])
    print(link[i])
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find("div", {"class": "popup-spec"})
    table = div.find("table")

    laptop = Computer()

    for line in table.findAll('tr'):
        for i in range(len(line.findAll('td'))):
            if line.findAll('td')[i].find("span").get_text().strip() == "Tên sản phẩm":
                try:
                    name = line.findAll('td')[i+1].get_text().strip()
                    laptop.set_name(name)
                except:
                    continue
            elif line.findAll('td')[i].find("span").get_text().strip() == "Bộ vi xử lý" or line.findAll('td')[i].find("span").get_text().strip() == "Công nghệ CPU":
                try:
                    chip = line.findAll('td')[i+1].get_text().strip()
                    laptop.set_chip(chip)
                except:
                    continue
            elif line.findAll('td')[i].find("span").get_text().strip() == "Màn hình" or line.findAll('td')[i].find("span").get_text().strip() == "Kích thước màn hình":
                try:
                    monitor = line.findAll('td')[i+1].get_text().strip()
                    laptop.set_monitor(monitor)
                except:
                    continue
            elif line.findAll('td')[i].find("span").get_text().strip() == "Xuất xứ" or line.findAll('td')[i].find("span").get_text().strip() == "Xuất Xứ":
                try:
                    origin = line.findAll('td')[i+1].get_text().strip()
                    laptop.set_origin(origin)
                except:
                    continue

    json_object = json.dumps(laptop.__dict__)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)