# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 10:23
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : app.py

import json

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


@app.route("/api/LoginCode", methods=['POST'])
def logincode():
    data = request.get_json(force=True)
    code = data.get("code")
    if len(code) == 6:
        num = qps.QRPhoneCode(code)
        if num == 1002:
            return jsonify(code=1002, msg="Cookie获取失败，请重新获取")
        else:
            return jsonify(code=1001, msg="Cookie获取成功", ck=num)
    else:
        return jsonify(code=1002, msg="请输入正确的验证码")


@app.route('/QRLogin')
def qrLogin():
    with open("./config/config.json", encoding="utf-8") as f:
        config_json = json.load(f)

    Title = config_json["Main"]["Title"]
    return render_template("qrLogin.html", Title=Title)


@app.route('/api/GetQR', methods=['POST'])
def getQR():
    num = qps.QRStart()
    if num == 1001:
        return jsonify(code=1001)
    else:
        return jsonify(code=1002)


@app.route('/api/LoginQR', methods=['POST'])
def QRLogin():
    num = qps.QRStart2()
    if num == 1002:
        return jsonify(code=1002, msg="Cookie获取失败，请重新获取")
    elif num == 1010:
        return jsonify(code=1010, msg="需要二次短信验证码")
    else:
        # 上传Cookie
        # addCookie.add_Cookie(num)
        return jsonify(code=1001, msg=num)


@app.route('/quit', methods=['POST'])
def quit_B():
    qps.quitBrowser()
    return jsonify(code=1001)


if __name__ == '__main__':
    login = "Welcome to JDC"
    print(login)
    app.run(host="0.0.0.0", port=5100)
