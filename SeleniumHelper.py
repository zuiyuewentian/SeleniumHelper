import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys			  
from time import sleep

driver = None

def create_driver():
	global driver
	options = webdriver.ChromeOptions()
	# 禁用gpu加速，防止出一些未知bug
	options.add_argument('--disable-gpu')
	#options.add_experimental_option("excludeSwitches", ['enable-automation'])
	driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)

	# 设置一个隐性等待 5s
	driver.implicitly_wait(5)
	driver.maximize_window()

#帮助文档
def helper():
	print('===============')
	print('帮助文档，输入【help】')
	print('1.【查看,(xPath)】根据xPath查找的元素有多少个')
	print('2.【点击,(xPath)】根据xPath查找的元素是否成功')
	print('3.【点击,(xPath,index)】根据xPath查找的第n个元素是否成功')
	print('4.【输入,(xPath,text)】根据xPath查找的元素输入指定内容')
	print('5.【输入,(xPath,index,text)】根据xPath查找的第n个元素输入指定内容')
	print('===============')

#根据xPath查找的元素有多少个
def find_elements_by_xPath_count(xpath):
	global driver
	try:
		elements = driver.find_elements_by_xpath(xpath)
		print('_execute_result>执行完毕！ 共' + str(len(elements)) + '个')
	except Exception as e:
		print("_execute_result>出现异常，" + str(e))

#点击根据xPath查找的元素是否成功
def click_element_by_xPath(xpath):
	global driver
	try:
		element = driver.find_element_by_xpath(xpath)
		driver.execute_script("arguments[0].click();", element)
		print("_execute_result>执行完毕！请观察浏览器元素")
	except Exception as e:
		print("_execute_result>出现异常，" + str(e))

#点击根据xPath查找的多元素的第[index]个是否成功
def click_element_by_xPath_index(xpath,index):
	global driver
	try:
		element = driver.find_elements_by_xpath(xpath)[int(index)]
		driver.execute_script("arguments[0].click();", element)
		print("_execute_result>执行完毕！请观察浏览器元素")
	except Exception as e:
		print("_execute_result>出现异常，" + str(e))

#输入根据xPath查找的元素是否成功
def input_element_by_xPath(xpath,text):
	global driver
	try:
		driver.find_element_by_xpath(xpath).send_keys(text)
		print("_execute_result>执行完毕！请观察浏览器元素")
	except Exception as e:
		print("_execute_result>出现异常，" + str(e))

#输入根据xPath查找的多元素中第index个是否成功
def input_element_by_xPath_index(xpath,index,text):
	global driver
	try:
		driver.find_elements_by_xpath(xpath)[int(index)].send_keys(text)
		print("_execute_result>执行完毕！请观察浏览器元素")
	except Exception as e:
		print("_execute_result>出现异常，" + str(e))

def main():
	global driver
	print("测试元素搜索功能")
	print("请输入参数：待访问地址")
	address = input()
	create_driver()
	driver.get(address)
	sleep(2)
	helper()
	keyword = ''
	while (keyword != '-1'):
		print('请选择功能选项，输入【help】打印帮助,【-1】退出')
		keyword = input()
		print("输入:" + keyword)
		if keyword == '1':
			print('请输入参数：xPath')
			xPath = input()
			find_elements_by_xPath_count(xPath)
		elif keyword == '2':
			print('请输入参数：xPath')
			xPath = input()
			click_element_by_xPath(xPath)
		elif keyword == '3':
			print('请输入参数：xPath')
			xPath = input()
			print('请输入参数：index')
			index = input()
			click_element_by_xPath_index(xPath,index)
		elif keyword == '4':
			print('请输入参数：xPath')
			xPath = input()
			print('请输入参数：text')
			text = input()
			input_element_by_xPath(xPath,text)
		elif keyword == '5':
			print('请输入参数：xPath')
			xPath = input()	
			print('请输入参数：index')
			index = input()
			print('请输入参数：text')
			text = input()
			input_element_by_xPath_index(xPath,index,text)
		elif keyword == 'help':
			helper()

	driver.quit()
	print("请按任何键结束...")

if __name__ == "__main__":
    main()
