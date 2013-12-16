import sys, argparse
from sqlalchemy import Column, String, MetaData, Table
import csv
from datasource import dbconfig, engines

def load_csv_into_memory(file_input):
    data = csv.Dictreader(open(file_input, 'r'))
    return data


def create_fec_master():
    metadata = MetaData()
    fec_data = Table('donations', metadata,
        Column('cmte_id', String),
        Column('cand_id', String),
        Column('contrb_nm', String),
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
        Column('election_tp', String),
        )
        return fec_data

def load_to_db(data, engine):
    listdata = []
    for row in data:
        listdata.append(row)
    db_engine.execute(fec_data.insert(), listdata)
    return fec_data

def main(args):
    cmd_parser = argparse.ArgumentParser(description='Send input the csv loader', prog='fec_dataloader')
    cmd_parser.add_argument('file_input', type=str)
    opts = cmd_parser.parse_args(args)
    fec_data = load_to_db(opts.file_input)
    engine = engines.get_postgres_engine()
    config = dbconfig
    return main()

if __name__ == '__main__':    
    main(sys.argv[1:])