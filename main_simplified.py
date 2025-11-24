from script.producthunt import scrape_launch_list
from tqdm import tqdm
import calendar 

results = [] 

URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"

# Master progress bar for years
for year in tqdm(range(2013, 2014), desc="Years", position=0, leave=True):
    # Sub-bar for months
    for month in tqdm(range(1, 13), desc=f"Months {year}", position=1, leave=False):
            
        # Skip invalid months
        if year == 2013 and month < 11:
            continue

        number_of_days = calendar.monthrange(year, month)[1]

        # Sub-sub-bar for days
        for day in tqdm(range(1, number_of_days + 1), desc=f"Days M{month:02d}", position=2, leave=False):
            
            url = URL_TEMPLATE.format(
                year=year,
                month=f"{month:02d}",
                day=f"{day:02d}"
            )

            try:
                products_hunt = scrape_launch_list(url)
                results.extend(products_hunt)
            except Exception as e:
                tqdm.write(f"Error scraping {url}: {e}")  # <-- évite de casser tqdm
                continue

tqdm.write(f"\nScraping finished. Total collected products: {len(results)}")
