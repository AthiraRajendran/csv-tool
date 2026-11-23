# def summarize(rows):
#     total = 0
#     highest = 0
#     name = ""
#     for row in rows:
#         amount = int(row["amount"])
#         total += amount
#         if amount > highest:
#             highest = amount
#             name = row["name"]
#     return total, name, highest

# from csv_tool.errors import InvalidRowError


# def summarize(rows):
#     if not rows:
#         raise InvalidRowError("No data rows to summarize")

#     total = 0
#     highest = None
#     name = ""
#     for line_no, row in enumerate(rows, start=2):  # line 1 is the header
#         try:
#             amount = int(row["amount"])
#         except KeyError:
#             raise InvalidRowError(f"Line {line_no}: missing 'amount' column") from None
#         except ValueError:
#             raise InvalidRowError(
#                 f"Line {line_no}: invalid amount {row['amount']!r}"
#             ) from None

#         total += amount
#         if highest is None or amount > highest:
#             highest = amount
#             name = row["name"]
#     return total, name, highest
from csv_tool.errors import InvalidRowError


def summarize(rows: list[dict[str, str]]) ->  tuple[int, str, int]:
    if not rows:
        raise InvalidRowError("No data rows to summarize")

    total = 0
    highest: int | None = None
    name = ""
    for line_no, row in enumerate(rows, start=2):
        try:
            amount = int(row["amount"])
        except KeyError:
            raise InvalidRowError(f"Line {line_no}: missing 'amount' column") from None
        except ValueError:
            raise InvalidRowError(
                f"Line {line_no}: invalid amount {row['amount']!r}"
            ) from None

        total += amount
        if highest is None or amount > highest:
            highest = amount
            name = row["name"]

    assert highest is not None  # rows is non-empty, so this is always set
    return total, name, highest