import unittest
from engines import get_postgres_engine


class PostgresDatabaseTest(unittest.TestCase):

    def test_connection(self):
        engine = get_postgres_engine()
        name = 'charles'
        data = 'male'
        conn = engine.connect()
        conn.execute('create table temp_table (id int, name text);')
        conn.execute('drop table temp_table;')
        conn.close()

if __name__ == '__main__':
    unittest.main()
