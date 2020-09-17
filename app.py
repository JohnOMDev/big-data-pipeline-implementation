# Import useful libraries
import csv
import psycopg2

import time

# Create database
#open("xgeeks.db", "w").close()


#con = psycopg2.connect(database="xgeeks.db", user="postgres", password ="postgres")

#cursor
#cur = con.cursor()

#cur.execute("CREATE TABLE metmuseum(Object Number NUMERIC, Is Highlight, Is Timeline Work, Is Public Domain, Object ID, Department, AccessionYear, Object Name, Title, Culture, Period, Dynasty, Reign, Portfolio, Artist Role, Artist Prefix, Artist Display Name,Artist Suffix, Artist Alpha Sort, Artist Nationality, Artist Begin Date, Artist End Date, Artist Gender, Artist ULAN URL, Artist Wikidata URL, Object Date, Object Begin Date, Object End Date, Medium, Dimensions, Credit Line, Geography Type, City, State, County, Region, Subregion, Locale, Locus, Excavation, River, Classification, Rights and Reproduction, Link Resource, Object Wikidata URL, Metadata Date, Repository,Tags, Tags AAT URL)")

#close the connection
#con.close


"""Ingestion"""
# Open the downloaded CSV file
with open("openaccess/MetObjects.csv", mode="r", encoding="utf8") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over TSV file
    for row in reader:
        time.sleep(.001)
        """Transformation"""
        #Parsing
Object Number
Is Highlight
Is Timeline Work
Is Public Domain
Object ID
Department
AccessionYear
Object Name
Title
Culture
Period
Dynasty
Reign
Portfolio
Artist Role
Artist Prefix
Artist Display Name
Artist Suffix
Artist Alpha Sort
Artist Nationality
Artist Begin Date
Artist End Date
Artist Gender
Artist ULAN URL
Artist Wikidata URL
Object Date
Object Begin Date
Object End Date
Medium
Dimensions
Credit Line
Geography Type
City
State
County
Region
Subregion
Locale
Locus
Excavation
River
Classification
Rights and Reproduction
Link Resource
Object Wikidata URL
Metadata Date
Repository
Tags
Tags AAT URL
        #Correcting
        #Standardization
        #Matching
        #Consolidating
        print(row)






#cur.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)