# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# 1. Открыть страницу http://suninjuly.github.io/file_input.html
# 2. Заполнить текстовые поля: имя, фамилия, email
# 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# 4. Нажать кнопку "Submit"

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = 'http://suninjuly.github.io/file_input.html'

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, os.path.basename(__file__))
    
    browser = webdriver.Chrome()
    browser.get(link)
    
    f_name = browser.find_element(By.NAME, 'firstname')
    f_name.send_keys('Ivan')
    
    l_name = browser.find_element(By.NAME, 'lastname')
    l_name.send_keys('Petrov')
    
    e_mail = browser.find_element(By.NAME, 'email')
    e_mail.send_keys('i.petrov@test.ru')
    
    upload_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    upload_file.send_keys(file_path)
    
    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
    
    
finally:
    time.sleep(5)
    browser.quit()