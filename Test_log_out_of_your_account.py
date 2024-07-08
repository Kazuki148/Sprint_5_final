from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Anton_Kazakov_6@yandex.ru")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456")
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[2]/div/button")))
assert "Оформить заказ" == driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]/a")))
assert "Профиль" == driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]/a").text

driver.find_element(By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/form/button")))
assert "Войти" == driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").text

driver.quit()
