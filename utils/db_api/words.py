import requests
from bs4 import BeautifulSoup
import csv

f = open('based_words.txt', 'r')
based_words = []
line = f.readlines()
size = len(line)


def get_based_words(a):
    for i in range(0, a):
        based_words.append(line[i].split(',')[0].rstrip())

    return based_words


get_based_words(size)

URL = 'https://wooordhunt.ru/word/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'accept': '*/*'}
HOST = 'https://wooordhunt.ru/word/'
FILE = 'translate.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    words = []
    words.append({
        'translate': soup.find('span', class_='t_inline_en').get_text()
    })
    # for item in items:
    # try:
    #    transcription = item.find_all('td')[1]
    # except KeyError:
    #    print('Нету транскрипции')
    # if transcription:
    #    transcription = transcription.get_text()
    # else:
    #    transcription = 'Транскрипция'
    # words.append(item.find_all('td')[1].get_text())
    # 'word': item.find('tr').find('td', class_='blue').get_text(strip=True),
    # 'transcription': item.find_all('td')[1].get_text()
    # 'type': item.find('p').get_text(),
    # 'definition': item.find('p', class_='indentwn').get_text().replace('1. ', ''),
    # print(words)
    return words


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Перевод'])
        for item in items:
            writer.writerow([item['translate']])


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        words = []
        for based_word in based_words:
            if based_word != 'actively' and based_word != 'founds' and based_word != 'neo' and based_word != 'non' \
                    and based_word != 'pre' and based_word != 'sperm' and based_word != 'statistically':
                print(f'Парсинг слова {based_word}...')
                html = get_html(HOST + '/' + based_word)
                get_content(html.text)
                words.extend(get_content(html.text))
        print(words)
        save_file(words, FILE)
        # print(f'Получено {len(words)} слов')

        # words = get_content(html.text)
    else:
        print('Error')


parse()
# print(based_words)
