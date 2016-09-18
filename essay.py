import sys
import requests
from bs4 import BeautifulSoup

urls_list = []


def start():
    url = "http://www.paulgraham.com/articles.html"
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    count = 0
    for post_detail in soup.findAll('a'):
        text = post_detail.text
        href = "http://www.paulgraham.com/" + post_detail.get('href')
        count = count + 1
        urls_list.append(href)
        print('{} {} >> {}'.format(count, text, href))
        print()


def get_essay(number):
    int_number = int(number)
    url = urls_list[int_number]
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for post_text in soup.findAll('td'):
        text = post_text.text
        print(text)

if __name__ == '__main__':
    start()
    get_essay(*sys.argv[1:])
