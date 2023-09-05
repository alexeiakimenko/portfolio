import requests
from bs4 import BeautifulSoup
import csv


class Parser:
    html = ''
    res = []
    res1 = []
    s = 0

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def write(self, data):
        with open(self.path, 'a') as f:
            write = csv.writer(f, lineterminator='\r')
            write.writerow(data)

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
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

    def null(self):
        with open(self.path, 'w') as f:
            null = csv.writer(f)
            null.writerow('')

    def run(self):
        self.get_html()
        self.parsing()
        self.null()
        for i in range(len(self.res1)):
            self.write(self.res1[i])


def begin():
    pars = Parser('https://aif.ru/', 'parsing_block.csv')
    pars.run()


begin()
