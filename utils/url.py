# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:04:08 2025
@author: Lenovo
"""

import re
import pandas as pd

def get_domain_alt(url: str) -> str:
    pattern = r"(?:https?://)?(?:www\.)?([^/?#:]+)"
    match = re.search(pattern, str(url).lower())
    return match.group(1) if match else ""

if __name__ == "__main__":
    company_info = pd.read_csv("output/producthunt_archive_product_info_sample.csv", sep=";")
    
    # Add domain column using vectorized apply
    company_info["domain"] = company_info["company_url"].apply(get_domain_alt)
    
    print(company_info)
