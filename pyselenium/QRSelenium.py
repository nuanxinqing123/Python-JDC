# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 19:28
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : QRSelenium.py

import time, json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from cookie import cookie
from PIL import Image

options = webdriver.ChromeOptions()
# 屏蔽扩展插件提示内容
options.add_argument('--ignore-certificate-errors')
# 静默运行
options.add_argument('--headless')
# 限制浏览器大小 width：915, height: 1000
options.add_argument("--window-size=915,1000")
# 在 root 权限下运行
options.add_argument('--no-sandbox')
# 禁用GPU加速
options.add_argument('--disable-gpu')
options.add_argument('--disable-software-rasterizer')
# 禁用扩展插件
options.add_argument('--disable-extensions')
# 无痕模式
options.add_argument('--incognito')
# 开发者模式启动
options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 添加 User Agent
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
options.add_argument(f'--user-agent={user_agent}')

with open("./config/config.json", encoding="utf-8") as f:
    config_json = json.load(f)


def QRStart():
    global browser

    # 启动驱动(Linux)
    options.binary_location = './chromedriver/chrome-linux/chrome'
    browser = webdriver.Chrome("./chromedriver/chromedriver", options=options)

    # 启动驱动(Windows)
    # options.binary_location = './chromedriver/chrome-win/chrome.exe'
    # browser = webdriver.Chrome("./chromedriver/chromedriver.exe", options=options)

    # 入口地址
    browser.get(
        'https://plogin.m.jd.com/login/login?appid=300&returnurl=https%3A%2F%2Fwq.jd.com%2Fpassport%2FLoginRedirect%3Fstate%3D2251685869%26returnurl%3Dhttps%253A%252F%252Fhome.m.jd.com%252FmyJd%252Fnewhome.action%253Fsceneval%253D2%2526ufc%253D%2526&source=wq_passport')

    time.sleep(1)
    C_Btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/p[2]/input')
    C_Btn.click()

    # QQ登陆
    QQ_Btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[6]/p/a')
    QQ_Btn.click()

    # 全局截图
    picture_name1 = './static/QR/1.png'
    browser.save_screenshot(picture_name1)

    # 局部截图
    ce = browser.find_element(By.XPATH, '//*[@id="combine_page"]/div[1]')
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))  # 截取二维码部分
    img.save('./static/QR/2.png')
    return 1001


def QRStart2():
    global browser
    # 判断是否触发短信验证
    try:
        phoneCode = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/span/a')
        if phoneCode:
            phoneCode.click()
            time.sleep(0.5)
            phoneCode2 = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/button')
            phoneCode2.click()
            # 需要二次验证码
            return 1010
    except:
        # 等待页面跳转
        try:
            WebDriverWait(browser, 120, 0.5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"mCommonMy\"]/div/img")))

            # 前往个人主页
            browser.get("https://home.m.jd.com/myJd/newhome.action")

            # 获取Cookie
            ck = browser.get_cookies()
            ck = cookie.clear(ck)
            return ck
        except:
            return 1002

        finally:
            browser.quit()


def QRPhoneCode(code):
    global browser

    phoneCode = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/input')
    phoneCode.send_keys(code)
    time.sleep(0.5)

    btnOK = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/a[1]')
    btnOK.click()

    # 等待页面跳转
    try:
        WebDriverWait(browser, 120, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"mCommonMy\"]/div/img")))

        # 前往个人主页
        browser.get("https://home.m.jd.com/myJd/newhome.action")

        # 获取Cookie
        ck = browser.get_cookies()
        ck = cookie.clear(ck)
        return ck
    except:
        return 1002
    finally:
        browser.quit()


def quitBrowser():
    browser.quit()