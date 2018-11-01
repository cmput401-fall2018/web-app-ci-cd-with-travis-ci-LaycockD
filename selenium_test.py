from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_home():
	driver = webdriver.Chrome()
	driver.get("http://162.246.157.216:8000")

	name_elem = driver.find_element_by_id("name")
	about_elem = driver.find_element_by_id("about")
	edu_elem = driver.find_element_by_id("education")
	skills_elem = driver.find_element_by_id("skills")
	work_elem = driver.find_element_by_id("work")
	contact_elem = driver.find_element_by_id("contact")

	assert name_elem != None
	assert about_elem != None
	assert edu_elem != None
	assert skills_elem != None
	assert work_elem != None
	assert contact_elem != None

test_home()
