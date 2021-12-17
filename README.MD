# 说明
JDCookie获取Python版

当前状态：未开发完毕

可用性（已测）：amd64_Win、amd64_Linux、amd64_Mac

# 修改
Chromedriver目录内置版本：96.0.4664.45（自行按需求更改）

查看自己的谷歌浏览器版本：设置 - 关于Chrome（关于版本选择，假如我的浏览器版本是96.0.4664.45，我们在驱动下载页面选择96.0.4664就可以了，最后一位小数点版本不一致基本不会有影响）

ChromeDriver下载地址：http://npm.taobao.org/mirrors/chromedriver

## 安装
运行环境(必须)：Python3.7 +

```text
# 安装所需工具(栗子：CentOS)
yum install wget git unzip

# 安装所需的库
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 创建目录
mkdir chromedriver && cd chromedriver

# 安装Selenium
wget https://mirrors.huaweicloud.com/chromium-browser-snapshots/Linux_x64/884014/chrome-linux.zip && unzip chrome-linux.zip
wget https://npm.taobao.org/mirrors/chromedriver/92.0.4515.43/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && cd ..

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
  "QL": {
    "QL_Name": "QL面板名字",
    "Client_ID": "ID",
    "Client_Secret": "Secret",
    "URL": "QL面板地址（结尾不要有 /）"
  }
}
```

## 错误排查

Q：ImportError: libGL.so.1: cannot open shared object file: No such file or directory
A：解决方法：yum install mesa-libGL.x86_64

Q：
A：

