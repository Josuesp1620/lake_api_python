from fastapi import FastAPI

app = FastAPI()
import dataclasses
import file_query.api
import os

os.environ["ENABLE_SQL_ENDPOINT"] = "0"
def_cfg = file_query.api.get_default_config()

cfg = dataclasses.replace(def_cfg, enable_sql_endpoint=True, data_path="data/", default_engine="duckdb")
sti = file_query.api.init_lakeapi(app, True, cfg, "config.yml")

# uvicorn app:app --host 0.0.0.0 --port 3072