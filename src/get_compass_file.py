from os import path, environ, makedirs, listdir
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import NBIN_URL, DOWNLOADS_FOLDER
DOWNLOAD_DIR = path.abspath(DOWNLOADS_FOLDER)


def get_file_from_compass():
    """
    Downloads a file from the NBCN Compass system.
    Requires environment variables 'username' and 'password' to be set.
    """

    username = 'ETFCAP1'
    password = 'Password2'

    if not path.exists(DOWNLOAD_DIR):
        makedirs(DOWNLOAD_DIR)

    options = Options()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", DOWNLOAD_DIR)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                           "application/pdf,application/octet-stream,text/csv,application/vnd.ms-excel")

    driver = webdriver.Firefox(options=options)
    try:
        driver.set_window_size(710, 920)
        driver.get(NBIN_URL)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.NAME, "userid"))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)
        wait.until(EC.element_to_be_clickable((By.NAME, "SUBMIT"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "downloadButton0"))).click()
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()
        time.sleep(2)

    finally:
        driver.quit()


def get_last_downloaded_file(download_dir=DOWNLOAD_DIR, printer=True):
    """
    Returns the name of the most recently downloaded file in the specified directory.
    """
    files = [path.join(download_dir, f) for f in listdir(download_dir)]
    if not files:
        return None
    last_file = max(files, key=path.getmtime)
    if last_file:
        if printer:
            print(f"Last downloaded file: {last_file}")
        return path.basename(last_file)
    else:
        raise AttributeError("No files downloaded yet.")