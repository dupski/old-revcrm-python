
# Rev Server Configuration File

DEBUG_SERVER_ADDRESS = '127.0.0.1'
DEBUG_SERVER_PORT = 8888
DEBUG_LOG_REQUESTS = True

DATABASES = {
    'default' : {
        'provider' : 'rev.db.providers.mongodb',
        'host' :  '127.0.0.1',
        'port' : 27017,
        'database' : "revtest",
    }
}

MODULE_PATHS = [
    '/home/russell/code/revframework/revframework/rev_modules',
    '/home/russell/code/revframework/revcrm/rev_modules',
]

INSTALLED_MODULES = [
    'revcrm_base',
    'revcrm_calendar',
]

from site_settings import *