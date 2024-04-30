# main.py
import logging
import time
from selenium import webdriver
from availability_page import AvailabilityPage
from selenium.webdriver.chrome.options import Options

# URL of the Park Evanston website
PE_URL = "https://parkevanston.prospectportal.com/evanston/the-park-evanston/conventional/"
desired_month = "June"
desired_date = "2024-06-05"

def setup_driver():
    # Setting up Chrome driver options
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--window-size=2560,1440")
    # Returning a Chrome WebDriver instance with specified options
    return webdriver.Chrome(options=options)

def main():
    logging.basicConfig(level=logging.INFO)
    driver = setup_driver()
    driver.get(PE_URL)

    try:
        apartment_page = AvailabilityPage(driver)
        
        apartment_page.open_calendar()
        apartment_page.select_date(desired_month, desired_date)

        floor_plans_items = apartment_page.fetch_floor_plans("2")  # "2" for 2-bedroom apartments

        # print necessary details for each floor plan
        apartment_page.print_floor_plan_details(floor_plans_items)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()