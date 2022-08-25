#!/usr/bin/python3.11
import sqlite3
import prosper2.path
import prosper2.database

# Connect to the database, creating the file
# if it does not already exist:
with sqlite3.connect(prosper2.path.database) as con:
    # Get a cursor:
    cur = con.cursor()
    # Create tables
    prosper2.database.create_table_exchange_derived(cur)
    prosper2.database.create_table_exchange_orders(cur)
    prosper2.database.create_table_material_all(cur)
    prosper2.database.create_table_exchange_station(cur)
    # Commit changes
    con.commit()

    