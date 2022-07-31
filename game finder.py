import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://moodle.ue.poznan.pl/login/index.php")
username_input = browser.find_element("id", "username")
password_input = browser.find_element("id", "password")

username_input.send_keys("numery")
password_input.send_keys("Jnazwa")

login = browser.find_element("id", "loginbtn")
login.click()
