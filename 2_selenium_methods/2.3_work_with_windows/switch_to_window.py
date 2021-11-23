# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    time.sleep(2)
    
    button = browser.find_element(By.TAG_NAME, 'button.btn').click()
    
    browser.switch_to.window(browser.window_handles[1])
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    submit_button = browser.find_element(By.TAG_NAME, 'button.btn').click()
    
finally:
    time.sleep(5)
    browser.quit()