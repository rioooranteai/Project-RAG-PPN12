import requests
import pandas as pd
import datetime

from selenium import webdriver
from bs4 import BeautifulSoup


base_url = "https://www.cnnindonesia.com/tag/ppn-12-persen?"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.1.26.76"

}

data = []

def get_article_content(article_url):
    try:
        response = requests.get(article_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        content_section = soup.find('div', class_='detail-text')
        if content_section:
            paragraphs = content_section.find_all('p')
            full_text = ' '.join([p.get_text(strip=True) for p in paragraphs])
            return full_text
        else:
            return "Konten tidak ditemukan."
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengambil konten dari {article_url} dengan error: {e}")
        return "Error saat mengambil konten."

def scrape_page(url): 
    try:
        driver = webdriver.Chrome()

        driver.get(url)

        driver.implicitly_wait(5)

        html = driver.page_source

        soup = BeautifulSoup(html, 'html.parser')

        articles = soup.find_all('article')
    
        for article in articles:
            h2_tag = article.find('h2')
            a_tags = article.find_all('a')
            if h2_tag:
                headline_text = h2_tag.get_text(strip=True)
                for a_tag in a_tags:
                    if a_tag.get('href') != "#":
                        link = a_tag.get('href')
                        print(f"Memproses artikel: {headline_text}")
                        content = get_article_content(link)
                        data.append({'title': headline_text,'content': content, 'link': link, 'timestamp': datetime.datetime.now()})

        driver.quit()
    except requests.exceptions.RequestException as e:
        print(f"Permintaan gagal untuk {url} dengan error: {e}")

for page in range(1, 12):  
    page_url = f"{base_url}page={page}"
    print(f"Scraping halaman: {page}")
    scrape_page(page_url)

if data:
    df_news = pd.DataFrame(data)
    df_news.to_csv('dataset_ppn-12-persen_cnn.csv', index=False)
    print("Data berita berhasil disimpan!")
else:
    print("Tidak ada data yang ditemukan.")

