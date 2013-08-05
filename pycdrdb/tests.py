from unittest import TestCase, TestSuite, TextTestRunner
from dbaccess import *
from models import *
import settings as s
from termprint import *

auth = (getattr(s, "DB_HOST"), 
        getattr(s, "DB_USER"), 
        getattr(s, "DB_PASS"), 
        getattr(s, "DB_NAME"),)

class TestConnection(TestCase):
    def test_connection(self):
        """ Test the connection to the database server. """
        session, metadata, connection = db(*auth)
        self.assertTrue(session)
        self.assertTrue(connection)
        self.assertTrue(metadata)
        db_disconnect(connection)

    def test_model_and_search(self):
        """ Test the model (table) structure. """
        session, metadata, connection = db(*auth)
        cdr_table = map_table(metadata, CDR, cdr, autoload=False, skip_table=True)
        results = db_filter(session, cdr_table, "dst", getattr(s, "TEST_SEARCH_NUMBER", "7861111111"))
        termprint("INFO", cdr_table.__dict__)
        termprint("WARNING", results)
        for i in results:
            termprint("INFO", i.calldate)
            for k, v in i.__dict__.items():
                termprint("ERROR", "\t%s = %s" % (k, v))
            termprint("INFO", "\n-------------------\n\n")
        db_disconnect(connection)


if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(TestConnection("test_connection"))
    suite.addTest(TestConnection("test_model_and_search"))
    TextTestRunner(verbosity=2).run(suite)
