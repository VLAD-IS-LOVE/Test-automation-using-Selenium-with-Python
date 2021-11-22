# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

# 1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
# 2. Считать значение для переменной x.
# 3. Посчитать математическую функцию от x.
# 4. Проскроллить страницу вниз.
# 5. Ввести ответ в текстовое поле.
# 6. Выбрать checkbox "I'm the robot".
# 7. Переключить radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://SunInJuly.github.io/execute_script.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)
    
    robotsRule = browser.find_element(By.ID,'robotsRule')  
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    robotCheckbox = browser.find_element(By.ID,'robotCheckbox') 
    robotCheckbox.click()
    
    submit_button = browser.find_element(By.TAG_NAME,'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button) 
    submit_button.click() 

finally:
    time.sleep(5)
    browser.quit()
