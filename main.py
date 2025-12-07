from script.producthunt import scrape_launch_list
from utils.dates import build_dates
import pandas as pd
from tqdm import tqdm

""" 1. ProductHunt - Archive Scraping """
# a - Set Archive Range to Scrape
dates = build_dates(start_year=2013, end_year=2013)

URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"
results = []
urls=[]

# b - Start Scraping
pbar = tqdm(dates)
for (y, m, d) in pbar:
    pbar.set_description(f"Scraping {d:02d}/{m:02d}/{y}")
    url = URL_TEMPLATE.format(year=y, month=f"{m}", day=f"{d}")
    results.extend(scrape_launch_list(url))
 
# c - Export Archive Data
df = pd.DataFrame(results)
df.to_csv("output/producthunt_archive_sample.csv",sep=",",index=False)






