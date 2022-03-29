import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

# paste the chrome driver path in the driver variable
driver = webdriver.Chrome(r" paste the chrome driver path here  ")
driver.get("https://windscribe.com/login")

username = driver.find_element(By.ID , "username")
password = driver.find_element(By.ID , "pass")
login = driver.find_element(By.ID , "login_button")

# paste your account details here
username.send_keys(" paste your windscribe username account here ")
password.send_keys(" paste your windscribe password account here ")
login.click()

download = driver.find_element_by_partial_link_text("Download")
download.click()

OpenVPN  = driver.find_element_by_partial_link_text("OpenVPN")
OpenVPN.click()

protocol = driver.find_element(By.ID , "protocol")
proto = Select(protocol)
proto.select_by_value("udp")

port = driver.find_element(By.ID , "port")
po = Select(port)
po.select_by_value("443")

version = driver.find_element(By.ID , "version")
ver = Select(version)
ver.select_by_value("3b")

location = driver.find_element(By.ID , "location")
loc = Select(location)
option = loc.options
for opt in option :
    opt.click()
    po.select_by_value("443")
    time.sleep(1)
    download = driver.find_element(By.ID , "get_config")
    download.click()
