# blaseball-reference-py
Python wrapper around the Blaseball stats API

# Installation
```
pip install blaseball-reference
```

# Usage
https://api.blaseball-reference.com/docs#/

# Development
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Release
1. Update `version` in setup.py. Please use semver.
2. Merge changes
3. Create a new release in github with matching version ID. Project will be uploaded to PyPi automatically.

# Examples
To start,
```
from blaseball_reference import api
```


When no arguments are specified, a ```dict``` object is returned, with a key for each player ID that could fit the query. For example, running
```
print(api.batting_average())
```
will print a dictionary of every Blaseball batter and their batting averages, and will not return pitchers.
```
{'batter_id': value'}
```


Some queries, ```event_type``` for example, will return every player.


You can specify the ID of the player to filter by. Multiple pitchers can also be specified, by passing a list or a string delimited by commas
```
pitcherera = api.era("pitcher_id")
```
```
pitcherera = api.era(["pitcher_id", "pitcher_id", "pitcher_id"])
```
```
pitcherera = api.era("pitcher_id, pitcher_id, pitcher_id")
```
