import requests
from bs4 import BeautifulSoup
import json
import os
import urllib.parse
import re

BASE_URL = "https://qclab.com.bd"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def scrape_qclab():
    print(f"Fetching {BASE_URL}...")
    response = requests.get(BASE_URL, headers=HEADERS, timeout=15)
    if response.status_code != 200:
        print(f"Failed to fetch site, status: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 1. Basic Meta Info
    title = soup.title.string.strip() if soup.title else "QCLAB | Testing, Inspection & Calibration Services in Bangladesh"
    meta_desc = ""
    meta_desc_tag = soup.find('meta', {'name': 'description'}) or soup.find('meta', {'property': 'og:description'})
    if meta_desc_tag:
        meta_desc = meta_desc_tag.get('content', '')
        
    meta_keywords = ""
    meta_kw_tag = soup.find('meta', {'name': 'keywords'})
    if meta_kw_tag:
        meta_keywords = meta_kw_tag.get('content', '')

    # Logo
    logo_img = soup.find('img', {'alt': re.compile(r'QC Lab|Logo', re.I)}) or soup.find('img', {'src': re.compile(r'logo', re.I)})
    logo_src = logo_img.get('src') if logo_img else ""
    if logo_src and not logo_src.startswith('http'):
        logo_src = urllib.parse.urljoin(BASE_URL, logo_src)
        
    print(f"Site Title: {title}")
    print(f"Logo URL: {logo_src}")

    # 2. Main Navigation & Mega Menu Categories
    navigation = []
    top_menu = soup.find('ul', class_='top-menu')
    if top_menu:
        for li in top_menu.find_all('li', recursive=False):
            a_tag = li.find('a')
            if a_tag:
                item_name = a_tag.text.strip()
                item_href = a_tag.get('href', '#')
                sub_items = []
                sub_ul = li.find('ul', class_='dropdown-menu')
                if sub_ul:
                    for sub_li in sub_ul.find_all('li'):
                        sub_a = sub_li.find('a')
                        if sub_a:
                            sub_items.append({'title': sub_a.text.strip(), 'href': sub_a.get('href', '#')})
                navigation.append({'name': item_name, 'href': item_href, 'children': sub_items})

    # Mega menu product categories
    categories = []
    header_lower = soup.find('div', class_='header-lower') or soup
    for li in header_lower.find_all('li', class_='mega-menu'):
        parent_a = li.find('a')
        cat_name = parent_a.text.strip() if parent_a else ""
        
        # Subgroups
        groups = []
        for col in li.find_all('div', class_=re.compile(r'col-md-')):
            h5 = col.find('h5')
            if h5:
                h5_a = h5.find('a')
                group_title = h5_a.text.strip() if h5_a else h5.text.strip()
                group_href = h5_a.get('href', '#') if h5_a else "#"
                
                sub_products = []
                ul = col.find('ul')
                if ul:
                    for item_li in ul.find_all('li'):
                        item_a = item_li.find('a')
                        if item_a:
                            sub_products.append({'title': item_a.text.strip(), 'href': item_a.get('href', '#')})
                groups.append({'group': group_title, 'href': group_href, 'items': sub_products})
        if cat_name:
            categories.append({'category': cat_name, 'groups': groups})

    # 3. Collect Images from Page
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', '')
        if src:
            full_src = urllib.parse.urljoin(BASE_URL, src)
            images.append({'src': full_src, 'alt': alt})

    # 4. Extract Text Content / Banners / Sections
    sections = []
    # Slider/Banner items
    banner_items = []
    for slide in soup.find_all(['div', 'li', 'section'], class_=re.compile(r'slide|banner|carousel', re.I)):
        text = slide.text.strip()
        img = slide.find('img')
        if text or img:
            banner_items.append({'text': text[:200], 'img': img.get('src') if img else ''})

    # Find service blocks, test items, feature boxes, counter boxes, about sections
    service_blocks = []
    for block in soup.find_all('div', class_=re.compile(r'service|feature|box|card|product', re.I)):
        title_tag = block.find(['h3', 'h4', 'h5', 'h2', 'a'])
        p_tag = block.find('p')
        img_tag = block.find('img')
        if title_tag and len(title_tag.text.strip()) > 3:
            service_blocks.append({
                'title': title_tag.text.strip(),
                'desc': p_tag.text.strip() if p_tag else '',
                'img': urllib.parse.urljoin(BASE_URL, img_tag['src']) if img_tag and img_tag.get('src') else ''
            })

    data = {
        'title': title,
        'meta_desc': meta_desc,
        'meta_keywords': meta_keywords,
        'logo': logo_src,
        'top_navigation': navigation,
        'categories': categories,
        'banner_items': banner_items,
        'service_blocks': service_blocks,
        'all_images': list({img['src']: img for img in images}.values())
    }

    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Scraping finished! Saved scraped_data.json with {len(categories)} categories and {len(images)} images.")

if __name__ == "__main__":
    scrape_qclab()
