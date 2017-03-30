import time
from random import randint, uniform
from selenium import webdriver
from itertools import repeat

# Add odd shit here
site_list = []

def site_select():
    i = randint(0, len(site_list) - 1)
    return (site_list[i])

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
driver = webdriver.Firefox(firefox_profile=firefox_profile)

# Visits a site, clicks a random number links, sleeps for random spans between
def visit_site():
    new_site = site_select()
    driver.get(new_site)
    print("Visiting: " + new_site)
    time.sleep(uniform(1, 15))

    for i in repeat(None, randint(1, 3)) :
        try:
            links = driver.find_elements_by_css_selector('a')
            l = links[randint(0, len(links)-1)]
            time.sleep(1)
            print("clicking link")
            l.click()
            time.sleep(uniform(0, 120))
        except Exception as e:
            print("Something went wrong with the link click.")
            print(type(e))

while(True):
    visit_site()
    time.sleep(uniform(4, 80))