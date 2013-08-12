from sqlalchemy import Table, MetaData, Column, ForeignKey, \
Integer, String, DateTime
from sqlalchemy.orm import mapper

try:
    import local_settings as s
    tbl = getattr(s, "CDR_TABLE", "cdr")
except ImportError:
    tbl = "cdr"

metadata = MetaData()

# tables below would need to be mapped to a class
cdr = Table(tbl, metadata,
            Column('calldate', DateTime, primary_key=True),
            Column('clid', String(240)),
            Column('src', String(240)),
            Column('dst', String(240)),
            Column('dcontext', String(240)),
            Column('channel', String(240)),
            Column('dstchannel', String(240)),
            Column('lastapp', String(240)),
            Column('lastdata', String(240)),
            Column('duration', Integer),
            Column('billsec', Integer),
            Column('disposition', String(135)),
            Column('amaflags', Integer),
            Column('accountcode', String(60)),
            Column('uniqueid', String(96)),
            Column('userfield', String(765)),)



