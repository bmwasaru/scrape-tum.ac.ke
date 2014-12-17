from urllib import urlopen

from bs4 import BeautifulSoup

BASE_URL = "http://tum.ac.ke/"


def get_news_links():
    html = urlopen(BASE_URL).read()
    soup = BeautifulSoup(html, "lxml")
    link_data = soup.select(".text_descr")
    print link_data

if __name__ == '__main__':
    get_news_links()
