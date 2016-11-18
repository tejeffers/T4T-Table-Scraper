# T4T-Table-Scraper
Scrape &amp; Map The New Yorker Tables for Two reviews

[View map] (http://htmlpreview.github.io/?https://github.com/tejeffers/T4T-Table-Scraper/blob/master/T4T_google-maps_102816.html) 


Here, I’ve used python’s open source beautifulsoup, geopy location services, and Google’s ‘requests’ API to scrape The New Yorker’s Tables for Two restaurant reviews, dating all the way back to 1936! Some have closed, some have moved, 

Here’s how it works:

1. Scrape each article from TNY’s Tables for Two history
2. For each review, save some info in a SQLite database for later:
  1. Restaurant name
  2. Address
  3. Telephone number
  4. Article Date
  5. Text of the review
3. Grab the latitude and longitude of the restaurant, either using:
  1. Python geopy
  2. Google’s ‘requests’ API
  (so far, neither is perfect…)
4. Format [Restaurant Name, Lat, Lng] for loading into Google Maps javascript.

Relevant notebooks:

* [T4T_scrape_database.ipynb](https://github.com/tejeffers/T4T-Table-Scraper/blob/master/T4T_scrape_database_161028.ipynb)
* [T4T_ExploratoryDataAnalysis.ipynb](https://github.com/tejeffers/T4T-Table-Scraper/blob/master/T4T_ExploratoryDataAnalysis_161028.ipynb)


![T4T_Map](https://github.com/tejeffers/T4T-Table-Scraper/blob/master/T4T_google-maps_Nishi.png)


To Do:

1. Sentiment analysis. Although rare, sometimes the reviews aren’t very good. Can I assign a rating system based on the text of the review?
2. From text, assign tags — (tacos, noodles, sushi, etc)
3. Time series analysis: how has the distribution of restaurants changed over the past 80 years?
4. Create a distance-based map: given current location, which amazing restaurant is closest?
5. Create a random-restaurant-generator… to resolve weeknight dinner ambivalence.
6. Repeat with the BarTabs page! A younger column, but a very valuable resource nevertheless!
