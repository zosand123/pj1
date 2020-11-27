from selenium import webdriver
import time
#웹드라이버:크롤러와 브라우져를 연결시켜주는 프로그램
#크롬드라이버 다운로드 ChromeDriver 81.0.4044.138
# driver.get(url)
# driver.find_element_by_class_name()
# driver.find_elements_by_class_name()
# driver.find_element_by_css_selector()
# driver.find_elements_by_css_selector()
#...
#마우스제어 click()
#키보드제어 send_keys()
#자바스크립트 실행 execute_script()
# driver=webdriver.Chrome('data\\chromedriver')
# url='https://pjt3591oo.github.io/'
# driver.get(url) # 해당페이지 접속
# print('현재페이지소스 : ',driver.page_source)
# print('현재url : ',driver.current_url)
# print('title tag : ',driver.title)
# a=driver.find_element_by_css_selector('body > main > div > div > div:nth-child(9) > h3 > a')
# print(a.tag_name)
# print(a.text)
# a.click()

#search로 들어가서 python검색하기
# time.sleep(1)
# search=driver.find_element_by_css_selector('body > header > div > nav > div > a:nth-child(4)')
# search.click()
# box=driver.find_element_by_css_selector('#search-box')
# box.send_keys('python')
# btn=driver.find_element_by_css_selector('input[type=submit]:nth-child(3)')
# #selector를 적절히 수정하여 간단하게 쓰는것도 좋다
# btn.click()
# titles=driver.find_elements_by_css_selector('#search-results > li > a > h3')
# for title in titles:
#     print(title.text)

def getPw():
    with open('D:\\pw.txt') as f:
        pw=f.readline()
    return pw.strip()
driver=webdriver.Chrome('data\\chromedriver')
# url='https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
# driver.get(url)
# idbox=driver.find_element_by_css_selector('#id')
# idbox.send_keys('zosand123')
# pwbox=driver.find_element_by_css_selector('#inputPwd')
# pwbox.send_keys(getPw())
# btn=driver.find_element_by_css_selector('#loginBtn')
# btn.click()
# mailbox=driver.find_element_by_css_selector('#mArticle > div.feature_tmp > div.login_tmp.login_my > ul > li:nth-child(1) > a')
# mailbox.click()

#넷플릭스로 들어간다
url='https://www.netflix.com/kr/login'
driver.get(url)
time.sleep(1)

#아이디랑 비번입력 : 비번을 그냥 입력하긴 보안상 안좋아서 메모장에 저장후 가져와서 넣기
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

driver.get('https://www.netflix.com/browse/my-list') #::after 가아닐때 driver.get으로도 갈수있다/
                                                     #클릭이나 driver.get 둘줄에 하나만 쓰면됨
# zzim=driver.find_element_by_css_selector('#appMountPoint > div > div > div:nth-child(1) > div.bd.dark-background > div.pinning-header > div > div > ul > li:nth-child(6) > a')
# zzim.click()
time.sleep(1)
#
titles=driver.find_elements_by_class_name('slider-refocus')
titles=driver.find_elements_by_css_selector('div.ptrack-content > a')
for title in titles:
    print(title.get_attribute('aria-label'))
