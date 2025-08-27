import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from os import path, environ, makedirs
import time

[Environment]::SetEnvironmentVariable("username", "ETFCAP1", "User")
[Environment]::SetEnvironmentVariable("password", "Password2", "User")



def get_file_from_compass():
    """
    Downloads a file from the NBCN Compass system.
    Requires environment variables 'username' and 'password' to be set.
    """
    # if 'username' not in environ or 'password' not in environ:
    #     raise EnvironmentError("Environment variables 'username' and 'password' must be set.")
    
    download_dir = path.abspath("downloads")
    if not path.exists(download_dir):
        makedirs(download_dir)

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
        wait.until(EC.presence_of_element_located((By.NAME, "userid"))).send_keys('ETFCAP1')
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys('Password2')
        wait.until(EC.element_to_be_clickable((By.NAME, "SUBMIT"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "downloadButton0"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
        time.sleep(2)

    finally:
        driver.quit()


def get_last_downloaded_file(download_dir):
    """
    Returns the name of the most recently downloaded file in the specified directory.
    """
    files = [os.path.join(download_dir, f) for f in os.listdir(download_dir)]
    if not files:
        return None  # No files in the directory

    # Get the file with the latest modification time
    latest_file = max(files, key=os.path.getmtime)
    return os.path.basename(latest_file)


if __name__ == "__main__":
    get_file_from_compass()