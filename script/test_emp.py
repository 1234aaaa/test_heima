import requests
import unittest

from parameterized import parameterized

import app
from api.request_api import RequestApi
from utils import read_json_data


class TestEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.login_url = app.PROJECT_URL + "/api/sys/login"
        cls.get_emp_url = app.PROJECT_URL + "/api/sys/user"
        cls.request_api = RequestApi()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    @parameterized.expand(read_json_data(app.BASE_DIR + "/data/test_emp_data.json", method_name="test_login"))
    def test_01_login(self, case_name, request_body, success, code, message, http_code):
        '''
        登陆测试
        :return:
        '''

        print("*" * 30, "测试" + case_name, "*" * 30)
        header = {"Content-type": "application/json;charset=utf-8"}
        response = self.request_api.doPost(self.session, self.login_url, request_body, headers=header)
        app.TOKEN = "Bearer " + response.json().get("data")
        self.assertIn(message, response.json().get("message"))
        self.assertEqual(code, response.json().get("code"))

    @parameterized.expand(read_json_data(app.BASE_DIR + "/data/test_emp_data.json", method_name="test_emp"))
    def test_02_get_user(self, case_name, params, success, code, message, http_code):
        '''
        获取所有用户
        :param case_name:
        :param params:
        :param success:
        :param code:
        :param message:
        :param http_code:
        :return:
        '''
        print("*" * 30, "测试" + case_name, "*" * 30)
        headers = {"Authorization": app.TOKEN}
        response = self.request_api.doGet(self.session, self.get_emp_url, params=params, headers=headers)
        self.assertIn(message, response.json().get("message"))
        self.assertEqual(code, response.json().get("code"))
