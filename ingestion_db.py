import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level= logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)
# 1) show current working dir (where a relative DB would be created)
print("cwd:", os.getcwd())
print("files here:", os.listdir("."))

# 2) create engine (relative path)
engine = create_engine('sqlite:///inventory.db')
print("engine url:", engine.url)

# 3) check if file exists yet
print("file exists before write:", os.path.exists("inventory.db"))

# 4a) Option A — create a table using SQLAlchemy Core (this WILL create the file)
meta = MetaData()
products = Table(
    "products", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("qty", Integer),
)
meta.create_all(engine)   # <- creates DB file and table if not present

# 4b) Option B — or write a pandas DataFrame (also creates the file)
# df = pd.DataFrame({"name":["apple","banana"], "qty":[10,5]})
# df.to_sql("products_pd", engine, if_exists="replace", index=False)

# 5) verify file now exists and list files again
print("file exists after write:", os.path.exists("inventory.db"))
print("files here after write:", os.listdir("."))

# 6) quick read to confirm table is present
with engine.connect() as conn:
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print("tables in DB:", res)
def ingest_db(df, table_name, engine):
    '''this fuction will ingest the dataform into database table'''
    df.to_sql(table_name, con = engine, if_exists = 'replace', index = False)

def load_raw_data():
    '''this function will load the CSVs as datafrom and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df= pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    end= time.time()
    total_time =(end - start)/ 60
    logging.info('----------Ingestion Complete----------')
    logging.info(f'\nTotal Time Taken: {total_time} minutes')

if __name__ == "__main__":
    load_raw_data()