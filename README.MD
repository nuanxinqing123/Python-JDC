# 说明
JDCookie获取Python 学习版

当前状态：未开发完毕（仅保留QQ扫码）

没有写过验证码部分和Selenium多实例管理，只支持同时间单用户使用

## 驱动

ChromeDriver下载地址：https://alist.6b7.org/JD/BrowserDrive

在项目同级创建chromedriver目录

选择自己系统的驱动下载并解压到chromedriver目录里面

## 安装
运行环境(必须)：Python3.7 +

```text
# 安装所需工具(栗子：CentOS)
yum install git

# 拉取源码
git clone https://github.com/nuanxinqing123/Python-JDC

# 安装所需的库
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 启动
python3 app.py
```

体验地址：http://自己的IP:5100

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

## 错误排查

Q：等待添加

A：等待添加
