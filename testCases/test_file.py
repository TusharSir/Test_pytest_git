import time

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
service_obj = Service()

def pytest_configure(config):
    config._metadata ['Project Name'] = 'nop Commerce'
    config._metadata ['Module Name'] = 'Customer'
    config._metadata ['Tester'] = 'Tushar'

@pytest.mark.optionalhook
def pytest_metadata (metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)

class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
   # @pytest.mark.sanity
    def test_sum_001(self):
        a = 3
        b = 4
        sum = a+ b
        if sum == 7:
            assert True
            print("test_sum_001 is pass")
        else:
            assert False
            print("test_sum_001 is Fail")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_mul_002(self):
        a = 3
        b = 4
        mul = a * b
        if mul == 12:
            assert True
            print("test_mul_002 is pass")
        else:
            assert False
            print("test_mul_002 is Fail")



    @allure.title('My test title')
    @allure.description('My test description')
    @allure.feature('My feature name')
    @allure.story('My story name')
    @allure.issue('https://github.com/pytest-dev/pytest/issues/123')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip
    def test_googletitle_003():
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.get("https://www.google.com/")
        Title = driver.title
        if Title == "Google":
            assert True
            print("test_googletitle_003 is pass")
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        else:
            assert False
            print("test_googletitle_003 is Fail")
        driver.close()

    @allure.severity(allure.severity_level.MINOR)
    #@pytest.mark.xfail
    def test_internetspeed_004(self):
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.get("https://fast.com/")
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        Title = driver.title
        print(Title)
        if Title == "Internet Speed Test | Fast.com":
            time.sleep(12)
            InternetSpeed =(driver.find_element(By.XPATH,"//div[@id='speed-value']").text)
            print ( "Your internet speed is " + InternetSpeed)
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            Title = driver.title
            assert True
            print("test_googletitle_003 is pass")
        else:
            assert False
            print("test_googletitle_003 is Fail")
        driver.close()

#     def test_SaerchCredence_005(self):
#         driver = webdriver.Chrome(service=service_obj, options=chrome_options)
#         driver.get("https://www.google.com/")
# #        time.sleep(4)
# #        driver.find_element(By.XPATH, "https://www.google.com/").click()
#         time.sleep(2)
#         driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("credence it professional training institute")
#   #      time.sleep(4)
# #        driver.find_element(By.XPATH, "//body/div[@class='L3eUgb']/div[@class='o3j99 ikrT4e om7nvf']/form[@role='search']/div[1]").click()
#         driver.close()

    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.xfail
    def test_sum_006(self):
        a = 3
        b = 4
        sum = a+ b
        if sum == 7:
            assert True
            print("test_sum_006 is pass")
        else:
            assert False
            print("test_sum_006 is Fail")

    @allure.severity(allure.severity_level.CRITICAL)
    #@pytest.mark.xfail
    def test_sum_007(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
            print("test_sum_007 is pass")
        else:
            assert False
            print("test_sum_007 is Fail")


    def test_sum_008(self):
        a = 3
        b = 4
        sum = a + b
        if sum == 7:
            assert True
            print("test_sum_008 is pass")
        else:
            assert False
            print("test_sum_008 is Fail")

    def test_sum_009(self):
        a = 3
        b = 4
        sum == a + b
        if sum != 8:
            assert True
            print("test_sum_009 is pass")
        else:
            assert False
            print("test_sum_009 is Fail")
