
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://baidu.com')
assert '百度' in browser.title