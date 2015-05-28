# GeoTweet
Tweets on Geographical Map

This application is to filter tweets locations using Twitter Streaming API and show them in Google Map in real-time. It uses Python to fetch the locations of tweets from Twitter and save them in local json files, which are called by D3 in HTML. The locations are marked in real time in the map and fade away in seconds.


How to use:

1. Keep geotweet.py, index.html and folder data (saving temporary streaming tweets in .json) in the same directory;

2. In geotweets.py, change DATA_DIR to the path of folder data in your directory, e.g., DATA_DIR = '/usr/geotweet/data';

3. In geotweets.py, filter tweets by locations which is defined using TRACK_LOC (e.g., '-74,40,-73,41': New York City);

4. Run geotweets.py firstly, then open index.html in web browser, e.g., Safari.


Limitations:
There are some seconds delay to mark the locations in the map.

