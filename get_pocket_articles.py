#!/usr/local/bin/python3

# PURPOSE =========================================================================================
# Create and open a CSV file containing a list of Pocket articles and their metadata
#
# USE =============================================================================================
# STEP 1:   Configure parameters in config.py file.
# STEP 2:   Open command line.
# STEP 3:   Use form 'python3 get_pocket_access_token.py [ -unfiltered ]' with optional unfiltered flag.
#
###################################################################################################

import config
import subprocess
import os
import argparse
import sys
import requests
import time
import datetime as dt
import pandas as pd
from datetime import datetime

def main() :
    try:
        # Make call to Pocket API to obtain the user's list of articles and assemble dataframe
        # retrieve_response = getPocketArticles()
        retrieve_url = 'https://getpocket.com/v3/get'
        retrieve_params = prepareRetrieveParameters()
        retrieve_response = requests.post(retrieve_url, data=retrieve_params)
        df = createArticleDataframe(retrieve_response)

        # Write the file to CSV and open it
        df.to_csv(config.FILE_NAME)
        openCSV()
        sys.exit()
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)

# Prepare Pocket API retrieve call parameters as per config.py
def prepareRetrieveParameters() : 
    params = {
        'consumer_key': config.CONSUMER_KEY,
        'access_token': config.ACCESS_TOKEN,
        'state': config.STATE,
        'sort': config.SORT,
        'detailType': config.DETAIL_TYPE,
        'count': config.COUNT,
        'offset': config.OFFSET
    }

    if config.FAVORITE is not -1:
        params['favorite'] = config.FAVORITE
    if config.TAG is not '':
        params['tag'] = config.TAG
    if config.CONTENT_TYPE is not 'all':
        params['contentType'] = config.CONTENT_TYPE
    if config.SEARCH is not '':
        params['search'] = config.SEARCH
    if config.DOMAIN is not '':
        params['domain'] = config.DOMAIN
    if config.SINCE is not 'beginning':
        params['since'] = time.mktime(dt.datetime.strptime(config.SINCE,'%Y%m%d').timetuple())
    return params

# Create the Pocket article dataframe
def createArticleDataframe(response) :
    df = pd.DataFrame(response.json()['list']).transpose()
    if not df.empty :
        df['time_added'] = df['time_added'].map(lambda timestamp: str(datetime.fromtimestamp(int(timestamp))))
        df = filterDataframe(df)
    return df

# Filter the dataframe to contain only the configured metadata columns
def filterDataframe(df) : 
    parser = argparse.ArgumentParser()
    parser.add_argument('-unfiltered', action='store_true')

    options = parser.parse_args()
    if options.unfiltered:
        return df
    else:
        return df[config.METADATA_FIELDS]

# Open created CSV file
def openCSV() :
    if sys.platform == "win32":
        os.startfile(config.FILE_NAME)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, config.FILE_NAME])
    return

main()