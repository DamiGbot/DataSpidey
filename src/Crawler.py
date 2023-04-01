import requests
from bs4 import BeautifulSoup
import time



def fetch_page(url: str, query: str = ''):
    try:
        full_url = url + query
        response: requests.Response = requests.get(full_url, timeout=10)
        if response.status_code == 200:
            return response.text;
    except requests.exceptions.RequestException as error:
        print(f"Error fetching page {url}: {error}")
    return None

def get_links(html: str):
    soup = BeautifulSoup(html, 'lxml')
    links = [link['href'] for link in soup.find_all("a") if link.has_attr('href') and link['href'].startswith("http")]

    return links

def get_data(html: str):
    soup = BeautifulSoup(html, 'lxml')
    data_output = [{'title': article.find('h2').text, 'url': article.find('a')['href']} for article in soup.find_all('article')]

    return data_output

visited_url = set()

def crawl_scrape(url, max_depth=3, depth = 0, delay = 1):
    if depth > max_depth or url in visited_url:
        return
    
    visited_url.add(url)
    html = fetch_page(url)
    if not html:
        return
    
    links = get_links(html)
    data = get_data(html)

    if data:
        print(data)

    for link in links:
        time.sleep(delay)
        crawl_scrape(link, max_depth, depth + 1)
