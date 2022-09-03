#!/usr/bin/python3.11
import sqlite3
import prosper2.path as path
import prosper2.database.query as query

# Connect to the database, creating the file
# if it does not already exist:
with sqlite3.connect(path.database) as con:
    # Get a cursor:
    cur = con.cursor()
    # Create tables
    query.create_table_exchange_derived(cur)
    query.create_table_exchange_orders(cur)
    query.create_table_material_all(cur)
    query.create_table_exchange_station(cur)
    # Commit changes
    con.commit()

    