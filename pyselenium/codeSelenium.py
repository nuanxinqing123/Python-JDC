# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 17:56
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : codeSelenium.py
import base64
import cv2 as cv
import numpy as np
import random
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from cookie import cookie

options = webdriver.ChromeOptions()
# 屏蔽扩展插件提示内容
options.add_argument('--ignore-certificate-errors')
# 静默运行
options.add_argument('--headless')
# 限制浏览器大小 width：915, height: 1000
options.add_argument("--window-size=915,1000")
# 禁用webgl
options.add_argument("--disable-webgl")
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
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
options.add_argument(f'--user-agent={user_agent}')


def CodeStart(phonenumber):
    global browser

    # 启动驱动
    # browser = webdriver.Chrome(options=options)
    options.binary_location = './chromedriver/chrome-win/chrome.exe'
    browser = webdriver.Chrome("./chromedriver/chromedriver.exe", options=options)
    # try:
    #     options.binary_location = './chromedriver/chrome-linux/chrome'
    #     browser = webdriver.Chrome("./chromedriver/chromedriver", options=options)
    # except:
    #     options.binary_location = './chromedriver/chrome-win/chrome.exe'
    #     browser = webdriver.Chrome("./chromedriver/chromedriver.exe", options=options)

    browser.get("https://plogin.m.jd.com/login/login")

    number_ = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/p[1]/input')
    number_.clear()
    number_.send_keys(phonenumber)
    time.sleep(1.5)

    # 发送验证码
    code_btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/p[2]/button')
    code_btn.click()

    time.sleep(0.8)

    # 文字验证：
    # 图：//*[@id="cpc_img"]
    # 字体：//*[@id="captcha_modal"]/div/div[3]/div/img

    # 判断是否有滑块
    try:
        x = 0
        for i in range(5):
            x += 1
            time.sleep(0.5)
            slide = browser.find_element(By.XPATH, '//*[@id="cpc_img"]')
            if slide:
                print("出现滑块")
                SliderProcessing()
    except:
        pass

    # 滑块之后
    try:
        time.sleep(1)
        slide = browser.find_element(By.XPATH, '//*[@id="cpc_img"]')
        if slide:
            x += 1
    except:
        pass

    if x > 5:
        browser.close()
        return 1003
    else:
        return 1006


def CodeStart2(phonecode):
    global browser

    # 输入验证码
    phonecode_ = browser.find_element(By.XPATH, '//*[@id="authcode"]')
    phonecode_.clear()
    phonecode_.send_keys(phonecode)

    # 选中单选框
    d_btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/p[2]/input')
    d_btn.click()

    # 登录
    login_btn = browser.find_element(By.XPATH, '//*[@id="app"]/div/a')
    login_btn.click()

    # 等待页面跳转
    try:
        WebDriverWait(browser, 20, 0.5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"mCommonMy\"]/div/img")))

        # 前往个人主页
        browser.get("https://home.m.jd.com/myJd/newhome.action")

        # 获取Cookie
        ck = browser.get_cookies()
        ck = cookie.clear(ck)
        return ck
    except:
        # 获取失败
        return 1002

    finally:
        browser.close()


# 滑动轨迹算法
def trace(sum):
    n = random.randint(6, 7)
    # print(n)
    listx = []

    for i in range(0, n - 1):
        a = random.uniform(1, sum)  # 生成 n-1 个随机节点
        listx.append(a)
    listx.sort()  # 对节点排序
    listx.append(sum)  # 设置第 n 个节点为 sum，即总额

    listy = []
    for i in range(len(listx)):
        if i == 0:
            b = listx[i]
        else:
            b = listx[i] - listx[i - 1]
        listy.append(b)

    listy.sort()
    listy.reverse()

    listz = [2, 0, 0, 0, -3, -2, -2, -1, 0, 1, 2, 3]
    listy.extend(listz)

    return listy


# 距离算法
def detect_displacement(bg, backpg):
    bg_np = np.frombuffer(base64.b64decode(bg), np.uint8)
    image = cv.imdecode(bg_np, cv.IMREAD_COLOR)
    backpg_np = np.frombuffer(base64.b64decode(backpg), np.uint8)
    template = cv.imdecode(backpg_np, cv.IMREAD_COLOR)

    image_tran_canny = cv.GaussianBlur(image, (3, 3), 0)
    image_tran_canny = cv.Canny(image_tran_canny, 50, 150)

    template_tran_canny = cv.GaussianBlur(template, (3, 3), 0)
    template_tran_canny = cv.Canny(template_tran_canny, 50, 150)

    res = cv.matchTemplate(
        image_tran_canny, template_tran_canny, cv.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    top_left = max_loc[0]

    return top_left


def SliderProcessing():
    global browser

    # 获取滑块图base64编码
    img = browser.find_element(By.XPATH, '//*[@id="cpc_img"]')
    imgSrc = img.get_attribute('src')
    imgSrc = imgSrc.replace('data:image/jpg;base64,', '')
    gap = browser.find_element(By.XPATH, '//*[@id="small_img"]')
    gapSrc = gap.get_attribute('src')
    gapSrc = gapSrc.replace('data:image/png;base64,', '')

    # 显示图：420px, 260px
    # 原图：277px, 173px
    # 倍率：65.9%, 66.5%, 66.2%
    result = detect_displacement(gapSrc, imgSrc)

    # 计算距离
    tracks = trace((int(result) / 0.662) + 5)

    # 移动
    slider = browser.find_element(By.XPATH, '//*[@id="captcha_modal"]/div/div[3]/div/img')
    ActionChains(browser).click_and_hold(slider).perform()

    # 滑动
    for x in tracks:
        ActionChains(browser, duration=15).move_by_offset(xoffset=x, yoffset=random.randint(-3, 3)).perform()
    time.sleep(0.2)
    # 松开鼠标
    ActionChains(browser).release().perform()

    time.sleep(0.8)
