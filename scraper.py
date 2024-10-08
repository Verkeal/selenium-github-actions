# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# # from webdriver_manager.core.utils import ChromeType
# from webdriver_manager.core.os_manager import ChromeType

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService

chrome_service = ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

# driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('http://nytimes.com')
print(driver.title)
