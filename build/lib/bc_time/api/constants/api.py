class Api:
    DOMAIN = 'http://time-v2.local'
    OAUTH2_TOKEN_URL = 'http://time-v2.local/oauth2/token/'
    OAUTH2_AUTHORISE_URL = 'http://time-v2.local/oauth2/authorise/'
    API_URL = 'http://time-v2.local/api/'
    DEFAULT_ROW_COUNT = 100 # 100 is the maximum no. of rows the API allows to retrieved at a time.
    UID_GET_ALL = -1
    UID_POST_MANY = -2