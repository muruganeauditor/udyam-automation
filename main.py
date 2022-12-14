import string
import sys
import requests
import datetime

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

api_url = "https://eauditoroffice.in/api/udyamDetails"
response = requests.get(api_url)
apiResponse = response.json()
print(apiResponse['status'])

if apiResponse['status']:
    userData = apiResponse['data'][0]
    locals().update(userData)
else:
    print("Invalid Api response")
    sys.exit()

# format
try:
    format = '%Y-%m-%d'
    datetime = datetime.datetime.strptime(start_date, format)
    business_date = datetime.date().strftime("%d/%m/%Y")
except Exception as e:
    print("start_date error"+str(e))

# {"data":[{"id":1,"name":"Murugan palani","email":"muruganaccetcse@gmail.com","mobile":"9585393730","aadhaar":"217298315618","social_category":"General","gender":"Male","specially_abled":"No","have_gstn":"No","enterprise_name":"ITrust","pan":"CLNPM9204L","organization_type_id":"1","bank_name":"HDFC Bank","account_number":"1223423423","ifsc_code":"HDFC0001068","business_activity":"Manufacturing","business_nature":"Service","male_employees":"12","female_employees":"5","start_date":"2022-11-04","flat_no":"12","name_of_building":"Pattanur","village_town":"Baleguli","block":"Kaveripattinam","road_street":"Krishnagiri","pincode":"635204","city":"Krishnagiri","state":"TAMIL NADU","district":"Krishnagiri","status":"1"}],"status":"true"}

browser = webdriver.Chrome(service=Service('C:\\Users\\Liva\\Desktop\\udyam-automation\\chromedriver.exe'))

browser.maximize_window()
browser.get("https://udyamregistration.gov.in/UdyamRegistration.aspx")

browser.implicitly_wait(5)
try:
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtadharno").send_keys(aadhaar.replace(' ', ''))
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtownername").send_keys(name)
except Exception as e:
    print("aadhaar error"+str(e))

browser.implicitly_wait(3)

try:
    aadharNewButton = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnValidateAadhaar")))

    aadharNewButton.click()
except Exception as e:
    print("btnvalid error"+str(e))

print("button clicks")

try:
    element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOtp1"))
        )
    element.send_keys("")

except Exception as e:
    print("62", e)

try:
    element = WebDriverWait(browser, 4000).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlTypeofOrg"))
        )
except Exception as e:
    print("failed to locate dropdown")
    sys.exit(e)

print(72, element.get_attribute("name"))

# browser.execute_script("window.scrollTo(0, 200)")

# # print(browser.page_source)

print('type', organization_type_id)

try:
    browser.implicitly_wait(2)
    l = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlTypeofOrg")
    d = Select(element)
except Exception as e:
    print("ddlTypeofOrg error",e)

print('Options are loaded: ')
# iterate over dropdown options
try:
    sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlTypeofOrg'))
    browser.implicitly_wait(5)
    sel.select_by_value(str(organization_type_id))

except Exception as e:
    print("ddlTypeofOrg 104",str(e))

time.sleep(6)
try:
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
    panelement = WebDriverWait(browser, 1).until(
                EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPan"))
            )
except Exception as e:
    print("txtPan error",e)

try:
    browser.implicitly_wait(1)
    if panelement.get_attribute("value") == '':
        browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPan").send_keys(pan)
        print("not value")
except Exception as e:
    print("txtPan 121",e)

try:
    browser.implicitly_wait(1)
    PanButton = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnValidatePan")))
    PanButton.click()
except Exception as e:
    print("btnValidatePan error",e)

try:
    browser.implicitly_wait(1)
    PanNewButton = WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnGetPanData")))
    PanNewButton.click()

except Exception as e:
    panError = browser.find_element("id", "ctl00_ContentPlaceHolder1_lblPanError").text
    if "PAN is not valid" in panError:
        browser.execute_script("alert('Invalid PAN Number')")
        sys.exit()
        browser.close()
        browser.quit()

    print('panbutton error', str(e))


try:
    browser.implicitly_wait(5)

    gst_for = browser.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_rblWhetherGstn']//td//label[contains( text( ), '" + have_gstn + "')]").get_attribute(
        'for')
    print('gst', have_gstn)
    gstfield = browser.find_element(By.CSS_SELECTOR, '#' + gst_for)
    print('gstid', gstfield)
    browser.execute_script("arguments[0].click();", gstfield)
except Exception as e:
    print('gst 136', str(e))

try:
    browser.implicitly_wait(1)
    mobileElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtmobile"))
    )
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtmobile").send_keys(mobile)
except Exception as e:
    print('mobile 144', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtemail").send_keys(email)
except Exception as e:
    print('email 173', str(e))

print('category', social_category)
try:
    browser.implicitly_wait(1)
    forname = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + social_category + "')]").get_attribute('for')
    caste = browser.find_element(By.CSS_SELECTOR, '#' + forname)
    browser.execute_script("arguments[0].click();", caste)
