from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
driver = webdriver.Chrome(service = Service("chromedriver.exe"), options=options)
driver.get("https://www.linkedin.com/login")

user = driver.find_element("name", "session_key")
user.send_keys("*YOUR EMAIL HERE*")
password = driver.find_element("name", "session_password")
password.send_keys("*YOUR PASSWORD HERE*")

driver.get("https://www.linkedin.com/in/*YOUR PROFILE NAME HERE*/edit/forms/skills/new/?profileFormEntryPoint=PROFILE_SECTIONn")

keywords2 = itertools.product(string.ascii_lowercase, repeat = 2)
keywords2 = [''.join(i) for i in keywords2]
keywords3 = itertools.product(string.ascii_lowercase, repeat = 3)
keywords3 = [''.join(i) for i in keywords3]

keywords = [''.join(i) for i in string.ascii_lowercase]
numbers = [str(i) for i in range(99)]

keywords.extend(keywords2)
keywords.extend(numbers)
keywords.extend(keywords3)

skills = []
field = driver.find_element("id", "single-typeahead-entity-form-component-profileEditFormElement-SKILL-AND-ASSOCIATION-skill-ACoAACArEy4BdCpyvAkhN57GqVbjWVJsOWlQ1KA-1-name")

for key in keywords:
    field.clear()
    field.send_keys(key)
    time.sleep(0.8)
   
    try:
        list = driver.find_element("class name", "basic-typeahead__triggered-content")
        skills.extend(list.text.split("\n"))
    except:
        pass 

    try:
        list = driver.find_element("class name", "fb-single-typeahead-entity__triggered-content")
        skills.extend(list.text.split("\n"))
    except:
        pass 

    try:
        list = driver.find_element(By.XPATH, "//div[@role = 'listbox']")
        skills.extend(list.text.split("\n"))
    except:
        pass 

skills = set(skills)

with open('skills.txt', 'w') as f:
    for skill in skills:
        f.write(skill)
