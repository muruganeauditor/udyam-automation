import string
import sys
import requests

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

api_url = "http://admin.ibuyfresh.in/api/udyamDetails"
response = requests.get(api_url)
apiResponse = response.json()
print(apiResponse['status'])

if apiResponse['status']:
    userData = apiResponse['data'][0]
    locals().update(userData)
else:
    print("Invalid Api response")
    sys.exit()

# {"data":[{"id":1,"name":"Murugan palani","email":"muruganaccetcse@gmail.com","mobile":"9585393730","aadhaar":"217298315618","social_category":"General","gender":"Male","specially_abled":"No","have_gstn":"No","enterprise_name":"ITrust","pan":"CLNPM9204L","organization_type_id":"1","bank_name":"HDFC Bank","account_number":"1223423423","ifsc_code":"HDFC0001068","business_activity":"Manufacturing","business_nature":"Service","male_employees":"12","female_employees":"5","start_date":"2022-11-04","flat_no":"12","name_of_building":"Pattanur","village_town":"Baleguli","block":"Kaveripattinam","road_street":"Krishnagiri","pincode":"635204","city":"Krishnagiri","state":"TAMIL NADU","district":"Krishnagiri","status":"1"}],"status":"true"}

# type = ''
# pan = ''
# gender = ''
# category = ''
# enterprise_name = ''
# bank_name = ''
# account_number = ''
# ifsc_code = ''
# business_activity = ''
# male_employee_count = ''
# female_employee_count = ''
# business_date = ''
# address = ''
# floor_no = ''
# village_town = ''
# block = ''
# pin = ''
# state = ''
# district = ''
# cityname = ''
# road_street = ''
# building_name = ''

# all_variables = dir()
#
# for name in all_variables:
#
#     # Print the item if it doesn't start with '__'
#     if not name.startswith('__') and not name == result:
#         myvalue = eval(name)
#         print(name, 'is', myvalue)
#
# sys.exit()
browser = webdriver.Chrome(service=Service('C:\\Users\\Liva\\Desktop\\udyam-automation\\chromedriver.exe'))

browser.maximize_window()
browser.get("https://udyamregistration.gov.in/UdyamRegistration.aspx")

browser.implicitly_wait(5)

browser.find_element("id", "ctl00_ContentPlaceHolder1_txtadharno").send_keys(aadhaar.replace(' ', ''))
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtownername").send_keys(name)

browser.implicitly_wait(3)

browser.find_element("id", "ctl00_ContentPlaceHolder1_btnValidateAadhaar").send_keys(Keys.ENTER)

try:
    element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOtp1"))
        )
    element.send_keys("")

except Exception as e:
    print("136", e)

try:
    element = WebDriverWait(browser, 3000).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlTypeofOrg"))
        )
except Exception as e:
    print("failed to locate dropdown")
    sys.exit(e)

print(149, element.get_attribute("name"))

# browser.execute_script("window.scrollTo(0, 200)")

# # print(browser.page_source)

print('type', organization_type_id)

try:
    l = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlTypeofOrg")
    d = Select(element)
except Exception as e:
    print("158",e)

print('Options are: ')
# iterate over dropdown options
for opt in d.options:
    print(opt.text)
    if type in opt.text:
        sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlTypeofOrg'))

        # sel.select_by_visible_text(opt.text)
        sel.select_by_value(organization_type_id)

        break


time.sleep(6)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
panelement = WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPan"))
        )
# print('pan set', panelement.get_attribute("value"))

if panelement.get_attribute("value") == '':
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
    print("not value")
# time.sleep(20)

