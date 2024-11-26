from pydantic import BaseModel
from typing import List, Dict, Self
from bs4 import BeautifulSoup
import re
import feedparser
from tqdm import tqdm
import requests
import time

feeds = [
     #   "https://www.dealnews.com/c142/Electronics/?rss=1",
     #   "https://www.dealnews.com/c39/Computers/?rss=1",
        "https://www.dealnews.com/c238/Automotive/?rss=1",
     #   "https://www.dealnews.com/f1912/Smart-Home/?rss=1",
     #   "https://www.dealnews.com/c196/Home-Garden/?rss=1",
       ]

def extract(html_snippet: str) -> str:

    if html_snippet.startswith("<") and html_snippet.endswith(">"):
        soup = BeautifulSoup(html_snippet, 'html.parser')
        snippet_div = soup.find('div', class_='snippet summary')
        
        if snippet_div:
            description = snippet_div.get_text(strip=True)
            description = BeautifulSoup(description, 'html.parser').get_text()
            description = re.sub('<[^<]+?>', '', description)
            result = description.strip()
        else:
            result = html_snippet
    else:
        result = html_snippet 
    return result.replace('\n', ' ')

class ScrapedDeal:

    category: str
    title: str
    summary: str
    url: str
    details: str
    features: str

    def __init__(self, entry: Dict[str, str]):

        self.title = entry['title']
        self.summary = extract(entry['summary'])
        self.url = entry['links'][0]['href']
        stuff = requests.get(self.url).content
        soup = BeautifulSoup(stuff, 'html.parser')
        content = soup.find('div', class_='content-section').get_text()
        content = content.replace('\nmore', '').replace('\n', ' ')
        if "Features" in content:
            self.details, self.features = content.split("Features")
        else:
            self.details = content
            self.features = ""

    def __repr__(self):

        return f"<{self.title}>"

    def describe(self):

        return f"Title: {self.title}\nDetails: {self.details.strip()}\nFeatures: {self.features.strip()}\nURL: {self.url}"

    @classmethod
    def fetch(cls, show_progress : bool = False) -> List[Self]:

        deals = []
        feed_iter = tqdm(feeds) if show_progress else feeds
        for feed_url in feed_iter:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:10]:
                deals.append(cls(entry))
                time.sleep(0.5)
        return deals

class Deal(BaseModel):

    product_description: str
    price: float
    url: str

class DealSelection(BaseModel):

    deals: List[Deal]

class Opportunity(BaseModel):

    deal: Deal
    estimate: float
    discount: float