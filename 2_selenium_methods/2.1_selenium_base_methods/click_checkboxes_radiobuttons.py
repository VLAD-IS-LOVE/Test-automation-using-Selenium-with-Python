# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)  

# Ваша программа должна выполнить следующие шаги:

# 1. Открыть страницу http://suninjuly.github.io/math.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x (код для этого приведён ниже).
# 4. Ввести ответ в текстовое поле.
# 5. Отметить checkbox "I'm the robot".
# 6. Выбрать radiobutton "Robots rule!".
# 7. Нажать на кнопку Submit.

from selenium import webdriver
import time, math

link = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    
    input_field = browser.find_element_by_id('answer')
    input_field.send_keys(y)
    
    robotCheckbox = browser.find_element_by_id('robotCheckbox') 
    robotCheckbox.click()
    
    robotsRule = browser.find_element_by_id('robotsRule') 
    robotsRule.click()
      
    submit_button = browser.find_element_by_css_selector('.btn.btn-default') 
    submit_button.click() 
    
finally:
    time.sleep(5)
    browser.quit()