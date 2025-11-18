import re

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.b144.co.il/%D7%94%D7%97%D7%9C%D7%A7%D7%95%D7%AA-%D7%A9%D7%99%D7%A2%D7%A8/")

pattern = r'<meta name="image" property="og:image" content="(.*?)">'

text = driver.page_source
match = re.search(pattern, text)

if match:
    url = match.group(1)
    print(url)

try:
    driver.get(url)

except :
    pass