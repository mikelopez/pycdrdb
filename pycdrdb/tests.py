from unittest import TestCase, TestSuite, TextTestRunner
from dbaccess import *
from models import *
from sqlalchemy.orm import mapper
import settings as s

auth = {'dbhost': getattr(s, "DB_HOST"), \
        'dbuser': getattr(s, "DB_USER"), \
        'dbpass': getattr(s, "DB_PASS"), \
        'dbname': getattr(s, "DB_NAME")}

class TestConnection(TestCase):
    def test_connection(self):
        """ Test the connection to the database server. """
        cl = db(**auth)
        cl.connect()
        self.assertTrue(cl.connection)

    def test_model(self):
        """ Test the model (table) structure. """
        cl = db(**auth)
        cl.connect()
        cdr_table = cl.map_table(CDR, cdr, autoload=False, skip_table=True)
        termprint("INFO", cdr_table.__dict__)
        


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(TestConnection("test_connection"))
    suite.addTest(TestConnection("test_model"))
    TextTestRunner(verbosity=2).run(suite)
