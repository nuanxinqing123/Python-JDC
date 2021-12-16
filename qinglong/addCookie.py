# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 10:29
# @Author  : Nuanxinqing
# @Email   : nuanxinqing@gmail.com
# @File    : addCookie.py

import requests
import json

with open("./config/config.json", encoding="utf-8") as f:
    config_json = json.load(f)

URL = config_json['QL']['URL']
Client_ID = config_json['QL']['Client_ID']
Client_Secret = config_json['QL']['Client_Secret']


# 获取青龙面板token
def get_token():
    url = URL + '/open/auth/token?client_id={}&client_secret={}'.format(Client_ID, Client_Secret)
    result = requests.get(url)
    result = result.json()
    return result["data"]


# 添加CK到面板
def add_Cookie(ck):
    # Token
    tk = get_token()
    token = tk['token']
    expiration = tk['expiration']

    # 字符串合并
    bearer = "Bearer {}".format(token)
    params = 't={}'.format(expiration)

    # 请求信息
    url = URL + "/open/envs"
    data = [{'value': str(ck), 'name': "JD_COOKIE"}]
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.198 Mobile Safari/537.36",
        "Authorization": bearer,
        "content-type": "application/json"
    }

    # 获取并打印结果
    result = requests.post(url, data=json.dumps(data), headers=headers, params=params)
    result = result.text
    print(result)
