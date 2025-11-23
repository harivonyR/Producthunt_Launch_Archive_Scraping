from script.producthunt import scrape_launch_list
from tqdm import tqdm

result = []

url_template = "https://www.producthunt.com/leaderboard/daily/2025/{month}/{day}"

#for month in tqdm(range(1, 13), desc="Months", position=0):
for month in tqdm(range(1, 2), desc="Months", position=0):
    for day in tqdm(range(1, 32), desc=f"Days M{month:02d}", position=1, leave=False):
        
        url = url_template.format(
            month=f"{month:02d}",
            day=f"{day:02d}"
        )

        products_hunt = scrape_launch_list(url)
        result.extend(products_hunt)
