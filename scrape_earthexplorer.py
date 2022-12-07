from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = ''
password = ''

driver = webdriver.Chrome()

# Login.
driver.get('https://ers.cr.usgs.gov/login')

username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys(password)

login_button = driver.find_element(By.ID, 'loginButton')
login_button.click()

# Navigate to SRTM 1 Arc-Second results.
driver.get('https://earthexplorer.usgs.gov/')

datasets_tab = driver.find_element(By.ID, 'tab2')
datasets_tab.click()

time.sleep(3)

digital_elevation_li = driver.find_element(By.ID, 'cat_207')
digital_elevation_expander = digital_elevation_li.find_element(By.CLASS_NAME, 'folder');
digital_elevation_expander.click()

srtm_li = driver.find_element(By.ID, 'cat_1103')
srtm_expander = srtm_li.find_element(By.CLASS_NAME, 'folder')
srtm_expander.click()

one_arcsecond_checkbox = driver.find_element(By.ID, 'coll_5e83a3ee1af480c5')
one_arcsecond_checkbox.click()

results_tab = driver.find_element(By.ID, 'tab4')
results_tab.click()

time.sleep(3)

# Download SRTM heightmaps.
download_options_buttons = driver.find_elements(By.CLASS_NAME, 'download')

for k in range(1428):
    for i in range(len(download_options_buttons)):
        download_options_buttons[i].click()

        time.sleep(3)

        download_options_container = driver.find_element(By.ID, 'optionsContainer')
        download_buttons = download_options_container.find_elements(By.CLASS_NAME, 'downloadButtons')
        geotiff_download_button = download_buttons[2]
        geotiff_download_button.click()

        time.sleep(3)

        close_button = driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/button')
        close_button.click()

        time.sleep(10)

    time.sleep(50)
    next_button = driver.find_element(By.ID, '2_5e83a3ee1af480c5')
    next_button.click()

time.sleep(10)


