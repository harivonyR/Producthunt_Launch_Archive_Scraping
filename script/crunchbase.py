# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:06:02 2025

@author: Lenovo
"""
import pandas as pd
from script.producthunt import scrape_product_info

def reverse_company_search(company_url):
    
    
    return 

if __name__ == "__main__":
    product_url = "https://www.producthunt.com/products/taskade"
    product_info = scrape_product_info(product_url)
    
    company_url = "https://www.taskade.com/?ref=producthunt"
    products = pd.read_csv("output/producthunt_archive_sample.csv")

        