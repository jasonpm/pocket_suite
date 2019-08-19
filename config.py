# PURPOSE =========================================================================================
# Configuration file for specifying required and optional parameters in get_pocket_articles.py
#
# USE =============================================================================================
# Change parameters as needed.
# Keep this file in the same directory as get_pocket_articles.py.
# See https://getpocket.com/developer/docs/v3/retrieve for further information.
#
###################################################################################################

##### REQUIRED PARAMETERS #####
###############################
#
# ===============================================
# PURPOSE:        Specifies outputted CSV file name
# VALID VALUES:   *.csv
FILE_NAME = 'pocket_articles.csv'

# ===============================================
# PURPOSE:        Specifies application's consumer key
# VALID VALUES:   Pocket consumer key generated when creating a new app at https://getpocket.com/developer/apps/
CONSUMER_KEY = '[YOUR-CONSUMER-KEY]'

# ===============================================
# PURPOSE:        Specifies user's access token
# VALID VALUES:   Pocket access token provided from authentication process
ACCESS_TOKEN = '[YOUR-ACCESS-TOKEN]'

###### OPTIONAL PARAMETERS #####
################################
#
# ===============================================
# PURPOSE:        List of metadata fields to display in the generated CSV file 
#                 (requires the '-unfiltered' flag to be specified on the command line).
# VALID VALUES:   Some subset of:
#                 [ 'item_id', 'resolved_id', 'given_url', 'resolved_url', 'given_title', 
#                   'resolved_title', 'favorite', 'status', 'excerpt', 'is_article', 
#                   'has_image', 'has_video', 'word_count', 'tags', 'authors', 'images', 'videos' ]
METADATA_FIELDS = [
    'time_added',
    'resolved_title',
    'given_url',
    'word_count',
    'excerpt'
    ]

# ===============================================
# PURPOSE:        Only return items in a particular state.
# VALID VALUES:   'unread', 'archive', 'all'
STATE = 'all'

# ===============================================
# PURPOSE:        Only return items that have been favorited/unfavorited.
# VALID VALUES:   -1 (all), 0 (unfavorited), 1 (favorited)
FAVORITE = -1

# ===============================================
# PURPOSE:        Specified number of records to retrieve from Pocket
# VALID VALUES:   '_untagged_' for all untagged records, '*' for all records tagged with '*'
TAG = ''

# ===============================================
# PURPOSE:        Specifies type of content to retrieve.
# VALID VALUES:   'article', 'video', 'image', 'all'
CONTENT_TYPE = 'all'

# ===============================================
# PURPOSE:        Specifies sorting method of retrieval results.
# VALID VALUES:   'newest', 'oldest', 'title', 'url'
SORT = 'newest'

# ===============================================
# PURPOSE:        Specifies whether to return all or limited information
# VALID VALUES:   'simple', 'complete'
DETAIL_TYPE = 'complete'

# ===============================================
# PURPOSE:        Only return items whose title or url contain the search string.
# VALID VALUES:   '*' to get records containing '*'
SEARCH = ''

# ===============================================
# PURPOSE:        Only return items from a particular domain.
# VALID VALUES:   '*' to get records from domain '*'
DOMAIN = ''

# ===============================================
# PURPOSE:        Only return items modified since the given date.
# VALID VALUES:   'YYYYMMDD', 'beginning'
SINCE = '20000101'

# ===============================================
# PURPOSE:        Specifies number of records to retrieve.
# VALID VALUES:   Integer (positive)
COUNT = 10000

# ===============================================
# PURPOSE:        Used only with count; start returning from offset position of results.
# VALID VALUES:   Integer (positive)
OFFSET = 0