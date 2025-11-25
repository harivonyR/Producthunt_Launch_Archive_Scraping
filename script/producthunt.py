# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 23:51:23 2025

@author: Lenovo
"""
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
    """ return list of product found in a roducthunt launch archive """
    html = website_crawler(url)
    
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    _class = ["isolate", "flex-row", "items-start"] # ckass list of items caracteristics
    
    result = []
    
    for item in find_with_all_classes(soup,_class):
        a = find_with_all_classes(item, ["text-14","font-semibold","leading-none"])

        data = {
            "title" : item.find("a").text,
            "product_url" : "https://www.producthunt.com"+item.find("a").get('href'),
            "source_url" : url,
            "description" : find_with_classes(item, ["text-16", "font-normal", "text-dark-gray", "text-secondary"]).text,
            "tags" : [i.text for i in find_with_all_classes(item, ["text-14","font-normal","text-dark-gray"])],
            "comment" : a[0].text if len(a) > 0 else None,
            "upvote" : a[1].text if len(a) > 1 else None
            }
        result.append(data)
        
    return result

if __name__ == "__main__" :
    #url = "https://www.producthunt.com/leaderboard/daily/2025/11/22"
    #url = "https://www.producthunt.com/leaderboard/yearly/2025"
    #url = "https://www.producthunt.com/leaderboard/daily/2025/1/1"
    url = "https://www.producthunt.com/leaderboard/daily/2025/1/8"
    products_hunt = scrape_launch_list(url)
