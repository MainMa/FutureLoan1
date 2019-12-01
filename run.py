# Author: Cup
# Time: 2019/11/16 17:00

import unittest
import os
from datetime import datetime
from HTMLTestRunnerNew import HTMLTestRunner
from scripts.log_info import log
from scripts.my_config import YmlConfig
from scripts.handle_path import REPORTS_DIR
from scripts.handle_path import USER_INFO_CONF_FILE
from scripts.handle_path import CASES_DIR
from scripts.handle_user import HandleUser
from cases.test_05_invest import TestCaseInvest

if not os.path.exists(USER_INFO_CONF_FILE):
    HandleUser().create_user_conf()

# 先加上这行不会有问题的，嗯！
suite = unittest.TestSuite()
# 添加一个路径
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASES_DIR))

# 用html接收结果
# stream  文件句柄
# # verbosity  默认参数，暂时不管
# # title 报告标题
# # description 描述
# # tester 作者
config = YmlConfig()
time = datetime.strftime(datetime.now(),'%Y%m%d%H%M%S')
report_name = f"{config.read_yml_config('test_report','report_name')}_{time}.html"
report_name = os.path.join(REPORTS_DIR,report_name)
report_title = config.read_yml_config('test_report','report_title')
report_descripition = config.read_yml_config('test_report','report_descripition')
report_tester = config.read_yml_config('test_report','report_tester')

runner = HTMLTestRunner(stream=open(report_name,'wb'),
                        verbosity=2,title=report_title,
                        description=report_descripition,
                        tester=report_tester)
runner.run(suite)
log.info('用例执行完成')
