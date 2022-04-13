from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Selenium用オプション
options = webdriver.ChromeOptions()
options.binary_location = "/opt/headless/python/bin/headless-chromium"
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--single-process")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280x1696")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-infobars")
options.add_argument("--hide-scrollbars")
options.add_argument("--enable-logging")
options.add_argument("--log-level=0")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--homedir=/tmp")

driver = webdriver.Chrome(executable_path="/opt/headless/python/bin/chromedriver", chrome_options=options)


def scrape(selector, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return driver
    driver.quit()
