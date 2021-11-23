# Задание: принимаем alert
# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
# 2. Нажать на кнопку
# 3. Принять confirm
# 4. На новой странице решить капчу для роботов, чтобы получить число с ответом

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.TAG_NAME, 'button.btn').click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    submit_button = browser.find_element(By.TAG_NAME, 'button.btn').click()
    
finally:
    time.sleep(5)
    browser.quit()