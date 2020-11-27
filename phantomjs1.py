#브라우저 안띄우고 조용히 작업
import time
from selenium import webdriver
def getPw():
    with open('D:\\pw.txt') as f:
        pw=f.readline()
    return pw.strip()

# driver=webdriver.PhantomJS('data\\phantomjs')
driver=webdriver.PhantomJS('data\\phantomjs')
#넷플릭스
url='https://www.netflix.com/kr/login'
driver.get(url)
time.sleep(1)
idbox=driver.find_element_by_css_selector('#id_userLoginId')
idbox.send_keys('jinjinlee54@naver.com')
time.sleep(1)
pwbox=driver.find_element_by_css_selector('#id_password')
pwbox.send_keys(getPw())
time.sleep(1)

btn=driver.find_element_by_css_selector('#appMountPoint > div > div.login-body > div > div > div.hybrid-login-form-main > form > button')
btn.click()
time.sleep(1)

profil=driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.profiles-gate-container > div > div > ul > li:nth-child(3) > div > a')
profil.click()
time.sleep(1)

# driver.get('https://www.netflix.com/browse/my-list')
zzim=driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.pinning-header > div > div > ul > li:nth-child(6) > a')
zzim.click()
time.sleep(1)
# titles=driver.find_element_by_css_selector('#title-card-0-0 > div.ptrack-content > a')
# print(titles.text)

# titles=driver.find_elements_by_class_name('slider-refocus')
titles=driver.find_elements_by_css_selector('div.ptrack-content > a')
for title in titles:
    print(title.get_attribute('aria-label'))