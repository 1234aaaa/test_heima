from requests import Response


class RequestApi:
    def doGet(self, session, url, params=None, headers=None):
        '''
        :rtype:Response
        处理get请求
        :param url:
        :param params:
        :param headers:
        :return:
        '''
        return session.get(url=url, params=params, headers=headers)

    def doPost(self, session, url, json, params=None, headers=None):
        '''
        :rtype:Response
        :param session:
        :param url:
        :param json:
        :param params:
        :param headers:
        :return:
        '''
        return session.post(url=url, params=params, json=json, headers=headers)
