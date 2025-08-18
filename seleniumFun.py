from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path, environ
import time

if __name__ == "__main__":
    download_dir = path.abspath("downloads")

    options = Options()
    options.set_preference("browser.download.folderList", 2)  # custom dir
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/pdf,application/octet-stream,text/csv,application/vnd.ms-excel")

    driver = webdriver.Firefox(options=options)
    try:
        driver.set_window_size(710, 920)
        driver.get("https://filecabinet.nbcn.ca/")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.NAME, "userid"))).send_keys(environ['username'])
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(environ['password'])
        wait.until(EC.element_to_be_clickable((By.NAME, "SUBMIT"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "downloadButton0"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
        time.sleep(2)

    finally:
        driver.quit()
