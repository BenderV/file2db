import pandas as pd
import csv
from sqlalchemy import create_engine
from pathlib import Path


def upload(uri, csv_path, table_name=None, schema='public'):
    if table_name is None or table_name == '':
        table_name = Path(csv_path).name.replace('.csv', '')

    print(f'Table name: {table_name}')

    engine = create_engine(uri)

    with open(csv_path, 'r+') as f:
        csvreader = csv.DictReader(f)
        rows = list(csvreader)

    df = pd.DataFrame(rows)
    df.to_sql(
        table_name,
        engine,
        index=False,
        schema=schema,
        if_exists='replace'
    )
