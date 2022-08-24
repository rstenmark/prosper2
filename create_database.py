#!/usr/bin/python3.11
from venv import create
import prosper2.path as path
import prosper2.logging as logging
import sqlite3

log_filename = "create_database"
logger = logging.Logger(log_filename)

def list_to_string_comma_delimited(list: list[any]):
    """
    Takes a list and returns a string containing the list
    members as their string representations delimited by commas
    Ex: ["a", "b", 1] -> "a, b, 1" 
    """
    return str(list)[1:-1].replace("'", "")

def create_table(cur: sqlite3.Cursor, name: str, columns: list[str]) -> None:
    # Format list of column names into SQL arguments:
    columns = list_to_string_comma_delimited(columns)
    # Assemble the query
    query = f"""
    CREATE TABLE {name}({columns});
    """
    # Log intention
    logger.log_ok(
        f"Creating table named {name} with columns {columns}")
    try:
        # Try to execute the query
        cur.execute(query)
    except Exception as e:
        # Log error and continue execution
        logger.log_error(
            f"Table creation failed with error",
            e
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
    name = "CXDerived"
    columns = [
        "CXDataModelId",
        "MaterialName",
        "MaterialTicker",
        "MaterialId",
        "ExchangeName",
        "ExchangeCode",
        "Currency",
        "Previous",
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
        "Supply",
        "Demand",
        "Traded",
        "VolumeAmount",
        "PriceAverage",
        "NarrowPriceBandLow",
        "NarrowPriceBandHigh",
        "WidePriceBandLow",
        "WidePriceBandHigh",
        "MMBuy",
        "MMSell",
        "UserNameSubmitted",
        "Timestamp"
    ]
    create_table(cur, name, columns)

def create_table_exchange_orders(cur: sqlite3.Cursor) -> None:
    """
    Create a table named CXOrders with the provided cursor.
    This table will contain order data from the /exchange/full FIO API
    endpoint.
    This endpoint provides current detailed data about all CXs, however
    this table only contains discrete order data. Information derived from
    this order data is stored in the CXDerived table.
    """
    name = "CXOrders"
    columns = [
        "Type",
        "OrderId",
        "CompanyId",
        "CompanyName",
        "CompanyCode",
        "ItemCount",
        "ItemCost",
        "UserNameSubmitted",
        "Timestamp",
        "PriceTimeEpochMs"
    ]
    create_table(cur, name, columns)

def create_table_exchange_station(cur: sqlite3.Cursor) -> None:
    """
    Create a table named CXStation with the provided cursor.
    This table will contain data from the /exchange/station
    FIO API endpoint.
    This endpoint provides current information describing all CX
    stations.
    """
    name = "CXStation"
    columns = [
        "StationId",
        "NaturalId",
        "Name",
        "SystemId",
        "SystemNaturalId",
        "SystemName",
        "CommisionTimeEpochMs",
        "ComexId",
        "ComexName",
        "ComexCode",
        "WarehouseId",
        "CountryId",
        "CountryCode",
        "CountryName",
        "CurrencyNumericCode",
        "CurrencyCode",
        "CurrencyName",
        "CurrencyDecimals",
        "GovernorId",
        "GovernorUserName",
        "GovernorCorporationId",
        "GovernorCorporationName",
        "GovernorCorporationCode",
        "UserNameSubmitted",
        "Timestamp"
    ]
    create_table(cur, name, columns)

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
    This table will contain data from the /planet/allplanets/full
    FIO API endpoint.
    This endpoint provides current information describing all
    planets.
    """
    name = "Planet"
    columns = [
        "Resources",
        "BuildRequirements",
        "ProductionFees",
        "COGCPrograms",
        "COGCVotes",
        "COGCUpkeep",
        "PlanetId",
        "PlanetNaturalId",
        "PlanetName",
        "Namer",
        "NamingDataEpochMs",
        "Nameable",
        "SystemId",
        "Gravity",
        "MagneticField",
        "Mass",
        "MassEarth",
        "OrbitSemiMajorAxis",
        "OrbitEccentricity",
        "OrbitInclination",
        "OrbitRightAscension",
        "OrbitPeriapsis",
        "OrbitIndex",
        "Pressure",
        "Radiation",
        "Radius",
        "Sunlight",
        "Surface",
        "Temperature",
        "Fertility",
        "HasLocalMarket",
        "HasChamberOfCommerce",
        "HasWarehouse",
        "HasAdministrationCenter",
        "HasShipyard",
        "FactionCode",
        "FactionName",
        "GovernorId",
        "GovernorUserName",
        "GovernorCorporationId",
        "GovernorCorporationName",
        "GovernorCorporationCode",
        "CurrencyName",
        "CurrencyCode",
        "CollectorId",
        "CollectorName",
        "CollectorCode",
        "BaseLocalMarketFee",
        "LocalMarketFeeFactor",
        "WarehouseFee",
        "PopulationId",
        "COGCProgramStatus",
        "PlanetTier",
        "UserNameSubmitted",
        "Timestamp"
    ]
    create_table(cur, name, columns)

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
    create_table(cur, name, columns)

# Connect to the database, creating the file
# if it does not already exist:
with sqlite3.connect(path.database) as con:
    # Get a cursor:
    cur = con.cursor()
    # Create tables
    create_table_exchange_derived(cur)
    create_table_exchange_orders(cur)
    create_table_material_all(cur)
    create_table_exchange_station(cur)
    # Commit changes
    con.commit()

    