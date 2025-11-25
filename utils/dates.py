# -*- coding: utf-8 -*-
"""
Created on Mon Nov 24 21:33:31 2025

@author: Lenovo
"""
import calendar
from datetime import date

# there is no archive before 26 november 2013
CUTOFF = date(2013, 11, 26)

def build_dates(start_year=2013, end_year=2013):
    dates = []
    for y in range(start_year, end_year + 1):
        for m in range(1, 13):
            for d in range(1, calendar.monthrange(y, m)[1] + 1):
                if date(y, m, d) < CUTOFF:
                    continue
                dates.append((y, m, d))
    return dates

if __name__ == "__main__" :
    dates = build_dates(start_year=2013, end_year=2013)
