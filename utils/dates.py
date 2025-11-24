# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:33:31 2025

@author: Lenovo
"""
import calendar
from datetime import date

# Build the list of dates to scrape (YYYY, MM, DD tuples)
def build_dates(start_year=2013, end_year=2013):
    dates = []
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            # exclude dates before 2013-11-01
            if y == 2013 and m < 11:
                continue
            days_in_month = calendar.monthrange(y, m)[1]
            for d in range(1, days_in_month + 1):
                dates.append((y, m, d))
    return dates

URL_TEMPLATE = "https://www.producthunt.com/leaderboard/daily/{year}/{month}/{day}"

def format_ymd(y, m, d):
    return f"{y}/{m:02d}/{d:02d}"
