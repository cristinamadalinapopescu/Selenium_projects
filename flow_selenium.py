import select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import webbrowser
import time

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.magnolia.ro/')
driver.implicitly_wait(1)

elem = WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[5]/div/a')))
elem.click()

driver.find_element(By.XPATH, '//*[@id="whiteMenu"]/div/div/ul[1]/li[1]/div/a').click()
print('CLICKED')
time.sleep(2)

url1 = 'https://www.magnolia.ro/buchet-red-passion-5935.html'
driver.get(url1)

elem = driver.find_element(By.ID, 'unde')
elem.clear()
elem.send_keys('Bucuresti')
driver.find_element(By.XPATH,
                    '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[1]/div[2]/div/ul/li[1]/a').click()
elem.send_keys(Keys.RETURN)
print('Localitatea a fost introdusa')
time.sleep(2)

driver.find_element(By.XPATH, '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[3]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[3]/section/div/div[1]/div[1]/ul/li[1]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,
                    '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[3]/section/div/div[1]/div[2]/ul/li[1]/a').click()
driver.find_element(By.XPATH, '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[4]/div/a/i').click()
time.sleep(1)
driver.find_element(By.XPATH,
                    '/html/body/section[2]/div/form/div/div[2]/div/div[3]/div[4]/ul/li/div/div[2]/label/figure/img').click()
time.sleep(2)
driver.find_element(By.ID, 'add_button').click()
print('Produsul a fost adaugat in cos')
time.sleep(2)


driver.find_element(By.XPATH,
                    '/html/body/section[2]/div[2]/form/div/div/div[2]/div[3]/div[2]/table/tbody/tr/td/div[1]/div/div[1]/div[1]/img').click()
time.sleep(2)


driver.find_element(By.XPATH,
                    '/html/body/section[2]/div[2]/form/div/div/div[2]/div[3]/div[2]/table/tbody/tr/td/div[2]/div/div/div[1]/div/div[4]/button[1]').click()
time.sleep(1)


driver.find_element(By.XPATH, '/html/body/section[2]/div[2]/form/div/div/div[2]/div[3]/div[2]/table/tbody/tr/td/div[2]/a/img').click()
print('A fost adaugata o cutie cu ciocolata.')
time.sleep(4)
driver.quit()
