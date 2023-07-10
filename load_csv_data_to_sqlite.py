#!/usr/bin/env python3

import pandas as pd
import csv
import sqlite3
import argparse


# Pandas: read csv file and write records stored in the dataFrame to a SQL database
def csv_to_sqlite(csv, table):
    file = pd.read_csv(csv, usecols=range(1, 5))
    file.to_sql(table, conn, if_exists='replace', index=True, index_label='id')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="CSV to SQL")
    parser.add_argument("-f", help="Path to the .csv file")
    parser.add_argument("-d", help="Path to the .db database")
    parser.add_argument("-t", help="Database table name")
    args = parser.parse_args()

    try:
        conn = sqlite3.connect(args.d)
    except sqlite3.Error as e:
        raise e

    curr = conn.cursor()
    csv_to_sqlite(args.f, args.t)
    conn.close()
