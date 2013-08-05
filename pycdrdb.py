try:
    import local_settings as s
except ImportError:
    pass

from dbaccess import *

auth = {'host': getattr(s, "DB_HOST"), '
