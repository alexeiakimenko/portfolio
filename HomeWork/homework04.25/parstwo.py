import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    html = ''
    html2 = ''
    res = []
    res1 = []
    res_time = []
    res_header_news = []
    res_news = []
    

    s = 0

    def __init__(self, url, url2, path):
        self.url = url
        self.url2 = url2
        self.path = path

    def write(self, data):
        with open(self.path, 'a') as f:
            write = csv.writer(f, lineterminator='\r')
            write.writerow(data)

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def get_html2(self):
        req2 = requests.get(self.url2).text

        self.html2 = BeautifulSoup(req2, 'lxml')

    def parsing_url1(self):
        news = self.html.find_all('ul', class_='list_js')

        for item in news:

            time = item.find_all('div', class_='date')
            for i in time:
                self.res = []
                s = i.text.split()
                time_all = s[0][:5]
                s.pop(0)
                header = ''
                if len(s) > 1:
                    for el in range(len(s)):
                        header = header + s[el] + ' '

                else:
                    header = s[0]
                self.res.append(time_all)
                self.res.append(header)
                self.res.append(' ')
                self.res1.append(self.res)

            bigheader = item.find_all('a')
            for i in bigheader:
                bigheader_all = i.text.strip()

                self.res1[self.s][2] = bigheader_all
                self.s += 1

    def parsing_url2(self):
        news = self.html2.find_all('div', class_='news-item__description')

        header_news = self.html2.find_all('h4')
        time = self.html2.find_all('time')
        for t in time:
            self.res_time.append(t.text)

        for h in header_news:
            self.res_header_news.append(h.text)

        for n in news:
            self.res_news.append(n.text)

    def null(self):
        with open(self.path, 'w') as f:
            null = csv.writer(f)
            null.writerow('')

    def run(self):
        self.get_html()
        self.get_html2()
        self.null()
        self.parsing_url1()

        for i in range(len(self.res1)):
            self.write(self.res1[i])
        self.parsing_url2()
        for i in range(len(self.res_news)):
            self.write([self.res_time[i],self.res_header_news[i],self.res_news[i]])


def begin():
    pars = Parser('https://aif.ru/', 'https://tsargrad.tv/news', 'parsing_news.csv')
    pars.run()


begin()
