from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime
import time


def moneycontrol(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    for a in soup.select('li.clearfix'):
        tag = a.find('a')
        dates.append(datetime.strptime(a.find('span').get_text(), '%B %d, %Y %H:%M %p IST'))
        links.append(tag.get('href'))
        titles.append(tag.get('title'))


def et_industry(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    featured = soup.find('div', 'featured')
    times = featured.find_all('time', 'date-format')
    link = featured.find_all('a')

    # Feature story 1

    dates.append(datetime.strptime(times[0].get_text(), '%b %d, %Y, %H:%M %p IST'))
    titles.append(featured.find('h2').get_text())
    links.append('https://economictimes.indiatimes.com' + link[0].get('href'))

    # Feature story 2

    dates.append(datetime.strptime(times[1].get_text(), '%b %d, %Y, %H:%M %p IST'))
    titles.append(featured.find('h3').get_text())
    links.append('https://economictimes.indiatimes.com' + link[2].get('href'))

    top = soup.find('ul', 'list1')
    for articles in top:
        tag = articles.find('a')
        dates.append(datetime.strptime(articles.find('time', 'date-format').get_text(), '%b %d, %Y, %H:%M %p IST'))
        titles.append(tag.get_text())
        links.append('https://economictimes.indiatimes.com' + tag.get('href'))


def et_markets(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    top = soup.find('ul', 'newsList')
    for articles in top:
        tag = articles.find('a')
        if tag is not None:
            if type(tag) is not int:
                dates.append(datetime.today())
                titles.append(tag.get_text())
                links.append('https://economictimes.indiatimes.com' + tag.get('href'))


def business_standard_companies(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    # Top story upper

    dates.append(datetime.today())
    titles.append(soup.find('div', 'top-section').find('h2').get_text().strip())
    links.append('https://www.business-standard.com' + soup.find('div', 'top-section').find('a').get('href'))

    # List of stories

    for article in soup.find_all('div', 'article'):
        dates.append(datetime.today())
        titles.append(article.find('h2').get_text().strip())
        links.append('https://www.business-standard.com' + article.find('a').get('href').strip())


def business_standard_markets(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    # Top story upper

    dates.append(datetime.today())
    titles.append(soup.find('div', 'top-section').find('h2').get_text().strip())
    links.append('https://www.business-standard.com' + soup.find('div', 'top-section').find('a').get('href'))

    # List of stories

    for article in soup.find_all('div', 'article'):
        dates.append(datetime.today())
        titles.append(article.find('h2').get_text().strip())
        links.append('https://www.business-standard.com' + article.find('a').get('href').strip())


def save_csv():
    try:
        df = pd.read_csv('data/Combined/stocks.csv')

        old_links = df['Link'].to_list()
        old_dates = df['Time'].to_list()
        old_titles = df['Title'].to_list()

        for i in range(len(links)):
            if links[i] not in old_links:
                old_links.append(links[i])
                old_dates.append(dates[i])
                old_titles.append(titles[i])
            # else:
            #     print(links[i])

        df = pd.DataFrame({'Time': old_dates, 'Title': old_titles, 'Link': old_links})

    except:

        df = pd.DataFrame({'Time': dates, 'Title': titles, 'Link': links})

    df.to_csv('data/Combined/stocks.csv')
    # df.to_json('data/Combined/stocks.json')


if __name__ == '__main__':
    time1 = time.time()

    links = []
    dates = []
    titles = []

    moneycontrol('https://www.moneycontrol.com/news/business/stocks')
    moneycontrol('https://www.moneycontrol.com/news/business/companies')
    et_industry('https://economictimes.indiatimes.com/industry')
    et_markets('https://economictimes.indiatimes.com/markets')
    business_standard_companies('https://www.business-standard.com/companies')
    business_standard_markets('https://www.business-standard.com/markets')

    save_csv()

    print(f'\nExecuted in {round(time.time() - time1, 2)} seconds.')
