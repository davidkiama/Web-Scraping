from selenium import webdriver
from bs4 import BeautifulSoup as bs

from time import sleep


class SearchCode:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            "https://www.tax.service.gov.uk/eat-out-to-help-out/find-a-restaurant"
        )

        codes = [
            "SW1A 1AA", "SW1A 2AA", "SW1A 0AA", "L30 4GB", "L1 8JQ",
            "EC1A 1BB", "CR2 6XH", "W1A 1AA", "BF1 2AT", "EC4Y 0HQ",
            "YO31 1EB", "NG80 1RH", "N1 9GU", "SW1W 0DT", "CF10 1BH",
            "SE1 8UJ", "SW1A 0PW", "B33 8TH", "EC2N 2DB", "CF99 1NA",
            "DH99 1NS", "LS98 1FD", "SN38 1NW", "NG80 1EH", "AB10", "SW1W 0NY",
            "GU16 7HF", "SW1H 0TL", "SW1P 3EU", "CV4 8UW", "E14 5HQ",
            "EH12 1HQ", "SW15 5PU", "E14 5JP", "E20 3BS", "E20 2AQ", "E20 3HB",
            "E20 2ST", "E20 3ET", "W1T 1FB", "SR5 1SU", "SE1 0NE", "DE55 4SW",
            "GL51 0EX", "NE1 4ST", "CV35 0DB", "M50 2BH", "M50 2QH", "M1 1AE"
        ]
        i = 0
        while i < len(codes):
            self.driver.find_element_by_xpath(
                "//input[contains(@class, 'govuk')]").send_keys(codes[i])
            sleep(3)

            self.driver.find_element_by_xpath(
                "//button[contains(@class, 'govuk')]").click()
            sleep(3)

            results_container = self.driver.find_element_by_xpath(
                "//ol[contains(@class, 'results')]")

            restaurants = results_container.find_elements_by_tag_name('li')
            print(restaurants)
            """for restaurant in restaurants:
                name = restaurant.find_elements_by_tag_name("h3").getText()
                print(name)"""

            sleep(3)

            self.driver.get(
                "https://www.tax.service.gov.uk/eat-out-to-help-out/find-a-restaurant"
            )

            i += 1


SearchCode()