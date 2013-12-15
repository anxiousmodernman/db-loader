from sqlalchemy import Column, Integer, String, MetaData, Table
import csv

# helper functions
def load_csv_into_memory():
    data = csv.Dictreader(open('donations.csv', 'r'))

def define_fec_master():
    metadata = MetaData()
    fec_data = Table('donations', metadata
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



