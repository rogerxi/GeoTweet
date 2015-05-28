# Import TwitterAPI
from TwitterAPI import TwitterAPI
import json, os, time, math

# Set user credentials to access Twitter Streaming API
CONSUMER_KEY = "GAwV1T5izyqwG4CYjjguF8JlK"
CONSUMER_SECRET = "ldAsK64cznb3AXME3BOeiroyskXcEDUYiDjMKXsfHhfm3CIH1u"
ACCESS_TOKEN_KEY = "2741532921-HqGBXeMGCrqxq2oYlije3zgxv4oreQGT5UCgjhh"
ACCESS_TOKEN_SECRET = "1VIYCMBcoZO8gJevoSUzQheGILZGTZ4XA0gk7Lsr7L6vW"
api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

# Filter Tweets by locations with pairs of longitude and latitude
TRACK_LOC = '-74,40,-73,41'
tweets = api.request('statuses/filter', {'locations': TRACK_LOC})

# the directory for saving streaming data
DATA_DIR = '/Users/roger/Lab/g/data'
# the previous timestamp
prev_ts = 0
# dictionary for locations
dict_loc = {}

for item in tweets:
    # If coordinates is given
    if (item['coordinates']):
        import time
        curr_ts = int(time.time())
        # Remove old files which was generated some time (e.g., 5 seconds) ago
        if (curr_ts % 10 == 0):
            map(os.unlink, [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                            if (round(os.stat(os.path.join(DATA_DIR, f)).st_mtime) < curr_ts - 5)])
    
        # If the timestamp changes
        if (prev_ts != curr_ts):
            if (dict_loc):
                # Open a file for writing
                out_file = open("data/" + str(prev_ts) + ".json", "w")
                # Save the dictionary into the file
                json.dump(dict_loc, out_file, indent = 0)
                # Close the file
                out_file.close()
                # Clean dictionary
                dict_loc.clear()
            dict_loc = {item['user']['screen_name']: item['coordinates'][u'coordinates']}
            prev_ts = curr_ts
        else:
            # Append data to the dictionary
            dict_loc[item['user']['screen_name']] = item['coordinates'][u'coordinates']