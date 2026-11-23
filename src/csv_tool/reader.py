# import csv


# def read_rows(path):
#     with open(path, newline="") as f:
#         return list(csv.DictReader(f))
    
# from csv_tool.errors import CsvToolError


# def read_rows(path):
#     try:
#         with open(path, newline="") as f:
#             return list(csv.DictReader(f))
#     except FileNotFoundError:
#         raise CsvToolError(f"File not found: {path}") from None
import csv

from csv_tool.errors import CsvToolError


def read_rows(path: str) -> list[dict[str, str]]:
    try:
        with open(path, newline="") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        raise CsvToolError(f"File not found: {path}") from None