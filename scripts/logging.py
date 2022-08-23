from inspect import trace
import path, pathlib, enum, datetime

class Prefix(enum.Enum):
    OK = f"[OK]: "
    WARN = f"[WARN]: "
    ERROR = f"[ERR]: "

# Alias for datetime.datetime.utcnow
def utcnow(): return str(datetime.datetime.utcnow())

class Logger(object):
    """
    Cheap n' cheerful logger class
    """
    def __init__(self, log_file_name: str):
        # Log file name must be a string
        assert type(log_file_name) == str
        # The name of the log file that this logger writes to
        self.log_file_name = log_file_name

    def _log(self, log_string: str) -> None:
        """
        Writes the log string to a log file with the name provided  
        """
        # Open the log file in append mode, creating it if it
        # does not already exist: 
        with open(pathlib.Path(path.logging / (self.log_file_name + ".log")), 'a') as f:
            # Write the log string
            f.write(log_string)
            f.write("\n")

    def _log_many(self, log_strings: list[str]) -> None:
        """
        Writes many log strings to a log file with the name provided
        as one batch.
        """
        with open(pathlib.Path(path.logging / (self.log_file_name + ".log")), 'a') as f:
            for s in log_strings:
                f.write(s)
                f.write("\n")

    def log_ok(self, log_string: str) -> None:
        """
        Logs an "OK" status log to a log file with the name provided
        """
        self._log(f"@ {utcnow()} | {Prefix.OK.value}{log_string}")

    def log_oks(self, log_strings: list[str]) -> None:
        """
        Logs many "OK" status log strings to a log file 
        with the name provided
        """
        # Prefix strings with OK status prefix and datetime
        for i, v in enumerate(log_strings):
            log_strings[i] = f"{Prefix.OK.value}{v}"
        self._log_many(log_strings)

    def log_warning(self, log_string: str) -> None:
        """
        Logs an "WARN" status log to a log file with the name provided
        """
        self._log(f"@ {utcnow()} | {Prefix.WARN.value}{log_string}", )

    def log_warnings(self, log_strings: list[str]) -> None:
        """
        Logs many "WARN" status log strings to a log file 
        with the name provided
        """
        # Prefix strings with OK status prefix and datetime
        for i, v in enumerate(log_strings):
            log_strings[i] = f"{Prefix.WARN.value}{v}"
        self._log_many(log_strings)

    def log_error(self, log_string: str, exc: Exception) -> None:
        """
        Logs an "WARN" status log to a log file with the name 
        and exception object provided.
        """
        self._log(f"@ {utcnow()} | {Prefix.ERROR.value}{log_string}\n{type(exc)}\n{exc}")