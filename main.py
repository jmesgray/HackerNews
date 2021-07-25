import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get('https://news.ycombinator.com/news')  # getting the first page of the website
res2 = requests.get('https://news.ycombinator.com/news?p=2')  # getting the second page of the website
soup1 = BeautifulSoup(res1.text, 'html.parser')  # converting the first page's data into text to be used
soup2 = BeautifulSoup(res2.text, 'html.parser')  # doing the same for the second page's data

links1 = soup1.select('.storylink')  # selecting the links and subtext of pages 1 and 2 from Hacker News
subtext1 = soup1.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

both_links = links1 + links2  # grabbing the links of pages 1 and 2
both_subtext = subtext1 + subtext2  # grabbing the subtext of pages 1 and 2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)  # sorting the data according to votes


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):  # creating a condition that selects articles based upon votes
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})  # title, link, and votes are the output
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(both_links, both_subtext))  # utilizing the pretty print module
