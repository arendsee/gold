#!/usr/bin/env python3

# Get current prices of precious metals and currencies relative to the US dollar

import requests 
  
if __name__ == '__main__':
  URL = "https://metals-api.com/api/latest"

  with open("API-key.txt", "r") as f:
    # Read the API key. For obvious reasons, this is not included in the
    # github repo. You can get your own key from https://metals-api.com and
    # write it into the API-key.txt file.
    key = "".join(f.readlines()).strip()
    PARAMS = {'access_key':key}
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()

  # Log the result under the date and timestamp. Since there are a limited
  # number of allowed API calls per month, it is best to store this data for
  # future reference.
  outfilename = f"{data['date']}_{data['timestamp']}.tab"

  with open(outfilename, "w") as out:
    # Print currency and metal rates relative to USD in columns:
    #   <currency> | <rate> | <date> | <timestamp>
    # The currency includes non-US currencies (by 3 letter currency code) and
    # metals by their codes. The metal codes all begin with X, for example, XAU
    # for gold and XAG for silver.
    # The 4th column is the UNIX timestamp (seconds since Jan 1, 1970).
    for (curr, rate) in data["rates"].items():
        print(f"{curr}\t{1 / float(rate)}\t{data['date']}\t{data['timestamp']}", file=out)
