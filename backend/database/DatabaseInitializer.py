import os
import pandas as pd
import sqlite3
from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def prepare_database(app: FastAPI):
    names = [
        "categories.csv", "customers.csv", "employee_territories.csv",
        "employees.csv", "orders.csv", "orders_details.csv",
        "products.csv", "regions.csv", "shippers.csv",
        "suppliers.csv", "territories.csv"
    ]
    for name in names:
        path = os.path.join("resources", name)
        if os.path.exists(path):
            df = pd.read_csv(path, sep=",")
            try:
                with sqlite3.connect("database/sample_database.db") as conn:
                    df.to_sql(name[:-4], conn, if_exists="fail", index=False)
            except ValueError:
                print(f"Table '{name[:-4]}' already exists.")
        else:
            print(f"File {name} not found.")

    yield
