from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[3]/a[4]")))
assert "Филе Люминесцентного тетраодонтимформа" == driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[3]/a[4]/p").text

driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[2]")))
assert "Соус фирменный Space Sauce" == driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[2]/p").text

driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]")))
assert "Флюоресцентная булка R2-D3" == driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[1]/p").text

driver.quit()
