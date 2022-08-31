CXDerived = {
    "name": "CXDerived",
    "columns": [
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
    ],
    "affinities": [
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "REAL",
        "REAL",
        "INTEGER",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "INTEGER",
        "REAL",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "TEXT",
        "INTEGER"
    ]
}
CXOrders = {
    "name": "CXOrders",
    "columns": [
        "Type",
        "OrderId",
        "CompanyId",
        "CompanyName",
        "CompanyCode",
        "ItemCount",
        "ItemCost",
        "UserNameSubmitted",
        "Timestamp",
        "PriceTimeEpochMs",
        "FirstSeen",
        "LastSeen"
    ],
    "affinities": [
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "INTEGER",
        "REAL",
        "TEXT",
        "TEXT",
        "INTEGER",
        "INTEGER",
        "INTEGER"
    ]
}
Material = {
    "name": "Material",
    "columns": [
        "MaterialId",
        "CategoryName",
        "CategoryId",
        "Name",
        "Ticker",
        "Weight",
        "Volume",
        "UserNameSubmitted",
        "Timestamp"
    ],
    "affinities": [
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "REAL",
        "REAL",
        "TEXT",
        "TEXT"
    ]
}
Planet = {
    "name": "Planet",
    "columns": [
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
    ],
    "affinities": [
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "INTEGER",
        "INTEGER",
        "TEXT",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "NUMERIC",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "INTEGER",
        "REAL",
        "REAL",
        "REAL",
        "REAL",
        "INTEGER",
        "REAL",
        "REAL",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "INTEGER",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "TEXT",
        "REAL",
        "REAL",
        "REAL",
        "TEXT",
        "TEXT",
        "INTEGER",
        "TEXT",
        "TEXT"
    ]
}