# Producthunt_Launch_Archive_Scraping
A fast and beginner-friendly ProductHunt archive scraping pipeline powered by the Piloterr API.
Generate date ranges, build dynamic URL templates, fetch clean HTML with the Piloterr Website Crawler, and extract structured product data for market intelligence, trend analysis, or dataset building.

## Use Case
* **Market intelligence** :  market gap analysis, leaderboards.
* **Emerging niche analysis** : growth signals, category pulse.
* **Investment opportunities** : spot promising startups early, evaluate traction, refine portfolio decisions.
* **Custom dashboards** : build your own product-insight or trend-tracking dashboards.

## Getting Started
### Clone the project
```
$ git clone https://github.com/harivonyR/Producthunt_Launch_Archive_Scraping
```

### Open the folder
```
$ cd Producthunt_Launch_Archive_Scraping
```

### Setup dependencies
```
$ pip install requests beautifulsoup4 pandas tqdm
```

### Copy paste the credential
```
$ copy credential.example.py credential.py
```

### Open `credential.py` and Paste the API key
```
x_api_key = "Paste Your API Key Here"
```
> Signup on [Piloterr Website](https://www.piloterr.com/) to get free credit.


## RUN the code
### Open  `main.py` and set year range to scrape
```
dates = build_dates(start_year=2013, end_year=2013)
```

### Run main
```
$ python main.py
```

## Output Sample
Output Sample :
```
  {
    'title': 'Product Hunt',
    'product_url': 'https://www.producthunt.com/products/producthunt',
    'source_url': 'https://www.producthunt.com/leaderboard/daily/2013/11/26',
    'description': 'Discover and geek out about cool new products',
    'tags': [
      'Tech'
    ],
    'comment': '9',
    'upvote': '146'
  }
```
## Teasing
Stay tuned, an upcoming project we will learn how to scrape company live info with Producthunt, Crunchbase and LinkedIn.

  