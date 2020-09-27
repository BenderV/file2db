import pandas as pd
import csv
import fire
import colored
from colored import stylize
from sqlalchemy import create_engine
from pathlib import Path


def upload(uri, path, table_name=None, schema=None):
    path = Path(path)

    if table_name is None or table_name == '':
        table_name = path.name.split('.')[0].lower()

    if schema == '':
        schema = None

    print(f'Table name: {table_name}')

    engine = create_engine(uri)

    if path.suffix.lower() == '.csv':
        read_funcs = [pd.read_csv]
    elif path.suffix.lower() == '.json':
        read_funcs = [pd.read_json]
    elif path.suffix.lower() == '.xlsx':
        read_funcs = [pd.read_excel]
    else:
        read_funcs = [pd.read_csv, pd.read_json, pd.read_excel]

    for func in read_funcs:
        try:
            print(f'Try: {func.__name__}')
            df = func(path)
        except Exception as e:
            print(stylize(e, colored.fg("red")))
            continue
        else:
            # if 'id' not in df.columns:
            #     df.index.names = ['id']
            df.to_sql(
                table_name,
                engine,
                # index=True,
                schema=schema,
                if_exists='replace'
            )
            break


if __name__ == '__main__':
  fire.Fire(upload)
