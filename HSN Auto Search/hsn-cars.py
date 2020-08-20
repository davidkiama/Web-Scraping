from selenium import webdriver
from time import sleep
import pandas as pd


class SearchCode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.hsn-tsn.de/")
        sleep(5)

        #Initializing
        master_list = []
        codes = ["0588/741", "0588/742"]
        i = 0
        while i < len(codes):
            data_dict = {}
            #Enter the HSN
            self.driver.find_element_by_xpath("//input[1]").send_keys(codes[i])
            sleep(3)

            #Click the search button
            self.driver.find_element_by_xpath("//input[2]").click()
            sleep(3)

            #Folow the link
            self.driver.find_element_by_xpath("//tr[2]/td[2]/a").click()

            #Save the car details
            brand = self.driver.find_element_by_xpath("//h1/span/span").text
            make = self.driver.find_element_by_xpath("//h1/span[2]").text
            title = brand + make
            year = self.driver.find_element_by_xpath("//h1/small").text
            designation = self.driver.find_element_by_xpath(
                "//p[@id='autodata']/span[2]").text

            #Fill the dictionary
            data_dict['Title'] = title
            data_dict['Year'] = year
            data_dict['Designation'] = designation
            master_list.append(data_dict)

            print(title, " ", year, " ", designation)

            self.driver.get("http://www.hsn-tsn.de/")

            i += 1

        # Parsing the data in a DataFrame
        df = pd.DataFrame(master_list)

        # Storing the data in a CSV format
        df.to_csv('HSN Codes Search', index=False)


SearchCode()