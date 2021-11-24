from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class TestRegistration(unittest.TestCase):
    
    def test_reg1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(
            By.XPATH, "//*[contains(text(), 'First name')]/../input")
        first_name.send_keys('Ivan')
        
        last_name = browser.find_element(
            By.XPATH, "//*[contains(text(), 'Last name')]/../input")
        last_name.send_keys('Petrov')
        
        e_mail = browser.find_element(
            By.XPATH, "//*[contains(text(), 'Email')]/../input")
        e_mail.send_keys('i.petrov@dot.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        expected_result = 'Congratulations! You have successfully registered!'  
        actual_result = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(
            expected_result, actual_result, "Should be successful message in reg 1!")
    
    def test_reg2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(
            By.XPATH, "//*[contains(text(), 'First name')]/../input")
        first_name.send_keys('Ivan')
        
        last_name = browser.find_element(
            By.XPATH, "//*[contains(text(), 'Last name')]/../input")
        last_name.send_keys('Petrov')
        
        e_mail = browser.find_element(
            By.XPATH, "//*[contains(text(), 'Email')]/../input")
        e_mail.send_keys('i.petrov@dot.com')

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        expected_result = 'Congratulations! You have successfully registered!'  
        actual_result = browser.find_element(By.TAG_NAME, "h1").text

        self.assertEqual(
            expected_result, actual_result, "Should be successful message in reg 2!")

if __name__ == "__main__":
    unittest.main()