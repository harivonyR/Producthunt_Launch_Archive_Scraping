# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 23:51:23 2025

@author: Lenovo
"""
from script.piloterr import website_crawler
from bs4 import BeautifulSoup
from utils.selector import find_with_all_classes, find_with_classes, get_one, get_attr, get_list


def scrape_launch_list(url):
    """ return list of product found in a roducthunt launch archive """
    html = website_crawler(url)
    
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    _class = ["isolate", "flex-row", "items-start"] # class list of items caracteristics
    
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
        
        if data["product_url"] != "https://www.producthunt.com/sponsor":
            result.append(data)
        
    return result

def scrape_product_info(product_url):
    html = website_crawler(product_url)
    soup = BeautifulSoup(html, "html.parser")
    
    data = {
        "product_name":       get_one(lambda: find_with_classes(soup, ["text-24","font-semibold","text-gray-900"])),
        "short_description":  get_one(lambda: find_with_classes(soup, ["text-18","text-gray-700"])),
        "company_url":        get_attr(lambda: find_with_classes(soup, ["transition-all","whitespace-nowrap"]), "href"),
        "tag":                get_list(lambda: find_with_all_classes(soup, ["text-14","text-tertiary","group-hover:brightness-25"]))
    }

    return data

"""
def scrape_product_info(product_url): 
    
    html = website_crawler(product_url) 
    soup = BeautifulSoup(html, "html.parser")
    
    product_class = ["text-24" ,"font-semibold" ,"text-gray-900"] 
    product_name = find_with_classes(soup,product_class).text 
    
    desc_class = ["text-18", "text-gray-700"]
    short_description = find_with_classes(soup,desc_class).text 
    
    company_url_class = ["transition-all","whitespace-nowrap"] 
    company_url = find_with_classes(soup,company_url_class).get("href") 
    
    tag_class = ["text-14", "text-tertiary", "group-hover:brightness-25"] 
    tag = [e.text for e in find_with_all_classes(soup, tag_class)] 
    
    data = { "product_name" : product_name, 
            "short_description" : short_description, 
            "company_url" : company_url, 
            "tag" : tag } 
    
    return data
"""
if __name__ == "__main__" :
    #url = "https://www.producthunt.com/leaderboard/yearly/2025"
    url = "https://www.producthunt.com/leaderboard/daily/2013/12/3"
    product_info = scrape_launch_list(url)
    
    #archive_url = "https://www.producthunt.com/leaderboard/daily/2025/1/8"
    #products_hunt = scrape_launch_list(archive_url)
    
    #product_url = "https://www.producthunt.com/products/coffeeme"
    #product_info = scrape_product_info(product_url)
    