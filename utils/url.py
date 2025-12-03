# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:04:08 2025
@author: Lenovo
"""

import re
import pandas as pd
import tldextract


def get_domain_alt(url: str) -> str:
    """  """
    pattern = r"(?:https?://)?([^/?#:]+)"
    match = re.search(pattern, str(url).lower())
    if not match:
        return ""

    host = match.group(1)

    # Remove common prefixes like www., m., blog., etc.
    prefixes = ("www.", "m.", "blog.", "app.", "site.", "web.")
    for p in prefixes:
        if host.startswith(p):
            host = host[len(p):]

    # Force extract main domain: last 2 parts (e.g. silvrback.com)
    parts = host.split(".")
    if len(parts) > 2:
        host = ".".join(parts[-2:])

    return host

def get_domain_strict(url: str) -> str:
    ext = tldextract.extract(url)
    return f"{ext.domain}.{ext.suffix}"


if __name__ == "__main__":
    company_info = pd.read_csv("output/producthunt_archive_product_info_sample.csv", sep=";")
    
    # Add domain column using vectorized apply
    #company_info["domain"] = company_info["company_url"].apply(get_domain_alt)
    company_info["domain"] = company_info["company_url"].apply(get_domain_alt)
    
    company_info.to_csv("output/producthunt_archive_info_domain.csv")
