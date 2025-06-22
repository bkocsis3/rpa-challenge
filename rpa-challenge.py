#imports
import pandas as pd #module for datasets
import requests #for download
from selenium.webdriver.common.by import By #for find element by
from selenium import webdriver #for webdriver
from pathlib import Path #to find users download folder
import ctypes #for instructional delays

#open rpa challenge site
url = "https://rpachallenge.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#pause for instructions
ctypes.windll.user32.MessageBoxW(0, "The automation has been paused so you can get familiar with the challenge. Click Ok when you're ready to start.", "Quick Pause", 1)

#download excel data
download_url = "https://rpachallenge.com/assets/downloadFiles/challenge.xlsx"
download_folder = str(Path.home() / "Downloads")
file_name = download_folder + "\challenge.xlsx"
download = requests.get(download_url)
with open(file_name, 'wb') as f:
    f.write(download.content)

#read data
data = pd.read_excel(file_name)

#start challenge
challenge_button = driver.find_element(By.XPATH, '//button')
challenge_button.click()

#begin main process loop
for index in data.index:
    email = driver.find_element(By.XPATH, "//div[label[contains(., 'Email')]]/input")
    phone = driver.find_element(By.XPATH, "//div[label[contains(., 'Phone Number')]]/input")
    address = driver.find_element(By.XPATH, "//div[label[contains(., 'Address')]]/input")
    first = driver.find_element(By.XPATH, "//div[label[contains(., 'First Name')]]/input")
    last = driver.find_element(By.XPATH, "//div[label[contains(., 'Last Name')]]/input")
    role = driver.find_element(By.XPATH, "//div[label[contains(., 'Role in Company')]]/input")
    company = driver.find_element(By.XPATH, "//div[label[contains(., 'Company Name')]]/input")
    submit = driver.find_element(By.XPATH, "//*[@value='Submit']")

    email.send_keys(str(data['Email'][index]))
    phone.send_keys(str(data['Phone Number'][index]))
    address.send_keys(str(data['Address'][index]))
    first.send_keys(str(data['First Name'][index]))
    last.send_keys(str(data['Last Name '][index]))
    role.send_keys(str(data['Role in Company'][index]))
    company.send_keys(str(data['Company Name'][index]))
    submit.click()
    
#pause and close
ctypes.windll.user32.MessageBoxW(0, "Nice work! Click Ok when you're ready to close.", "Quick Pause", 1)
driver.quit()