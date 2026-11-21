import sys

from csv_tool.reader import read_rows
from csv_tool.processor import summarize


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    rows = read_rows(path)

    for row in rows:
        print(row["name"], row["amount"])

    total, name, highest = summarize(rows)
    print(f"Total = {total}")
    print(f"Highest = {name} {highest}")


if __name__ == "__main__":
    main()