# availability_page.py
# written with Page Object Model (POM) in mind
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AvailabilityPage:
    def __init__(self, driver):
        self.driver = driver

    # open the date picker calendar on the page
    def open_calendar(self):
        # wait until the calendar trigger is clickable
        calendar_trigger = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "calendar-trigger"))
        )
        calendar_trigger.click()
        time.sleep(1)

    # select a specific date on the calendar date picker
    def select_date(self, desired_month, desired_date):
        month_locator = (By.CLASS_NAME, "i18n-cal__month")
        # button to get to next month
        next_button_locator = (By.CLASS_NAME, "i18n-cal__control-next")

        month = self.driver.find_element(*month_locator)

        # keep clicking the next button until the desired month is visible
        while desired_month not in month.text:
            # click the next button to go to the next month
            next_button = self.driver.find_element(*next_button_locator)
            next_button.click()

            # wait for the next month to load/simulate human behavior
            time.sleep(1)
            month = self.driver.find_element(*month_locator)
        
        # find the button for the desired date and click it
        date_button_locator = (By.CSS_SELECTOR, f"button.i18n-cal__day[data-date='{desired_date}']")
        date_button = self.driver.find_element(*date_button_locator)
        date_button.click()

        # wait for the page to update/simulate human behavior
        time.sleep(3)

    # fetch all floor plans for a specific apartment type
    def fetch_floor_plans(self, apartment_type):
        floor_plans_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, f"floorplans-{apartment_type}"))
        )
        return floor_plans_container.find_elements(By.CLASS_NAME, "fp-group-item")

    def print_floor_plan_details(self, floor_plans):
        for floor_plan in floor_plans:
            details = {
                "NAME": floor_plan.find_element(By.CLASS_NAME, "fp-name").text,
                "LINK": floor_plan.find_element(By.CLASS_NAME, "fp-name-link").get_attribute("href"),
                "BEDS/BATHS": floor_plan.find_element(By.CSS_SELECTOR, ".fp-col.bed-bath .fp-col-text").text,
                "RENT": floor_plan.find_element(By.CSS_SELECTOR, ".fp-col.rent .fp-col-text").text,
                "SQ.FT": floor_plan.find_element(By.CSS_SELECTOR, ".fp-col.sq-feet .fp-col-text").text,
            }
            for key, value in details.items():
                print(f"{key}: {value}")
            print("\n")

