# Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

# Напишите код, который реализует следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    
    
    dropdown_list = Select(browser.find_element(By.ID, 'dropdown'))
    dropdown_list.select_by_value(str(num1 + num2))
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
    
finally:
    time.sleep(5)
    browser.quit()