#coding=utf-8
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.4'
desired_caps['deviceName'] = '9e6e5eed'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("清除").click()
#driver.find_element_by_name("1").click()
driver.find_element_by_android_uiautomator("new UiSelector().text(\"1\")").click();
#driver.findElement(By.xpath("//android.widget.Button[contains(@text,'1')]")).click();
driver.find_element_by_name("5").click()
#driver.find_element_by_name("delete").click()
driver.find_element_by_name("+").click()
#driver.find_element_by_name("加").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("等于").click()
#driver.find_element_by_id("com.android.calculator2:id/equal").click()
#driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'等于')]").click();
#driver.find_element_by_accessibility_id("等于").click(); #根据元素的 content-desc 
#driver.find_element_by_android_uiautomator("new UiSelector().description(\"等于\")").click();
#driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.android.calculator2:id/equal\")").click();
#driver.find_element_by_android_uiautomator("new UiSelector().className(\"android.widget.Button\").description(\"等于\").clickable(true)").click();

driver.quit()