# 说明
JDCookie获取Python 学习版

当前状态：未开发完毕

没有写文字验证部分和Selenium多实例管理，只支持同时间单用户使用

# 修改
Chromedriver目录内置版本：96.0.4664.45（自行按需求更改）

查看自己的谷歌浏览器版本：设置 - 关于Chrome（关于版本选择，假如我的浏览器版本是96.0.4664.45，我们在驱动下载页面选择96.0.4664就可以了，最后一位小数点版本不一致基本不会有影响）

ChromeDriver下载地址：http://npm.taobao.org/mirrors/chromedriver

## 安装
运行环境(必须)：Python3.7 +

```text
# 安装所需工具(栗子：CentOS)
yum install wget git

# 安装所需的库
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 启动
python app.py
```

体验地址：http://自己的IP:5000

## 配置文件
```json
{
  "Main": {
    "Title": "网站标题"
  },
  "Selenium Addr": "Dcoker Chrome地址",
  "QL": {
    "QL_Name": "QL面板名字",
    "Client_ID": "ID",
    "Client_Secret": "Secret",
    "URL": "QL面板地址（结尾不要有 /）"
  }
}
```

## 错误排查

Q：等待添加

A：等待添加
