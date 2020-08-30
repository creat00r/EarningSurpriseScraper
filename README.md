# EarningSurpriseScraper
Earning Surprise Stock Scraper

Scrapes earning surprises from nasdaq.com and puts them in a csv.

Uses python 3!
Requires installing the Firefox geckodriver and updating its directory in scraper.py.
If you have less than 8 cores update line 15 in earningSurprise.py.
replace "with mp.Pool(processes=8) as pool:" with "with mp.Pool(processes=<number of cores>) as pool:"

You can check how many cores you have with the nproc command
Happy scraping!
