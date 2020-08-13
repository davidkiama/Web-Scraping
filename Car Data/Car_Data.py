# Importing the Libraries
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Getting the data for each car
url = 'https://www.pigiame.co.ke/vehicles'
response = requests.get(url)
html = response.text
soup = bs(html, 'html.parser')
car_container = soup.findAll('div', {'class': 'listing-card__content'})

# Empty list to be filled later
master_list = []

for detail in car_container:
    master_dict = {}
    # Extracting data for each car
    title = detail.div.div.div.div.text.strip()
    master_dict['Title'] = title
    brand_cont = detail.findAll('span')
    if len(brand_cont) > 6:
        brand = brand_cont[1].text.strip()
        auto = brand_cont[3].text.strip()
        location = brand_cont[4].text.strip()
        price = brand_cont[6].text.strip()

        # Fill the dictionary
        master_dict['Brand'] = brand
        master_dict['Gear-Shift'] = auto
        master_dict['Location'] = location
        master_dict['Price'] = price
        master_list.append(master_dict)

# Parsing the data in a DataFrame
df = pd.DataFrame(master_list)

# Storing the data in a CSV format
df.to_csv('Pigiame Vehicles', index=False)
