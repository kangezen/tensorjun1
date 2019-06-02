from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

class NaverMovie:
    def __init__(self, url):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        #한 줄 코딩 driver. 컨트롤 스페이스
        #print(driver.find_element_by_class_name(''))
        #print(driver.find_element_by_id('mflick'))
        # print(driver.find_element_by_class_name('flick_view_area flick-view'))
        print(soup)


