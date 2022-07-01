from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website="https://selenium-python.readthedocs.io/index.html"
path="I:\Python\pythonSelenium\chromedriver"
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)
driver.get(website)