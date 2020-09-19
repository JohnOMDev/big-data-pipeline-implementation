# Import useful libraries
import csv
#import psycopg2

import time

# Create database
#open("xgeeks.db", "w").close()


#con = psycopg2.connect(database="xgeeks.db", user="postgres", password ="postgres")

#cursor
#cur = con.cursor()

#cur.execute("CREATE TABLE metmuseum(Object Number NUMERIC, Is Highlight, Is Timeline Work, Is Public Domain, Object ID, Department, AccessionYear, Object Name, Title, Culture, Period, Dynasty, Reign, Portfolio, Artist Role, Artist Prefix, Artist Display Name,Artist Suffix, Artist Alpha Sort, Artist Nationality, Artist Begin Date, Artist End Date, Artist Gender, Artist ULAN URL, Artist Wikidata URL, Object Date, Object Begin Date, Object End Date, Medium, Dimensions, Credit Line, Geography Type, City, State, County, Region, Subregion, Locale, Locus, Excavation, River, Classification, Rights and Reproduction, Link Resource, Object Wikidata URL, Metadata Date, Repository,Tags, Tags AAT URL)")

#close the connection
#con.close

def parsing_strip(data):
     out = data.split('|',1)
     out = out.split('-',1)
     out = out.split(',',1)
     out = out.split('(',1)
     out = out.replace('probably','')
     out = out.replace('possibly','')
     out = out.replace('present-day','')
     out = out.replace('?','')
     out = out.strip()
     return out

"""Ingestion"""
# Open the downloaded CSV file
with open("openaccess/MetObjects.csv", mode="r", encoding="utf8") as file:

    # Create DictReader
    reader = csv.DictReader(file, delimiter=',')
    
    # Iterate over TSV file
    for row in reader:
        #time.sleep(.001)
        """Transformation"""
        #Standardization
        Object_number = row["\ufeffObject Number"]
        Is_Highlight = row["Is Highlight"]
        Is_Timeline_Work = row["Is Timeline Work"]
        Is_Public_Domain = row["Is Public Domain"]
        Object_ID = int(row["Object ID"])
        Accession_Year =row["AccessionYear"]
        Object_Name = row["Object Name"]
        Artist_Role = row["Artist Role"]
        Artist_Prefix = row["Artist Prefix"]
        Artist_Display_Name = row["Artist Display Name"]
        Artist_Suffix = row["Artist Suffix"]
        Artist_Alpha_Sort = row["Artist Alpha Sort"]
        Artist_Nationality = row["Artist Nationality"]
        Artist_Begin_Date = row["Artist Begin Date"]
        Artist_End_Date = row["Artist End Date"]
        Artist_Gender = row["Artist Gender"]
        Artist_ULAN_URL = row["Artist ULAN URL"]
        Artist_Wikidata_URL = row["Artist Wikidata URL"]
        Object_Date = row["Object Date"]
        Object_Begin_Date = row["Object Begin Date"]
        Object_End_Date = row["Object End Date"]
        Credit_Line = row["Credit Line"]
        Geography_Type = row["Geography Type"]
        Rights_and_Reproduction = row["Rights and Reproduction"]
        Link_Resource = row["Link Resource"]
        Object_Wikidata_URL = row["Object Wikidata URL"]
        Metadata_Date = row["Metadata Date"]
        Tags_AAT_URL = row["Tags AAT URL"]
        #Correcting
        #Parsing
        #Matching
        #Consolidating
        #for data in row['Country']:
        #      if (data== None).any():
        #             print("yes")
        

        out = row['Country'].split('|',1)
        print(parsing_strip(row['Country']))




#cur.execute("INSERT INTO genres (show_id, genre) VALUES(?, ?)", id, genre)