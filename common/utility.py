import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_time_stamp():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)


def get_usd_jpy():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://info.finance.yahoo.co.jp/fx/')
    usd_jpy = driver.find_element(By.ID, 'USDJPY_top_bid').text
    driver.quit()
    return usd_jpy
