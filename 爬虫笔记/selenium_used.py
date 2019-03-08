# 什么叫selenium？
#  谷歌浏览器驱动
#  火狐的浏览器驱动
#  无头浏览器

# 安装：pip3 install selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#创建浏览器驱动（火狐）
# brower = webdriver.Firefox(
#     executable_path='/Users/ljh/Desktop/1808爬虫/geckodriver'
# )

#创建浏览器驱动（无头浏览器phantomjs）
# warnings.warn('Selenium support for PhantomJS
# has been deprecated, please use headless '

# brower = webdriver.PhantomJS(
#     executable_path='/Users/ljh/Desktop/1808爬虫/phantomjs'
# )

#创建浏览器驱动（谷歌）
#设置无头浏览器
# opt = webdriver.ChromeOptions()
# opt.set_headless()
# brower = webdriver.Chrome(
#     executable_path='/Users/ljh/Desktop/1808爬虫/chromedriver'
#     ,options=opt
# )

brower = webdriver.Chrome(
    executable_path='/Users/ljh/Desktop/1808爬虫/chromedriver'
)
#使用get方法打开网站
brower.get('https://www.baidu.com')

#保存页面截图
brower.save_screenshot('baidu.png')


#模拟用户点击和输入操作
# brower.find_element_by_id() 根据节点id查找
# brower.find_element_by_class_name() 根据节点class属性查找
# brower.find_element_by_css_selector() 根据css选择器查找
# brower.find_element_by_link_text() 根据节点的文本查找
# brower.find_element_by_xpath() 根据xpath语法选择器查找

brower.find_element_by_id('kw').send_keys('美女')
brower.find_element_by_id('su').click()

#清空关键字
brower.find_element_by_id('kw').clear()
brower.find_element_by_id('kw').send_keys('帅哥')
brower.find_element_by_id('su').click()


time.sleep(2)
#获取节点的属性和文本
#get_attribute:获取节点的属性
searchText = brower.find_element_by_id('kw').get_attribute('value')
#text()获取节点的文本
# text = brower.find_element_by_class_name('search_tool').text
text = brower.find_element_by_xpath('//div[@class="search_tool"]').text
print(searchText,text)
time.sleep(2)

#点击下一页按钮
try:
    brower.find_element_by_link_text('下一页>').click()
except NoSuchElementException as err:
    print('没有找到这个节点')

time.sleep(1)
#返回（后退）
brower.back()

time.sleep(1)

#前进
brower.forward()





