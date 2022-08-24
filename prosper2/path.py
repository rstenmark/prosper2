import pathlib

# This is the absolute path to the root directory of the project.
# Replace the path string with the correct path if it differs from
# the one provided by default.
root: pathlib.Path = pathlib.Path("/home/rs/prosper2")

# Absolute path to the scripts directory (folder)
scripts: pathlib.Path = pathlib.Path(root / "scripts")

# Absolute path to the sqlite3 database (file)
database: pathlib.Path = pathlib.Path(root / "database.db")

# Absolute path to the logging directory (folder)
logging: pathlib.Path = pathlib.Path(root / "logs")