except Exception as e:
    print('category 182', str(e))

try:
    browser.implicitly_wait(5)

    gen_for = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + gender + "')]").get_attribute(
        'for')
    print(gender, gen_for)
    genderfield = browser.find_element(By.CSS_SELECTOR, '#' + gen_for)
    print(gender, genderfield)
    browser.execute_script("arguments[0].click();", genderfield)
except Exception as e:
    print('gender 194', str(e))

try:
    browser.implicitly_wait(5)

    abled_for = browser.find_element(By.XPATH, "//td//label[contains( text( ), '" + specially_abled + "')]").get_attribute(
        'for')
    print('abled', abled_for)
    abledfield = browser.find_element(By.CSS_SELECTOR, '#' + abled_for)
    print('abledid', abledfield)
    browser.execute_script("arguments[0].click();", abledfield)
except Exception as e:
    print('gst 206', str(e))

try:
    browser.implicitly_wait(1)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtenterprisename").send_keys(enterprise_name)
except Exception as e:
    print('ex 187', str(e))

try:
    browser.implicitly_wait(1)
    unitElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtUnitName"))
    ).send_keys(enterprise_name)
except Exception as e:
    print('ex 194', str(e))

try:
    browser.implicitly_wait(1)
    unitElements = WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_btnAddUnit"))
    ).click()
except Exception as e:
    print('ex 201', str(e))

try:
    browser.implicitly_wait(15)
    element = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_ddlUnitName")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    unitElementsnew = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_ddlUnitName") )
    )
    time.sleep(10)
    sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlUnitName'))

    sel.select_by_value('1')
except Exception as e:
    print('ex 215', str(e))

try:
    browser.implicitly_wait(1)
    elementFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPFlat")

    actions = ActionChains(browser)
    actions.move_to_element(elementFlat).perform()
    print("Action ok")
except Exception as e:
    print('FlatNo 224', str(e))

try:
    browser.implicitly_wait(1)
    flatElement = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtPFlat"))
        ).send_keys(flat_no)

    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPFlat").send_keys(flat_no)
    print("flatp ok")
