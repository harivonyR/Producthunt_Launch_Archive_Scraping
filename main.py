from script.producthunt import scrape_launch_list, scrape_product_info
from utils.dates import build_dates
from utils.url import get_domain_strict
import pandas as pd
from tqdm import tqdm

""" 1. Set Year Archive To Scrape """
dates = build_dates(start_year=2013, end_year=2013)

URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"
results = []
urls=[]

""" Run Archive Scraping """
pbar = tqdm(dates)
for (y, m, d) in pbar:
    pbar.set_description(f"Scraping {d:02d}/{m:02d}/{y}")
    url = URL_TEMPLATE.format(year=y, month=f"{m}", day=f"{d}")
    results.extend(scrape_launch_list(url))

""" 2. Export Data """
df = pd.DataFrame(results)
df.to_csv("output/producthunt_archive_sample.csv",sep=",")


""" 3. Adding Product Info """
product_rows = []
for _, row in tqdm(df.iterrows(), total=df.shape[0]):
    info = scrape_product_info(row["product_url"])  # doit retourner dict
    enriched = {**row.to_dict(), **info}            # fusion
    product_rows.append(enriched)

df_enriched = pd.DataFrame(product_rows)
df_enriched.to_csv("output/producthunt_archive_product_info_sample.csv", sep=",", index=False)

""" 4. Adding Produt Domain Name """
df_enriched.domain = df_enriched["company_url"].apply(get_domain_strict)
df_enriched.to_csv("output/producthunt_archive_info_domain.csv")