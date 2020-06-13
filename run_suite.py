import unittest
import time

from BeautifulReport import BeautifulReport

# 运行测试用例并生成测试报告
import app

dir = app.BASE_DIR
report_name = "tpshop_report{}.html".format(time.strftime("%Y%m%d%H%M%S"))
suite = unittest.TestLoader().discover(dir + "/script", pattern="test*.py")
BeautifulReport(suite).report(filename=report_name, description="TpShop报告", log_path=dir + "/report")
