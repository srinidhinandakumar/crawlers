# crawl google.com to fire a query search
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasicCrawler:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def initdriver(self):
        self.driver.wait = WebDriverWait(self.driver, 5)
        return self.driver

    def spider(self, driver, query):
        driver.get("http://www.google.com")
        try:
            query_box = driver.wait.until(EC.presence_of_element_located((By.NAME, 'q')))
            button = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
            query_box.send_keys(query)
            button.click()
        except TimeoutException:
            print("Query box or Search button not found")


dr = BasicCrawler()
driver = dr.initdriver()
dr.spider(driver, "USC")
time.sleep(5)
driver.quit()