PanButton = WebDriverWait(browser, 20).until(
EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnValidatePan")))
PanButton.click()

# browser.find_element("id", "ctl00_ContentPlaceHolder1_btnValidatePan").send_keys(Keys.ENTER)

try:
    PanNewButton = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnGetPanData")))
    PanNewButton.click()
    # browser.find_element("id", "ctl00_ContentPlaceHolder1_btnGetPanData").send_keys(Keys.ENTER)

except Exception as e:
    panError = browser.find_element("id", "ctl00_ContentPlaceHolder1_lblPanError").text
    if "PAN is not valid" in panError:
        browser.execute_script("alert('Invalid PAN Number')")
        sys.exit()
        browser.close()
        browser.quit()

    print('panbutton 148', str(e))

browser.implicitly_wait(10)

try:
    mobileElement = WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtmobile"))
    )
    try:
        browser.find_element("id", "ctl00_ContentPlaceHolder1_txtmobile").send_keys(mobile)
    except:
        pass

    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtemail").send_keys(email)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtenterprisename").send_keys(enterprise_name)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtBankName").send_keys(bank_name)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtaccountno").send_keys(account_number)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtifsccode").send_keys(ifsc_code)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonMale").send_keys(male_employees)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonFemale").send_keys(female_employees)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonOthers").send_keys(0)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtdateIncorporation").send_keys(start_date)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtcommencedate").send_keys(start_date)
except Exception as e:
    print('176', str(e))

try:
    forname = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + social_category + "')]").get_attribute('for')
    caste = browser.find_element(By.CSS_SELECTOR, '#' + forname)
    browser.execute_script("arguments[0].click();", caste)
except Exception as e:
    print('category 179', str(e))

try:
    browser.implicitly_wait(5)

    gen_for = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + gender + "')]").get_attribute(
        'for')
    print(gender, gen_for)
    genderfield = browser.find_element(By.CSS_SELECTOR, '#' + gen_for)
    print(gender, genderfield)
    browser.execute_script("arguments[0].click();", genderfield)
except Exception as e:
    print('gender 191', str(e))

try:
    bus_for = browser.find_element(By.XPATH,
                                   "//td//label[contains( text( ), '" + business_activity + "')]").get_attribute('for')
    actfield = browser.find_element(By.CSS_SELECTOR, '#' + bus_for)
    browser.execute_script("arguments[0].click();", actfield)
except Exception as e:
    print('gender 198', str(e))

browser.implicitly_wait(3)

print('category', social_category)
elementFlat = browser.find_element_by_id("ctl00_ContentPlaceHolder1_txtOffFlatNo")

actions = ActionChains(browser)
actions.move_to_element(elementFlat).perform()

flatElement = WebDriverWait(browser, 8).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOffFlatNo"))
    ).send_keys(flat_no)

# browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffFlatNo").send_keys(flat_no)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffVillageTown").send_keys(village_town)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBlock").send_keys(block)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffPin").send_keys(pincode)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBuilding").send_keys(name_of_building)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffRoadStreetLane").send_keys(road_street)
browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffCity").send_keys(city)

try:
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
    statt = Select(stat)
except Exception as e:
    print('state 213', str(e))
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
    statt = Select(stat)

print('state Options loading')
print('state', state)
# iterate over dropdown options
for opt in statt.options:
    print(opt.text)
    if state.upper() in opt.text:
        sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlstate'))

        sel.select_by_visible_text(opt.text)
        print(opt.text)
        time.sleep(0.8)
        break

browser.implicitly_wait(15)

try:
    city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
    citys = Select(city)
except Exception as e:
    print('state 240', str(e))
    city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
    citys = Select(city)

browser.implicitly_wait(15)
print('city Options loading')
print('city', district)
# iterate over dropdown options
for opt in citys.options:
    print(opt.text)
    if district.upper() in opt.text:
        sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlDistrict'))

        sel.select_by_visible_text(opt.text)
        print(opt.text)
        time.sleep(0.8)
        break

# unknown values
try:
    actfield = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rbtPh_1')
    browser.execute_script("arguments[0].click();", actfield)
except Exception as e:
    print('gender 263', str(e))

browser.find_element("id", "ctl00_ContentPlaceHolder1_btnsubmit").send_keys(Keys.ENTER)

browser.execute_script("alert('process completed')")

print('Process completed')
time.sleep(200)

print(name, email, mobile, aadhaar)
