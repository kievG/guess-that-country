"""
This script automates the scraping of countries from the site worldometers.info.
Data saved will be used in a mini-game called 'Guess-that-country!'
"""

from bs4 import BeautifulSoup
import requests
import csv

# request from website; use text only
html_text = requests.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/").text

# create instance of Beautifulsoup with lxml parser
soup = BeautifulSoup(html_text, 'lxml')

# read file content
with open('scraped_countries.csv', 'w') as csv_file:
    # write into csv file
    csv_writer = csv.writer(csv_file)
    # write csv file header
    csv_writer.writerow(['country', 'population', 'land_area', 'density'])

    # get countries and assign to variable countries
    countries = soup.tbody
    # get row/country from countries table
    for row in countries:
        country = row.text.replace(",", "")[1:]
        # split country entries and select 2nd to last elements of the list
        country = country.split()[1:]
        if country != []:
            density = country[-1]
            land_area = country[-2]
            population = country[-3]
            country_name = str(country[:-3]).replace("'", "")
            country_name = country_name.replace("[", "")
            country_name = country_name.replace("]", "")
            country_name = country_name.replace(",", "")
            country_name = country_name.replace(" ", "_")
            country_name = country_name.replace('"', "")
            country_name = country_name.replace('fmr._', "")
            country_name = country_name.replace('formerly_', "")
            # write scraped data into csv file
            csv_writer.writerow([country_name, population, land_area, density])
# close CSV file
csv_file.close()
# END