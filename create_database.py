#!/usr/bin/python3.11
import prosper2.path as path
import prosper2.logging as logging
import sqlite3

log_filename = "create_database"
logger = logging.Logger(log_filename)

def list_to_string_comma_delimited(list: list[any]):
    """
    Takes a list and returns a string containing the list
    members as strings delimited by commas
    Ex: ["a", "b", 1] -> "a, b, 1" 
    """
    return str(list)[1:-1].replace("'", "")

def create_table(cur: sqlite3.Cursor, name: str, columns: list[str]) -> None:
    # Format list of column names into SQL arguments:
    # ["a", "b", "c"] -> "a, b, c" 
    columns = list_to_string_comma_delimited(columns)
    # Assemble the query
    query = f"""
    CREATE TABLE {name}({columns});
    """
    # Execute the query (create the table)
    logger.log_ok(
        f"Creating table named {name} with columns {columns}")
    try:
        cur.execute(query)
    except Exception as e:
        logger.log_error(
            f"Table creation failed with error",
            e
        )

def create_table_exchange_derived(cur: sqlite3.Cursor) -> None:
    """
    Create a table named ExchangeDerived with the provided cursor.
    This table will contain derived data from the /exchange/all FIO API
    endpoint, including the last traded price, high/low price, etc.
    This endpoint provides all current data from all CXs, including
    discrete order data.
    """
    name = "ExchangeDerived"
    columns = [
        "Price",
        "PriceTimeEpochMs",
        "High",
        "AllTimeHigh",
        "Low",
        "AllTimeLow",
        "Ask",
        "AskCount",
        "Bid",
        "BidCount",


    ]

def create_table_exchange_all(cur: sqlite3.Cursor) -> None:
    """
    Create a table named ExchangeSummary with the provided cursor.
    This table will contain data from the /exchange/all FIO API
    endpoint.
    This endpoint provides current summarized information from all CXs.
    """
    raise NotImplementedError

def create_table_exchange_station(cur: sqlite3.Cursor) -> None:
    """
    Create a table named ExchangeStation with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all CX
    stations.
    """
    raise NotImplementedError

def create_table_material_all(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Material with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all
    materials.
    """
    name = "Material"
    columns = [
        "MaterialId",
        "CategoryName",
        "CategoryId",
        "Name",
        "Ticker",
        "Weight",
        "Volume",
        "UserNameSubmitted",
        "Timestamp"
    ]
    create_table(cur, name, columns)
    

def create_table_planet_full(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Planet with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all
    planets.
    """
    raise NotImplementedError

def create_table_recipe(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Recipe with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all
    recipes.
    """

# Connect to the database, creating the file
# if it does not already exist:
with sqlite3.connect(path.database) as con:
    # Get a cursor:
    cur = con.cursor()
    create_table_material_all(cur)
    # Commit changes
    con.commit()

    