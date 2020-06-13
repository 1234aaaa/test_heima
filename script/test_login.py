import requests
import unittest

from parameterized import parameterized

import app
from api.request_api import RequestApi
from utils import read_json_data


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_url = app.PROJECT_URL + "/api/sys/login"
        cls.request_api = RequestApi()
        cls.header = {"Content-type": "application/json;charset=utf-8"}

    def setUp(self):
        self.session = requests.session()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_json_data(app.BASE_DIR + "/data/test_login_data.json"))
    def test_login(self, case_name, request_body, success, code, message, http_code):
        '''
        登陆测试
        :return:
        '''
        print("*" * 30, "测试" + case_name, "*" * 30)
        response = self.request_api.doPost(self.session, self.login_url, request_body, headers=self.header)
        self.assertIn(message, response.json().get("message"))
        self.assertEqual(code, response.json().get("code"))
