# Import useful libraries
import csv
import psycopg2

# Open the downloaded CSV file
with open("openaccess/MetObjects.csv", mode="r", encoding="utf8") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over TSV file
    for row in reader:
        print(row["Object Begin Date"])