import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp():
    global name,driver,director,year,distributor,producer
    name=input("Enter your movie name-:")
    year=input("Enter year of release-:")
    director=input("Enter director name-:")
    distributor=input("Enter distributor name-:")
    producer=input("Enter producer name-:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_form(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    driver.find_element_by_name("mname").send_keys(name)
    time.sleep(2)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(2)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(2)
    driver.find_element_by_name("mdist").send_keys(distributor)
    time.sleep(2)
    driver.find_element_by_name("mproducer").send_keys(producer)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    time.sleep(2)
    driver.find_element_by_name("subbtn").click()
    time.sleep(2)