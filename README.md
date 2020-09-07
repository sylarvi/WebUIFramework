# WebUIFranmework

基于Python+selenium+unittest的Web UI自动化测试框架

Config

```
--config.ini   	测试配置文件
```

Email

```
--Email_handle.py  		基于smtplib与email.mime模块对发送测试报告邮件功能的封装
```

Framework

```
--BasePage.py				基于selenium模块对各个页面操作方法的封装
--BrowserEngine.py			封装webdriver类，初始化webdriver对象
--KeyBoardUtil.py			基于win32api, win32con模块对键盘动作方法的封装
```

Logs

```
--Logger.py  log模块
```

Run

```
--Run_main.py   脚本主程序入口
```

Screenshots

```
-- 截图保存路径
```

TestReport

```
-- 测试结果保存路径
--HTMLTestRunner.py 测试报告模板
```

Testsuits

```
 测试用例集
--case01_search.py  
--case02_pageswitch.py
--case03_login.py
--case04_writepost.py

```

Tools

```
webdriver驱动程序
--chromedriver.exe chrome浏览器
--geckodriver.exe firfox浏览器
--IEDriverServer.exe ie浏览器
```

