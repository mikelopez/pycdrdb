DB_HOST, DB_NAME, DB_PASS, DB_USER = "", "", "", ""
try:
    from local_settings import *
except ImportError:
    pass
