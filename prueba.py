import time
from selenium import webdriver

# Login
driver = webdriver.Chrome('/Users/codebo04/Downloads/chromedriver')
driver.get('https://www.facebook.com/login.php')
search_box = driver.find_element_by_name('email')
search_box.send_keys('email')
search_box1 = driver.find_element_by_name('pass')
search_box1.send_keys('password')
search_box1.submit()
# Page scrapin
driver.get('https://www.facebook.com/thehackernews/')
thelist = []
# get Post
for item in driver.find_elements_by_tag_name('a'):
    ahref = item.get_attribute("href")
    if ahref is not None and ahref.find("https://www.facebook.com/ufi/") > -1:
        thelist.append(item.get_attribute("href"))
driver.get(thelist[0])
time.sleep(30)
driver.quit()

# driver.get('https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=1538171092863425&av=100012901368010')
# # login_form = driver.find_element_by_xpath("//div[@class='_5j0e fsl fwb fcb']/a")
# element2 = driver.find_element_by_xpath("//ul[@class='uiList _5i_n _4kg _6-h _6-j _6-i']")
# print type(element2)
# print len(element2)
# print element2.text
# print help(element2.text)
# # element2.find_element_by_xpath(".//p[@class='test']").text 
# # for item in driver.find_element_by_xpath('//a[contains(@href,"profile.php"]'):
# #     print item
# time.sleep(30)
# driver.quit()
