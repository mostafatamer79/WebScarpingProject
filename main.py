import time

import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
addre = []
link = []
money = []
website = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(website.text,'html.parser')
properties = soup.select("#grid-search-results > ul")
for property in properties:
    addresses = property.findAll(name="address")
    linkes = property.findAll(name='a',href=True)
    prices = property.findAll(name='span',class_ = "PropertyCardWrapper__StyledPriceLine")
    for price in prices:
        money.append(price.get_text(strip=True)[:6])
    for lin in linkes:
        link.append(lin['href'])
    for address in addresses:
        addre.append(address.get_text(strip=True))

# setup seleium
driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_option)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfXZtNL2HIx4V9deyUaqGX8RLTl1uTcJU63t5tc2HIff3dekQ/viewform")
wait = WebDriverWait(driver, 10)

for i in range(len(addre)):
    property_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    submit = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))

    # Fill inputs
    property_input.send_keys(addre[i])
    price_input.send_keys(money[i])
    link_input.send_keys(link[i])
    submit.click()

    # Wait for the "another form" button
    another_form = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")))
    another_form.click()