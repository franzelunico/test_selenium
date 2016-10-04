import time
from selenium import webdriver


class ScrapingPage(object):
    def __init__(self):
        print "Hello"

    def user(self):
        file = open('data.txt')
        lines = file.read().splitlines()
        self.name = lines[0]
        self.password = lines[1]
        file.close()

    def loadDriver(self):
        path = './chromeDriver/chromedriver'
        # self.driver = webdriver.Chrome(path)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path=path,
                                       chrome_options=chrome_options)

    def login(self):
        self.driver.get('https://www.facebook.com/login.php/')
        username = self.driver.find_element_by_name('email')
        username.send_keys(self.name)

        password = self.driver.find_element_by_name('pass')
        password.send_keys(self.password)

        login_button = self.driver.find_element_by_name('login')
        login_button.click()

    def scraping(self):
        self.driver.get('https://www.facebook.com/thehackernews/')
        thelist = []
        # get Post
        for item in self.driver.find_elements_by_tag_name('a'):
            ahref = item.get_attribute("href")
            links = "https://www.facebook.com/ufi/"
            if ahref is not None and ahref.find(links) > -1:
                thelist.append(item.get_attribute("href"))
        self.driver.get(thelist[0])

    def despliegue(self):
        css = 'uiMorePagerPrimary'
        for item in self.driver.find_elements_by_class_name(css):
            item.click()
            time.sleep(5)

    def run(self):
        self.user()
        self.loadDriver()
        self.login()
        self.scraping()
        time.sleep(5)
        self.despliegue()

if __name__ == "__main__":
    app = ScrapingPage()
    app.run()
