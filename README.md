# GeoTweet
Tweets on Geographical Map


This application is to filter tweets from Twitter Streaming API by locations, and represent them synchronously in Google Map. It is not implemented in web framework, but in a simple way: geotweet.py fetches the locations of tweets from Twitter and saves them in local json files, which transfer the data to D3.js in index.html. This HTML file builds a Google map where the locations is marked in real-time and fade away in seconds.



How to use:

1. Keep geotweet.py, index.html and folder data (for saving temporary streaming tweets in .json) in the same directory;

2. In geotweets.py, change DATA_DIR to the path of folder data in your directory, e.g., DATA_DIR = '/usr/geotweet/data';

3. In geotweets.py, filter tweets by locations which are defined in TRACK_LOC (e.g., '-74,40,-73,41': New York City);

4. Run geotweets.py firstly, then open index.html in web browser, e.g., Safari.



Limitations:
There are some seconds delay to mark the locations in the map.

