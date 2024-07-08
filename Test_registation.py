from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

email = random.randint(20,90)
password = random.randint(10000, 99999)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Anton")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(f'Anton_Kazakov_{email}@yandex.ru')
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")))

assert "Некорректный пароль" == driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("6")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

driver.quit()