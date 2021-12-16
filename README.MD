# 说明
JDCookie获取Python版

# 修改
Chromedriver目录内置版本：96.0.4664.45（自行按需求更改）

查看自己的谷歌浏览器版本：设置 - 关于Chrome（关于版本选择，假如我的浏览器版本是96.0.4664.45，我们在驱动下载页面选择96.0.4664就可以了，最后一位小数点版本不一致基本不会有影响）

ChromeDriver下载地址：http://npm.taobao.org/mirrors/chromedriver

## 安装
```text
# 安装所需的库
pip install -r requirements.txt

# 启动
python app.py
```

## 配置文件
```json
{
  "Main": {
    "Title": "网站标题"
  },
  "QL": {
    "QL_Name": "QL面板名字",
    "Client_ID": "ID",
    "Client_Secret": "Secret",
    "URL": "QL面板地址（结尾不要有 /）"
  }
}
```

