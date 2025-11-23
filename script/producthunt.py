# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 23:51:23 2025

@author: Lenovo
"""

from urllib.parse import urlencode
from script.piloterr import website_crawler
from bs4 import BeautifulSoup

def find_with_all_classes(soup, classes):
    """ return all elements that contain all classes """
    return soup.find_all(
        lambda tag: tag.has_attr("class") and all(c in tag["class"] for c in classes)
    )

def find_with_classes(soup, classes):
    """ return first elements that contain all classes """
    return soup.find(
        lambda tag: tag.has_attr("class") and all(c in tag["class"] for c in classes)
    )

def scrape_launch_list(url):
    url = "https://www.producthunt.com/leaderboard/daily/2025/11/22"
    html = website_crawler(url)
    
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    _class = ["isolate", "flex-row", "items-start"]

    items = find_with_all_classes(soup,_class)
    
    item = items[0]
    title = item.find("a").text
    description = find_with_classes(item, ["text-16", "font-normal", "text-dark-gray", "text-secondary"]).text
    tags = [i.text for i in find_with_all_classes(item, ["text-14","font-normal","text-dark-gray"])]
    
    """
    results = []

    for item in soup.select('*[data-test-id="ad"]'):
        data = {
            "title": (item.select_one("a") or {}).get_text(strip=True) if item.select_one("a") else None,
            "description": (item.select_one("p.text-16.font-normal.text-dark-gray.text-secondary") or {}).get_text(strip=True)
        }
        results.append(data)

    return results
    """



if __name__ == "__main__" :
    url = "https://www.producthunt.com/leaderboard/daily/2025/11/22"
    products_hunt = scrape_launch_list(url)