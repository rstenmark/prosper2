# Prosper2

## Overview
Prosper2 is a collection of Python (>=3.11) scripts for collecting and curating data from the game [Prosperous Universe](https://prosperousuniverse.com/). The data collected is focused on the Commodity Exchange (CX) mechanic, where players in a local area can exchange materials for currency. 

Prosper2 does the following; It:
1. Collects data from sources (Currently the ["FIO" API](https://doc.fnar.net)).
2. Stores collected data in a local SQLite database.
3. Deduplicates or retains only unique data to save disk space. 

## Data source(s)
Currently, data is solely sourced from the [third-party "FIO" API](https://doc.fnar.net). This API sources its data from players who voluntarily install a browser extension to have game data automatically scraped and posted to the API for others to consume programmatically.

## Deduplication
Duplicate data is discarded. In instances where the lifetime of a datapoint is of interest, the first time it is observed as being unique and the last time it is discarded as a duplicate are recorded.
