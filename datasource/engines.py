from sqlalchemy import create_engine
from datasource.dbconfig import postgres_connection


def get_postgres_engine():
    engine = create_engine('postgresql://%s:%s@%s' %
                          (postgres_connection['username'],
                           postgres_connection['password'],
                           postgres_connection['host'])
                           )
    return engine



