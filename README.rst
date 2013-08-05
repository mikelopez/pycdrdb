pycdrdb
========

Lightweight Asterisk CDR wrapper with Python and SQLAlchemy

Settings
========
Use the following variables in local_settings to override default behavior or set your authentication defaults. Otherwise, you can provide them when you instantiate the class.
* DB_HOST = The hostname of the db
* DB_USER = Database username 
* DB_PASS = The database password
* DB_NAME = Name of the database
* CDR_TABLE = Table name of the Asterisk CDR table. Defaults to ``cdr``
* TEST_SEARCH_NUMBER = Test phone number to use when searching the database in ``tests.py``