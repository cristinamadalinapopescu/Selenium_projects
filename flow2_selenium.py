from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.saucedemo.com/')
driver.implicitly_wait(1)
driver.fullscreen_window()
username = driver.find_element(By.ID, 'user-name')
username.send_keys('standard_user')
time.sleep(2)

verify_pass = driver.find_element(By.NAME, 'password')
verify_pass.send_keys('secret_sauce')
print('Now you are ready to buy things')
time.sleep(3)

login_verify = driver.find_element(By.NAME, 'login-button')
login_verify.send_keys(Keys.RETURN)

sorter_options = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[2]/span/select').click()
time.sleep(2)
option_chose1 = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[3]')))
option_chose1.click()
print('Price low to high was selected.')
time.sleep(2)

option_chose2 = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div[2]/span/select/option[4]')))
option_chose2.click()
print('Price high to low was selected.')
time.sleep(2)

select_product = driver.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/a/div').click()
time.sleep(3)

driver.execute_script("window.history.go(-1)")
time.sleep(3)

product_chose = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[5]/div[1]/a/img').click()
time.sleep(3)

add_product1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
time.sleep(2)

cart_view = driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
time.sleep(3)

continue_shopping = driver.find_element(By.NAME, 'continue-shopping').click()
time.sleep(2)

add_product2 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
time.sleep(3)

remove_product2 = driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
time.sleep(3)

cart_view2 = driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
time.sleep(3)

checkout = driver.find_element(By.NAME, 'checkout').click()
time.sleep(2)

first_name = driver.find_element(By.ID, 'first-name')
first_name.send_keys('Leona')
time.sleep(1)

last_name = driver.find_element(By.ID, 'last-name')
last_name.send_keys('Veza')
time.sleep(1)

zip_code = driver.find_element(By.ID, 'postal-code')
zip_code.send_keys('237288')
time.sleep(2)

order = driver.find_element(By.ID, 'continue')
order.send_keys(Keys.RETURN)
time.sleep(3)

finish_order = driver.find_element(By.ID, 'finish')
finish_order.send_keys(Keys.RETURN)
print('Your order has been placed successfully!')
time.sleep(3)

driver.get_screenshot_as_file('screen.png')
print('Screenshot captured successfully!')
time.sleep(3)

back_home = driver.find_element(By.NAME, 'back-to-products').click()
time.sleep(3)

go_to_logout = driver.find_element(By.ID, 'react-burger-menu-btn').click()
time.sleep(2)

logout = driver.find_element(By.ID, 'logout_sidebar_link').click()
time.sleep(2)

driver.find_element(By.NAME, 'login-button').click()
assert 'Epic sadface: Username is required' in driver.page_source
print('The error message is displayed.')
time.sleep(3)

username2 = driver.find_element(By.NAME, 'user-name')
username2.send_keys('locked_out_user')
time.sleep(1)

verify2_pass = driver.find_element(By.NAME, 'password')
verify2_pass.send_keys('secret_sauce')
time.sleep(2)

login_verify2 = driver.find_element(By.NAME, 'login-button')
login_verify2.send_keys(Keys.RETURN)
assert 'Epic sadface: Sorry, this user has been locked out.' in driver.page_source
print('The error message is displayed.')
time.sleep(4)

username3 = driver.find_element(By.NAME, 'user-name')
username3.clear()
time.sleep(2)
username3.send_keys('problem_user')
time.sleep(1)

verify3_pass = driver.find_element(By.NAME, 'password')
verify3_pass.clear()
time.sleep(2)
verify3_pass.send_keys('secret_sauce')
time.sleep(3)

login_verify3 = driver.find_element(By.NAME, 'login-button')
login_verify3.send_keys(Keys.RETURN)
time.sleep(3)
driver.close()