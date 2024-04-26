from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint


def auto_register(count):
    # Открываем текстовые файлы где лежать наши логины и пароли
    with open('login_email.txt', 'r') as l_email:
        login = l_email.read()
    with open('password.txt', 'r') as l_pass:
        password = l_pass.read()
        
    # Создаем экземпляр браузера
    driver = webdriver.Chrome()

    # Открываем страницу регистрации
    driver.get("https://ru.4game.com/signup/")  # Замените на реальный URL
    html_code = driver.page_source
    # time.sleep(10)

    # Находим поля и заполняем
    login_email = f'{login}+{count}@gmail.com'
    email_field = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='email']"))
        )
    email_field.clear()  
    email_field.send_keys(login_email)  

    password_field = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
        )
    password_field.clear()  
    password_field.send_keys(password)  


    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "Checkbox_input__mqggd"))
    )
    driver.execute_script("arguments[0].click();", checkbox)

    # Отправляем форму регистрации
    register_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@data-locator='register-form-button']"))
        )
    driver.execute_script("arguments[0].click();", register_button)
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    
    count = 500
    for _ in range(1):
        try:
            auto_register(count)
            count = count +1
            print(f'уверичен', count)
        except:
            print('Что то пошло не так, пробуем еще.')
        