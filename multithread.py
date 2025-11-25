# -*- coding: utf-8 -*-
import asyncio
from script.producthunt import scrape_launch_list
from utils.dates import build_dates
from tqdm.asyncio import tqdm_asyncio

dates = build_dates(start_year=2013, end_year=2013)[:10]
URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"

def build_url(y, m, d):
    return URL_TEMPLATE.format(
        year=y, 
        month=f"{m:02d}", 
        day=f"{d:02d}"
    )

async def main():
    tasks = []
    for (y, m, d) in dates:
        url = build_url(y, m, d)
        tasks.append(scrape_launch_list(url))
    return await tqdm_asyncio.gather(*tasks)


if __name__ == "__main__":
    results = asyncio.run(main())
    print(f"Scraping finished. Total collected: {len(results)} datasets")
