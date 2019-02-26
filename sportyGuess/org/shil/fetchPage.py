'''
Created on 2019Feb24

@author: yuanshun.sl
'''
from selenium import webdriver
from org.shil.db import team_statistics
import time
import random

# print('this is my first python code i know nothing i will put everything in this file because i dont know what should i do good luck to me LOL')

sleepMin = 3;
sleepMax = 8;
url = "https://www.whoscored.com/Teams/65"

browser = webdriver.Chrome()
browser.get(url);

time.sleep(random.randrange(sleepMin,sleepMax))


print("$TeamName Statistics")

'''

print("Summary - Overall")
ttss = browser.find_element_by_id('top-team-stats-summary')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)
    print(element.find_elements_by_css_selector("td")[8].text)
    

print("Summary - Home")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Home):
        a.click()
        break
    
time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-summary')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)
    print(element.find_elements_by_css_selector("td")[8].text)

print("Summary - Away")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Away):
        a.click()
        break

time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-summary')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)
    print(element.find_elements_by_css_selector("td")[8].text)
    

print("Defensive - Overall")

defensive = browser.find_element_by_link_text(team_statistics.type_Defensive);
defensive.click()

time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-defensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)


print("Defensive - Home")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Home):
        a.click()
        break
    
time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-defensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)

print("Defensive - Away")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Away):
        a.click()
        break

time.sleep(random.randrange(sleepMin,sleepMax))
    
ttss = browser.find_element_by_id('top-team-stats-defensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)


print("Offensive - Overall")

offensive = browser.find_element_by_link_text(team_statistics.type_Offensive);
offensive.click()

time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-offensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)


print("Offensive - Home")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Home):
        a.click()
        break
    
time.sleep(random.randrange(sleepMin,sleepMax))

ttss = browser.find_element_by_id('top-team-stats-offensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)

print("Offensive - Away")

listbox = ttss.find_element_by_id('field')
dds = listbox.find_elements_by_tag_name('dd')
for dd in dds:
    a = dd.find_element_by_tag_name('a')
    if(a.text == team_statistics.view_Away):
        a.click()
        break

time.sleep(random.randrange(sleepMin,sleepMax))
    
ttss = browser.find_element_by_id('top-team-stats-offensive')
trs = ttss.find_element_by_id("top-team-stats-summary-content")
elements = trs.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    print(element.find_elements_by_css_selector("td")[5].text)
    print(element.find_elements_by_css_selector("td")[6].text)


'''

print('Team Fixtures')

fixtures_but = browser.find_element_by_id('sub-navigation').find_element_by_link_text("Fixtures")
fixtures_but.click()

time.sleep(random.randrange(sleepMin,sleepMax))

fixtures = browser.find_element_by_id('team-fixtures')
elements = fixtures.find_elements_by_tag_name("tr")
for element in elements:
    print(element.find_elements_by_css_selector("td")[0].text)
    print(element.find_elements_by_css_selector("td")[1].text)
    print(element.find_elements_by_css_selector("td")[2].text)
    print(element.find_elements_by_css_selector("td")[3].text)
    print(element.find_elements_by_css_selector("td")[4].text)
    sed = element.find_elements_by_css_selector("td")[5]
    at = sed.find_element_by_tag_name('a')
    print(at.text)
    print(element.find_elements_by_css_selector("td")[6].text)
    print(element.find_elements_by_css_selector("td")[7].text)
    print(element.find_elements_by_css_selector("td")[8].text)
    


browser.quit()