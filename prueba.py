import time
from selenium import webdriver


class ScrapingPage(object):
    def __init__(self):
        print "Hello"

    def user(self):
        mydata = open('data.txt')
        lines = mydata.read().splitlines()
        self.name = lines[0]
        self.password = lines[1]
        mydata.close()

    def loadDriver(self):
        path = './chromeDriver/chromedriver'
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
        print thelist[0]
        self.driver.get(thelist[0])
        # test
        # link = "https://www.facebook.com/ufi/reaction/profile/browser/"
        # link += "?ft_ent_identifier=1550376058309595&av=100012901368010"
        # self.driver.get(link)

    """ Mespliega la version de like en tu totalidad  """
    def motion(self):
        contenido = self.driver.find_element_by_id('content')
        query = "div>div>div>ul.uiList>li"
        lista_emo = contenido.find_elements_by_css_selector(query)
        for item in lista_emo:
            self.display(item)
        # tam = len(item.find_elements_by_css_selector(css))
        # while tam == 1:
        #     elem = item.find_element_by_css_selector(css)
        #     ahref = elem.get_attribute("href")
        #     links = "reaction_type=1"
        #     if ahref is not None and ahref.find(links) > -1:
        #         elem.click()
        #         time.sleep(10)
        #     tam = len(item.find_elements_by_css_selector(css))
        # elem = item.find_element_by_css_selector(css)

    def display(self, item):
        css = "a.pam.uiBoxLightblue.uiMorePagerPrimary"
        tam = len(item.find_elements_by_css_selector(css))
        while tam == 1:
            elem = item.find_element_by_css_selector(css)
            ahref = elem.get_attribute("href")
            links = "reaction_type"
            if ahref is not None and ahref.find(links) > -1:
                elem.click()
                time.sleep(10)
            tam = len(item.find_elements_by_css_selector(css))

    def capturarLikes(self):
        contenido = self.driver.find_element_by_id('content')
        query = "div>div>div>ul.uiList>li"
        lista_emo = contenido.find_elements_by_css_selector(query)
        print "================================"
        for item in lista_emo:
            "reaction_profile_browser3"
            query = "ul.uiList"
            reaction = item.find_element_by_css_selector(query)
            id_elemt = reaction.get_attribute("id")
            print id_elemt
            lista = item.find_elements_by_css_selector("div>ul>li>div>a")
            for elem in lista:
                ahref = elem.get_attribute("href")
                links = "profile_browser"
                if ahref is not None and ahref.find(links) > -1:
                    print ahref
            print "================================"

    def run(self):
        self.user()
        self.loadDriver()
        self.login()
        self.scraping()
        self.motion()
        self.capturarLikes()
        print 'end display show'

if __name__ == "__main__":
    app = ScrapingPage()
    app.run()
