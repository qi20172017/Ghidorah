"""
在线对云打码网站的验证码进行识别
"""
from selenium import webdriver
from ydmapi import *
# Python图片处理库
from PIL import Image

class YdmSpider:
    def __init__(self):
        """打开云打码网站,将窗口最大化"""
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(options=self.options)
        # 输入云打码官网地址
        self.browser.get('http://www.yundama.com/')

    # 截取验证码图片
    def get_image(self):
        # 1、获取主页截图
        self.browser.save_screenshot('index.png')
        # 2、从大截图中截取出验证码的图片
        # 先获取到验证码的节点,再使用location属性获取左上角的 x y 坐标
        location = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').location
        # size属性: 获取节点的宽度和高度
        size = self.browser.find_element_by_xpath('//*[@id="verifyImg"]').size
        # 获取两个坐标: 左上角x、y坐标 和 右下角的x、y坐标
        left_x = location['x']
        left_y = location['y']
        right_x = left_x + size['width']
        right_y = left_y + size['height']

        # 截取验证码图片(注意corp()参数为元组)
        img = Image.open('index.png').crop((left_x,left_y,right_x,right_y))
        img.save('verify.png')

    # 获取在线识别结果
    def get_code(self):
        result = get_result('verify.png')
        print('识别结果:',result)

    def run(self):
        """程序入口函数"""
        self.get_image()
        self.get_code()
        self.browser.close()

if __name__ == '__main__':
    spider = YdmSpider()
    spider.run()














