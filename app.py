# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 10:23
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : app.py

import json
import re

from pyselenium import QRSelenium as qps
from flask import Flask, render_template, jsonify, request
from qinglong import addCookie

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    # 读取JSON文件
    with open("./config/config.json", encoding="utf-8") as f:
        config_json = json.load(f)

    Title = config_json["Main"]["Title"]
    return render_template("index.html", Title=Title)


@app.route('/QRLogin')
def qrLogin():
    with open("./config/config.json", encoding="utf-8") as f:
        config_json = json.load(f)

    Title = config_json["Main"]["Title"]
    qps.QRStart()
    return render_template("qrLogin.html", Title=Title)


@app.route('/api/LoginQR', methods=['POST'])
def QRLogin():
    num = qps.QRStart2()
    if num == 1002:
        return jsonify(code=1002, msg="Cookie获取失败，请重新获取")
    else:
        # 上传Cookie
        addCookie.add_Cookie(num)
        return jsonify(code=1001, msg=num)


if __name__ == '__main__':
    login = "Welcome to JDC"
    print(login)
    app.run(host="0.0.0.0", port=5100)
