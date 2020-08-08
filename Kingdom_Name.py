# Importing the Libraries
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd

# Getting the Rows
url = 'https://lordsmobilemaps.com/en/kingdom/ranking/population'
response = requests.get(url)
html = response.text
html_page = soup(html, 'html.parser')
rows = html_page.findAll('div', {'class': 'toptabrow'})

# Empty list to be filled later
master_list = []

for detail in rows:
    data_dict = {}
    row_container = detail.findAll('div')

    # Extracts data from the rows
    index = row_container[0].text.strip()
    kingdom_name = row_container[1].text.strip()
    population = row_container[2].text.strip()
    bp_clan_name = row_container[3].text.strip()
    bk_clan_name = row_container[4].text.strip()
    bp_player_name = row_container[5].text.strip()
    bk_player_name = row_container[6].text.strip()

    # Fill the dictionary
    data_dict['#'] = index
    data_dict['Kingdom Name'] = kingdom_name
    data_dict['Population'] = population
    data_dict['Best power clan name'] = bp_clan_name
    data_dict['Best kills clan name'] = bk_clan_name
    data_dict['Best power player name'] = bp_player_name
    data_dict['Best kills player name'] = bk_player_name
    master_list.append(data_dict)

# Parsing the data in a DataFrame
df = pd.DataFrame(master_list)

# Storing the data in a CSV format
df.to_csv('Kingdom Ranking', index=False)
