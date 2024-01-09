from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass



class UtilClass(BaseClass):
    def perform_login(driver):
        email  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"identifierId")))
        email.send_keys("kaymerasqa@gmail.com")
        next  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//span[contains(text(),'Next')]")))
        next.click()
