from Controller.sepBrowserController import *


options = webdriver.ChromeOptions()

options.add_experimental_option("debuggerAddress", f"127.0.0.1:29688")

service = Service(executable_path="./chromedriver/128.exe")

# Lấy cái gì để điều khiển

driver = webdriver.Chrome(options=options, service=service)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@data-at='account_btn']"))).click()

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//button[@data-at='sign_out_button']"))).click()

e = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,"//button[@data-at='sign_out_button']")))
driver.execute_script("arguments[0].click();", e)