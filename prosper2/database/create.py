import prosper2.database.definitions as table_definitions
from prosper2.helpers import list_to_string_comma_delimited
from prosper2.logging import Logger
import sqlite3

log_filename = "create_database"
logger = Logger(log_filename)

def _create_table_query_from_definition(table_definition: dict) -> str:
    '''
    Assemble a create-table-stmt from a table definition
    See: https://www.sqlite.org/lang_createtable.html
    '''
    # create-table-stmt
    ret = f"CREATE TABLE {table_definition['name']}("
    for column, affinity in zip(
        table_definition['columns'],
        table_definition['affinities']
    ):
        # column-def
        ret += f"{column} {affinity},"

    # Remove trailing comma, add closing parenthesis
    ret = ret[:-1] + ")"
    return ret

def _create_table(cur: sqlite3.Cursor, table_definition: dict) -> None:
    try:
        # Log intent
        logger.log_ok(
        f"Creating table named {table_definition['name']}\
             with columns {table_definition['columns']}")
        # Execute query
        cur.execute(
            _create_table_query_from_definition(table_definition)
        )
    except Exception as exc:
        # Log error and continue execution
        logger.log_error(
            f"Table creation failed with exception",
            exc
        )
        pass

def create_table_exchange_derived(cur: sqlite3.Cursor) -> None:
    """
    Create a table named CXDerived with the provided cursor.
    This table will contain derived data from the /exchange/all FIO API
    endpoint, including the last traded price, high/low price, etc.
    This endpoint provides all current data from all CXs, including
    discrete order data. Discrete order data is instead stored in
    the CXOrders table. 
    """
    _create_table(cur, table_definitions.CXDerived)

def create_table_exchange_orders(cur: sqlite3.Cursor) -> None:
    """
    Create a table named CXOrders with the provided cursor.
    This table will contain order data from the /exchange/full FIO API
    endpoint.
    This endpoint provides current detailed data about all CXs, however
    this table only contains discrete order data. Information derived from
    this order data is stored in the CXDerived table.
    """
    _create_table(cur, table_definitions.CXOrders)

def create_table_exchange_station(cur: sqlite3.Cursor) -> None:
    """
    Create a table named CXStation with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all CX
    stations.
    """
    raise NotImplementedError
    #_create_table(cur, name, columns)

def create_table_material_all(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Material with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all
    materials.
    """
    _create_table(cur, table_definitions.Material)
    

def create_table_planet_full(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Planet with the provided cursor.
    This table will contain data from the /planet/allplanets/full
    FIO API endpoint.
    This endpoint provides current information describing all
    planets.
    """
    _create_table(cur, table_definitions.Planet)

def create_table_recipe(cur: sqlite3.Cursor) -> None:
    """
    Create a table named Recipe with the provided cursor.
    This table will contain data from the /recipes/allrecipes
    FIO API endpoint.
    This endpoint provides current information describing all
    recipes.
    """
    name = "Recipe"
    columns = [
        "BuildingTicker",
        "RecipeName",
        "Inputs",
        "Outputs",
        "TimeMs"
    ]
    _create_table(cur, name, columns)