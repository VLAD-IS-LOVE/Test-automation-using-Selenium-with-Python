# Задание:

#Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button") после открытия страницы http://suninjuly.github.io/cats.html?

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/cats.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.ID, 'button')
    
finally:
    browser.quit()

