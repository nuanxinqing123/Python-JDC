# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 10:23
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : app.py

import json, re
import logging

from pyselenium import codeSelenium as cps
from pyselenium import QRSelenium as qps
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config [ 'JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    # 读取JSON文件
    with open("./config/config.json", encoding="utf-8") as f:
        config_json = json.load(f)

    Title = config_json["Main"]["Title"]
    return render_template("index.html", Title=Title)


@app.route('/NumberLogin')
def numLogin():
    with open("./config/config.json", encoding="utf-8") as f:
        config_json = json.load(f)

    Title = config_json["Main"]["Title"]
    return render_template("numLogin.html", Title=Title)


@app.route("/api/LoginNum", methods=['POST'])
def loginnum():
    data = request.get_json(force=True)
    number = data.get("number")
    print(number)
    if number != "":
        ret = re.match(r"^1[356789]\d{9}$", str(number))
        if ret:
            res = cps.CodeStart(number)
            if res == 1006:
                return jsonify(code=1001, msg="正在通过滑块验证，如果长时间没收到验证码，请重新登录")
            elif res == 1003:
                return jsonify(code=1002, msg="滑块验证失败，请稍等十分钟后重试")
            else:
                return jsonify(code=1001, msg="请输入6位验证码")
        else:
            return jsonify(code=1002, msg="请输入正确的手机号码")
    else:
        return jsonify(code=1002, msg="参数不完整")


@app.route("/api/LoginCode", methods=['POST'])
def logincode():
    data = request.get_json(force=True)
    code = data.get("code")
    if len(code) == 6:
        num = cps.CodeStart2(code)
        if num == 1002:
            return jsonify(code=1002, msg="Cookie获取失败，请重新获取")
        else:
            #
            #   预留位置（QL面板上传）
            #
            return jsonify(code=1001, msg="Cookie获取成功", ck=num)
    else:
        return jsonify(code=1002, msg="请输入正确的验证码")


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
        return jsonify(code=1001, msg="Cookie获取成功")


if __name__ == '__main__':
    login = """
    ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◆◆◆◆◆◆◇◇◇◇◇◇◇◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◇◇
    ◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◆◇◇◆◆◆◇◇◇◇◇◇◇◇◆◆◆◇◇◆◆◇◇◇◇
    ◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◇◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◇◇◇
    ◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◇◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◆◇◇◇◇◇◇◆◆◆◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◇◇◇◇◇◇◇◆◆◆◇◇◇◇◇◇◇◇◇
    ◇◇◇◆◆◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◇◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◇◇◇
    ◇◇◇◆◆◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◆◆◆◇◇◇◇◇◇◇◇◆◆◆◇◇◆◆◆◇◇◇
    ◇◇◇◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◇◇
    ◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    ◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇
    """
    print(login)
    app.run(host="0.0.0.0", port=5000)
