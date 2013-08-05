try:
    import local_settings as s
    tbl = getattr(s, "CDR_TABLE", "asteriskcdrdb")
except ImportError:
    tbl = "asteriskcdrdb"

from sqlalchemy import Table, MetaData, Column, ForeignKey, \
Integer, String
from sqlalchemy.orm import mapper

metadata = MetaData()

cdr = Table('asteriskcdrdb', metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(50)),)

class CDR(object):
    pass

# automap?
#mapper(CDR, cdr)
