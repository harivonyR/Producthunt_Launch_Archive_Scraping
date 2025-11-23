# -*- coding: utf-8 -*-
"""
Created on Sat Nov 22 22:49:19 2025

@author: Lenovo
"""

import requests
from credential import x_api_key
import json

def website_crawler(site_url):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    # decode double escape "\\" and inline "\n" 
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    
    # decode special character 
    clean_html = clean_html.encode('latin-1').decode('utf-8')
   
    return clean_html


def website_rendering(site_url, wait_in_seconds=5, scroll=0):
    """
    Render a website using Piloterr API.
    Supports optional scroll to bottom.
    """
    url = "https://piloterr.com/api/v2/website/rendering"
    querystring = {"query": site_url, "wait_in_seconds": str(wait_in_seconds)}
    headers = {"x-api-key": x_api_key}  # Assure-toi que x_api_key est défini globalement

    # we don't need to scroll
    if scroll == 0:
        response = requests.get(url, headers=headers, params=querystring)
    
    # with scrolling
    else:
        
        smooth_scroll = [
            {
                "type": "scroll",
                "x": 0,
                "y": 2000,                    # scrolling height : 2000 pixels down
                "duration": 3,                # scrolling duration
                "wait_time_s": 4              # wait time in second (s) before the next instruction
            }
        ]

        instruction = {
            "query": site_url,
            "wait_in_seconds": str(wait_in_seconds),
            "browser_instructions": smooth_scroll*scroll
        }

        response = requests.post(url, headers=headers, json=instruction)
        
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    
    # decode special character 
    clean_html = clean_html.encode('latin-1').decode('utf-8')
        
    return clean_html


if __name__ == "__main__":
    product_hunt_url = "https://www.producthunt.com/leaderboard/daily/2025/11/22"
    html = website_crawler(product_hunt_url)
