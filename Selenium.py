from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Page 실행 후 Source 가져오기
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://www.indeed.com/jobs?q=python&limit=50")

print(browser.page_source)