except Exception as e:
    print('flatp 234', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPBuilding").send_keys(name_of_building)
except Exception as e:
    print('name_of_building 239', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPVillageTown").send_keys(village_town)
except Exception as e:
    print('village_town 244', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPBlock").send_keys(block)
except Exception as e:
    print('block 249', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPRoadStreetLane").send_keys(road_street)
except Exception as e:
    print('road_street 254', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPCity").send_keys(city)
except Exception as e:
    print('city 259', str(e))

try:
    browser.implicitly_wait(2)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtPpin").send_keys(pincode)
except Exception as e:
    print('pincode 264', str(e))

try:
    browser.implicitly_wait(5)
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPState")
    statt = Select(stat)
except Exception as e:
    print('state 270', str(e))
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPState")
    statt = Select(stat)

print('state Options loading')
print('state', state)
# iterate over dropdown options
try:
    for opt in statt.options:
        print(opt.text)
        if state.upper() in opt.text:
            sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlPState'))

            sel.select_by_visible_text(opt.text)
            print(opt.text)
            time.sleep(0.8)
            break
except Exception as e:
    print('statepick 324', str(e))

browser.implicitly_wait(15)

try:
    browser.implicitly_wait(1)
    citya = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPDistrict")
    citys = Select(citya)
except Exception as e:
    print('citys 293', str(e))
    citya = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlPDistrict")
    citys = Select(citya)

browser.implicitly_wait(15)
print('city Options loading')
print('city', district)
# iterate over dropdown options
try:
    for opt in citys.options:
        print(opt.text)
        if district.upper() in opt.text:
            sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlPDistrict'))

            sel.select_by_visible_text(opt.text)
            print(opt.text)
            time.sleep(0.8)
            break
except Exception as e:
    print('PDistrict 352', str(e))

browser.implicitly_wait(10)

try:
    browser.implicitly_wait(5)
    unitNewButton = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_BtnPAdd")))
    unitNewButton.click()
except Exception as e:
    print('uBtnPAdd 361', str(e))

browser.implicitly_wait(13)

try:
    browser.implicitly_wait(2)
    elementFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtOffFlatNo")

    actions = ActionChains(browser)
    actions.move_to_element(elementFlat).perform()
    print("Action324 ok")
except Exception as e:
    print('FlatNo 326', str(e))

try:
    time.sleep(5)
    flatElement = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOffFlatNo"))
        ).send_keys(flat_no)

    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffFlatNo").send_keys(flat_no)
    print("flat335 ok")
except Exception as e:
    print('flat 337', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBuilding").send_keys(name_of_building)
except Exception as e:
    print('name_of_building 343', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffVillageTown").send_keys(village_town)
except Exception as e:
    print('village_town 349', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffBlock").send_keys(block)
except Exception as e:
    print('block 355', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffRoadStreetLane").send_keys(road_street)
except Exception as e:
    print('road_street 361', str(e))

try:
    time.sleep(2)
    elementsFlat = browser.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtOffCity")

    actionsnew = ActionChains(browser)
    actionsnew.move_to_element(elementsFlat).perform()

    cityElement = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtOffCity"))
    )

    inputcity = browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffCity")
    inputcity.send_keys(city)
except Exception as e:
    print('city 377', str(e))

try:
    browser.implicitly_wait(5)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtOffPin").send_keys(pincode)
except Exception as e:
    print('pincode 383', str(e))

try:
    browser.implicitly_wait(5)
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
    statt = Select(stat)
except Exception as e:
    print('state 390', str(e))
    stat = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlstate")
    statt = Select(stat)

print('state Options loading')
print('state', state)
# iterate over dropdown options
try:
    for opt in statt.options:
        print(opt.text)
        if state.upper() in opt.text:
            sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlstate'))

            sel.select_by_visible_text(opt.text)
            print(opt.text)
            time.sleep(0.8)
            break
except Exception as e:
    print('states 456', str(e))

browser.implicitly_wait(15)

try:
    city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
    citys = Select(city)
except Exception as e:
    print('citys 413', str(e))
    city = browser.find_element("id", "ctl00_ContentPlaceHolder1_ddlDistrict")
    citys = Select(city)

browser.implicitly_wait(15)
print('city Options loading')
print('city', district)
# iterate over dropdown options
try:
    for opt in citys.options:
        print(opt.text)
        if district.upper() in opt.text:
            sel = Select(browser.find_element("id", 'ctl00_ContentPlaceHolder1_ddlDistrict'))

            sel.select_by_visible_text(opt.text)
            print(opt.text)
            time.sleep(0.8)
            break
except Exception as e:
    print('ldistrict 483', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtdateIncorporation").send_keys(business_date)
except Exception as e:
    print('ex 434', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtcommencedate").send_keys(business_date)
except Exception as e:
    print('439', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtBankName").send_keys(bank_name)
except Exception as e:
    print('ex 445', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtaccountno").send_keys(account_number)
except Exception as e:
    print('ex 450', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtifsccode").send_keys(ifsc_code)
except Exception as e:
    print('ex 455', str(e))

try:
    browser.implicitly_wait(3)
    bus_for = browser.find_element(By.XPATH,
                                   "//td//label[contains( text( ), '" + business_activity + "')]").get_attribute('for')
    actfield = browser.find_element(By.CSS_SELECTOR, '#' + bus_for)
    browser.execute_script("arguments[0].click();", actfield)
except Exception as e:
    print('gender 463', str(e))

try:
    browser.implicitly_wait(5)
    if business_nature=='Trading' and business_activity=='Services':
        bactfield = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rdbSubCategg_1')
        browser.execute_script("arguments[0].click();", bactfield)
    elif business_nature=='Non-Trading' and business_activity=='Services':
        bactfield = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rdbSubCategg_0')
        browser.execute_script("arguments[0].click();", bactfield)
except Exception as e:
    print('trading 533', str(e))

try:
    time.sleep(3)
    maleElement = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1_txtNoofpersonMale"))
    )
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonMale").send_keys(male_employees)
except Exception as e:
    print('ex 472', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonFemale").send_keys(female_employees)
except Exception as e:
    print('ex 477', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtNoofpersonOthers").send_keys(0)
except Exception as e:
    print('ex 482', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtDepCost").send_keys(0)
except Exception as e:
    print('ex 487', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtExCost").send_keys(0)
except Exception as e:
    print('ex 492', str(e))

try:
    browser.implicitly_wait(3)
    browser.find_element("id", "ctl00_ContentPlaceHolder1_txtTotalTurnoverA").send_keys(0)
except Exception as e:
    print('ex 497', str(e))

try:
    browser.implicitly_wait(5)
    actfield = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rbtPh_1')
    browser.execute_script("arguments[0].click();", actfield)
except Exception as e:
    print('actfield 503', str(e))

# unknown values
try:
    browser.implicitly_wait(3)
    actfieldone = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblGeM_1')
    browser.execute_script("arguments[0].click();", actfieldone)
except Exception as e:
    print('actfield 510', str(e))

try:
    browser.implicitly_wait(3)
    actfieldtwo = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblTReDS_1')
    browser.execute_script("arguments[0].click();", actfieldtwo)
except Exception as e:
    print('actfield 516', str(e))

try:
    browser.implicitly_wait(3)
    actfieldthree = browser.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_rblNCS_1')
    browser.execute_script("arguments[0].click();", actfieldthree)
except Exception as e:
    print('actfield 522', str(e))

try:
    browser.find_element("id", "ctl00_ContentPlaceHolder1_btnsubmit").send_keys(Keys.ENTER)

    browser.execute_script("alert('process completed')")
except Exception as e:
    print('btnfinal 597', str(e))

print('Process completed')
time.sleep(1000)

print(name, email, mobile, aadhaar)
