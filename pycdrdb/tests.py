try:
    import local_settings as s
except ImportError:
    pass

from dbaccess import *

auth = {'dbhost': getattr(s, "DB_HOST"), \
        'dbuser': getattr(s, "DB_USER"), \
        'dbpass': getattr(s, "DB_PASS"), \
        'dbname': getattr(s, "DB_NAME")}
cl = db(**auth)
cl.connect()

