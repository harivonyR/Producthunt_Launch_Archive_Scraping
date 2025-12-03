# -*- coding: utf-8 -*-
"""
Created on Mon Dec  1 21:06:02 2025
@author: Lenovo
"""
import pandas as pd
from script.piloterr import crunchbase_info
from tqdm import tqdm
import json


if __name__ == "__main__":
    product_info = pd.read_csv("output/producthunt_archive_info_domain.csv", sep=";")
    
    results = []
    
    pbar = tqdm(product_info.head(5).iterrows(),total=5)
    for _, row in pbar:
        domain = row["domain"]

        if pd.notna(domain):
            pbar.set_description(f"Lookup Company Info {domain} ")
            data = crunchbase_info(domain=domain)
            merged = {**row.to_dict(), **data}
            results.append(merged)

    # Convert list → DataFrame → JSON
    df_out = pd.DataFrame(results)
    df_out.to_json("output/producthunt_crunchbase.json", orient="records", indent=4)
