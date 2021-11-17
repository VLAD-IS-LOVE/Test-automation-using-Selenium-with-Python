# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:

# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с # сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    img_element = browser.find_element(By.ID, 'treasure')
    x = img_element.get_attribute('valuex')
    y = calc(x)
    
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    
    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()
    
    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()
    
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
         
finally:
    time.sleep(5)
    browser.quit()