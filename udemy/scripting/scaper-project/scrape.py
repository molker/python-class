import requests
from bs4 import BeautifulSoup
import pprint
import sys

geturl = 'https://news.ycombinator.com/news'

# upgraded on top of the class version to allow
# for user to say how many pages to call


def decide_page_range(geturl):
    try:
        num_pages = int(input('How many pages should we scrape?\t'))
    except ValueError:
        print('Please provide a value')
        sys.exit()
    response = requests.get(geturl)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    if num_pages > 1:
        for i in range(num_pages):
            next_response = requests.get(geturl+'?p='+str(i))
            next_soup = BeautifulSoup(next_response.text, 'html.parser')
            links = links + next_soup.select('.storylink')
            subtext = subtext + next_soup.select('.storylink')
    return create_custom_hn(links, subtext)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            score = int(vote[0].getText().replace(' points', ''))
            if score > 99:
                hn.append({'title': title, 'link': href, 'votes': score})
    return sort_stories_by_votes(hn)


pprint.pprint(decide_page_range(geturl))
