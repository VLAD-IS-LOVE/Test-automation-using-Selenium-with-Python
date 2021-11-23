# Задание: ждем нужный текст на странице
# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
# Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import math, time

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 13).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    
    book_button = browser.find_element(By.ID, 'book').click()
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    submit_button = browser.find_element(By.ID, 'solve').click()
    
finally:
    time.sleep(10)
    browser.quit()
    
    