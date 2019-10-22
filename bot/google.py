import requests
from bs4 import BeautifulSoup


def search(query):
    url = f'https://www.google.com/search?query={query}'

    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    a = soup.find_all('div', attrs={'class': "kCrYT"})
    # print(a)
    result_list = list()
    #
    for l1 in a:
        links = l1.find_all('a')
        for k in links:
            if k.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}):
                result_list.append((k.get('href')[7:].split('&')[0],
                                   k.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).string))
    return result_list
