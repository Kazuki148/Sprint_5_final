driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click() #переход по кнопке «Войти в аккаунт» на главной
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click() #Переход по кнопке Зарегистрироваться
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Anton") #Ввод имени в поле
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Anton_Kazakov_6@yandex.ru") #Ввод email в поле
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("123456") #Ввод пароля в поле
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click() #Финальный переход по кнопке Зарегистрироваться после заполнения всех полей
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click() #Переход по кнопке войти после заполнения email и пароля
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/div/a").click() #переход по клику на Stellar Burgers
driver.find_element(By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p").click() #переход по клику на «Конструктор»
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]").click() #переход по клику на начинки
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]").click() #переход по клику на соусы
driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]").click() #переход по клику на булки