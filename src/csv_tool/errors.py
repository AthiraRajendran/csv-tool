class CsvToolError(Exception):
    """Base class for all csv_tool errors."""


class InvalidRowError(CsvToolError):
    """A row has missing or invalid data."""