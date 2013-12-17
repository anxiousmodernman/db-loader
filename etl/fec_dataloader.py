import sys
import argparse
from sqlalchemy import Column, String, MetaData, Table
import csv
from datasource import engines


def load_csv_into_memory(file_input):
    data = csv.DictReader(open(file_input, 'r'))
    return data


def create_fec_master(engine):
    # "cmte_id"	"cand_id"	"cand_nm"	"contbr_nm"	"contbr_city"	"contbr_st"	"contbr_zip"
    # "contbr_employer"	"contbr_occupation"	"contb_receipt_amt"	"contb_receipt_dt"	"receipt_desc"
    # "memo_cd"	"memo_text"	"form_tp"	"file_num"	"tran_id"	"election_tp"
    metadata = MetaData()
    fec_data = Table('blownations', metadata,
        Column('cmte_id', String),
        Column('cand_id', String),
        Column('cand_nm', String),
        Column('contbr_nm', String),
        Column('contbr_city', String),
        Column('contbr_st', String),
        Column('contbr_zip', String),
        Column('contbr_employer', String),
        Column('contbr_occupation', String),
        Column('contb_receipt_amt', String),
        Column('contb_receipt_dt', String),
        Column('receipt_desc', String),
        Column('memo_cd', String),
        Column('memo_text', String),
        Column('form_tp', String),
        Column('file_num', String),
        Column('tran_id', String),
        Column('election_tp', String)
    )
    metadata.create_all(engine)
    return fec_data


def load_to_db(data, table, engine):
    data_list = []
    for row in data:
        data_list.append(row)
    statement = table.insert()
    engine.execute(statement, data_list)
    print 'did this work?'



def main(args):
    engine = engines.get_postgres_engine()
    cmd_parser = argparse.ArgumentParser(description='Send input the csv loader', prog='fec_dataloader')
    cmd_parser.add_argument('file_input', type=str)
    opts = cmd_parser.parse_args(args)
    data = load_csv_into_memory(opts.file_input)
    print 'checking type'
    table = create_fec_master(engine)  # returns a table
    load_to_db(data, table, engine)

if __name__ == '__main__':
    main(sys.argv[1:])