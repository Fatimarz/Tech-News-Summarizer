from bs4 import BeautifulSoup
import requests
import os, json
from urllib.parse import urljoin

def scrape():
    soup = requests.get('https://www.zdnet.com/topic/artificial-intelligence/')
    text = BeautifulSoup(soup.text, 'html.parser')

    start_url = 'https://www.zdnet.com/'
    article_link = text.select('.c-listingFiveStory_additional-items-container a')

    articles_data = []

    for idx, article in enumerate(article_link, start=1):
        title_tag = article.select_one('span')
        clean_title = title_tag.text.strip() if title_tag else f'No title {idx}'

        href = article.get('href')
        if not href:
            continue

        full_link = urljoin(start_url, href)

        more_soup = requests.get(full_link)
        more_text = BeautifulSoup(more_soup.text, 'html.parser')
        paras = more_text.select('.c-articleContent p')
        clean_text = "\n\n".join(p.text.strip() for p in paras if p.text.strip())

        articles_data.append({
            'Title': clean_title,
            'Article': clean_text,
            'Link': full_link
        })

    os.makedirs('data', exist_ok=True)
    file_name = 'data/scraped_articles.json'

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            old_data = json.load(f)
    else:
        old_data = []

    old_data.extend(articles_data)

    with open(file_name, 'w') as f:
        json.dump(old_data, f, indent=4)

if __name__ == "__main__":
    scrape()