import requests
from bs4 import BeautifulSoup
import json

def scrape_yverdon_news():
    url = "https://www.yverdonsport.ch/news-ys/"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Pour éviter les blocages
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    news_items = []
    # À adapter selon la structure HTML réelle du site
    articles = soup.select('div.entry-content')  # Exemple de sélecteur, à vérifier
    for article in articles:
        title_elem = article.select_one('h2.entry-title a')
        date_elem = article.select_one('time.entry-date')
        summary_elem = article.select_one('div.entry-summary p')
        
        title = title_elem.text.strip() if title_elem else ""
        date = date_elem['datetime'].split('T')[0] if date_elem else ""
        summary = summary_elem.text.strip() if summary_elem else ""
        link = title_elem['href'] if title_elem else ""
        
        news_items.append({
            "title": title,
            "date": date,
            "summary": summary,
            "link": link
        })
    
    return {"news": news_items}

if __name__ == "__main__":
    news_data = scrape_yverdon_news()
    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news_data, f, ensure_ascii=False, indent=2)
