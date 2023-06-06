from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# driver.get('https://portal.cuc.ac.jp/uprx/up/pk/pky001/Pky00101.xhtml')

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:

	if time.time() > five_min:
		chrome_diver_path = "../chromedriver_win32/chromedriver"
		driver = webdriver.Chrome(executable_path= chrome_diver_path)
		driver.get('https://portal.cuc.ac.jp/uprx/up/bs/bsa001/Bsa00101.xhtml')
		login = driver.find_element_by_xpath('//*[@id="loginForm:userId"]')
		login.send_keys('xxxx')
		login_pass = driver.find_element_by_xpath('//*[@id="loginForm:password"]')
		login_pass.send_keys('xxxx')

		login_button = driver.find_element_by_xpath('//*[@id="loginForm:loginButton"]/span[2]')
		login_button.click()

		time.sleep(3)

		rishuuu = driver.find_element_by_xpath('//*[@id="menuForm:mainMenu"]/ul/li[2]')
		rishuuu.click()

		time.sleep(4)

		res =  driver.find_element_by_xpath("//*[@id='menuForm:mainMenu']/ul/li[2]/ul/table/tbody/tr/td[1]/ul/li[2]")
		res.click()


		#pro_A
		time.sleep(1)
		proA = driver.find_element_by_xpath('//*[@id="funcForm:tabArea:gakkiT02:0:j_idt461:2:j_idt463:0:j_idt506"]/span')
		proA.click()


		#rgb(254, 249, 218) none repeat scroll 0% 0% / auto padding-box border-box
		time.sleep(1)
		number = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[6]/td[2]")
		condition = number.value_of_css_property("background")
		ok_1 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:j_idt825']")
		if int(number.text) >= 1 and  "rgb(254, 249, 218)" not in condition :
			check_1 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[6]/td[1]/div/div[2]/span")
			check_1.click()

			ok_1.click()
			print("Pro Ok")
		else:
			ok_1.click()


		#RBG
		time.sleep(2)
		rbg_button = driver.find_element_by_xpath("//*[@id='funcForm:tabArea:gakkiT02:0:j_idt461:2:j_idt463:1:j_idt506']")
		rbg_button.click()

		time.sleep(1)
		number_2 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[3]/td[2]")
		condition_2 = number_2.value_of_css_property("background")
		ok_2 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:j_idt825']")
		if int(number_2.text) >= 1 and  "rgb(254, 249, 218)" not in condition_2 :
			check_2 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[3]/td[1]/div/div[2]")
			check_2.click()

			ok_2.click()
			print("RBG OK")
		else:
			ok_2.click()


		#Web
		time.sleep(2)
		web_button = driver.find_element_by_xpath("//*[@id='funcForm:tabArea:gakkiT02:0:j_idt461:2:j_idt463:2:j_idt506']")
		web_button.click()

		time.sleep(1)
		number_3 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[2]/td[2]")
		condition_3 = number_3.value_of_css_property("background")
		ok_3 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:j_idt825']")
		if int(number_3.text) >= 1 and  "rgb(254, 249, 218)" not in condition_3 :
			check_3 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[2]/td[1]/div/div[2]")
			check_3.click()

			ok_3.click()
			print("Web OK")
		else:
			ok_3.click()



		#Soft
		time.sleep(2)
		soft = driver.find_element_by_xpath("//*[@id='funcForm:tabArea:gakkiT02:0:j_idt461:2:j_idt463:4:j_idt506']")
		soft.click()

		time.sleep(1)
		number_4 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[4]/td[2]")
		condition_4 = number_4.value_of_css_property("background")
		ok_4 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:j_idt825']")
		if int(number_4.text) >= 1 and  "rgb(254, 249, 218)" not in condition_4 :
			check_4 = driver.find_element_by_xpath("//*[@id='xuk01003:ch:jugyoList_data']/tr[4]/td[1]/div/div[2]")
			check_4.click()

			ok_4.click()
			print("Soft OK")
		else:
			ok_4.click()

		driver.quit()
		timeout = time.time() + 5