import json
from datetime import timedelta
with open('acdc.json') as d:
    data = json.load(d)
    duration = [int(track['duration']) for track in data['album']['tracks']['track']]
    print(timedelta(seconds=(sum(duration))))