from ..logging import Logger
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

def create_table(cur: sqlite3.Cursor, table_definition: dict) -> None:
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