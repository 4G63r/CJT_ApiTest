#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-19 18:01

from common import baseRequest
from utils import get_conf_value


class Login:
    def __init__(self, username=None, password=None):
        ua_info = get_conf_value.get_account_info()
        if username is None and password is None:
            self.username = ua_info.get('username')
            self.password = ua_info.get('password')
        else:
            self.username = username
            self.password = password

        self.platform = get_conf_value.get_platform()
        self.host_addr = get_conf_value.get_host_addr()
        self.access_token = self._access_token
        self.domain_org = self._domain_and_orgaccount
        self.url = self.url_with_domain_and_orgaccount
        self._auth = self.auth
        self.session = self.session_by_login()

    def login_1(self):
        url = '{}/mobile/cia/graphql?user_req_id=1566209016114_0'.format(self.host_addr)
        data = {
            "query": "\n    fragment OrgType on Org {\n        id\n        name\n        account\n        isInitial\n "
                     "   }\n\n    fragment AppSubscribeType on AppSubscription {\n        status\n        startDate\n "
                     "       endDate\n        license\n        org {\n            ...OrgType\n        }\n    }\n\n    "
                     "mutation Login($username: String!, $password: String!) {\n        createToken(username: "
                     "$username, password: $password) {\n            accessToken\n            refreshToken\n          "
                     "  viewer {\n                id\n                name\n                headPicture(size: "
                     "MIDDLE)\n                mobile\n                email\n                orgId\n                "
                     "defaultOrg {\n                    ...OrgType\n                }\n                defaultAppOrg{"
                     "\n                    ...OrgType\n                }\n                orgs {\n                   "
                     " ...OrgType\n                }\n                appSubscribes {\n                    "
                     "...AppSubscribeType\n                }\n                #                subscribes {\n         "
                     "       #                    status\n                #                    startDate\n            "
                     "    #                    endDate\n                #                    license\n                "
                     "#                    appId\n                #                    appName\n                #     "
                     "               org {\n                #                        id\n                #            "
                     "            name\n                #                        account\n                #           "
                     "             isInitial\n                #                        logo\n                #        "
                     "            }\n                #                }\n            }\n        }\n    }\n",
            "variables": {
                "username": self.username,
                "password": self.password
            },
            "mutation": "\n    fragment OrgType on Org {\n        id\n        name\n        account\n        "
                        "isInitial\n    }\n\n    fragment AppSubscribeType on AppSubscription {\n        status\n     "
                        "   startDate\n        endDate\n        license\n        org {\n            ...OrgType\n      "
                        "  }\n    }\n\n    mutation Login($username: String!, $password: String!) {\n        "
                        "createToken(username: $username, password: $password) {\n            accessToken\n           "
                        " refreshToken\n            viewer {\n                id\n                name\n              "
                        "  headPicture(size: MIDDLE)\n                mobile\n                email\n                "
                        "orgId\n                defaultOrg {\n                    ...OrgType\n                }\n     "
                        "           defaultAppOrg{\n                    ...OrgType\n                }\n               "
                        " orgs {\n                    ...OrgType\n                }\n                appSubscribes {"
                        "\n                    ...AppSubscribeType\n                }\n                #              "
                        "  subscribes {\n                #                    status\n                #               "
                        "     startDate\n                #                    endDate\n                #              "
                        "      license\n                #                    appId\n                #                 "
                        "   appName\n                #                    org {\n                #                    "
                        "    id\n                #                        name\n                #                     "
                        "   account\n                #                        isInitial\n                #            "
                        "            logo\n                #                    }\n                #                "
                        "}\n            }\n        }\n    }\n "
        }
        json_r = baseRequest.base_request('post', url, data=data).json()
        return json_r

    def login_web(self):
        url = 'https://inte-passport.chanjet.com/loginV2/webLogin?callback=jQuery111308033636904233341_1566266649823&auth_username=15899991005&password=e10adc3949ba59abbe56e057f20f883e&auth_code=4H1PLP&jsonp=1&_=1566266649827'

    @property
    def _access_token(self):
        r = self.login_1()
        access_token = r.get('data').get('createToken').get('accessToken')
        return access_token

    def login_2(self):
        url = '{}/mobile/cia/graphql?user_req_id=1566209018073_1'.format(self.host_addr)
        data = {
            "query": "\n            query findAccountBooks {\n                accountBooks: findAccountBooks {\n      "
                     "              isDefault\n                    tenant{\n                        id\n              "
                     "          name\n                        code\n                        domainName\n              "
                     "          createdStamp\n                        isHidden\n                        disabled\n    "
                     "                    enterpriseId\n                        org{\n                            "
                     "orgId\n                            orgName\n                            orgFullName\n           "
                     "                 orgAccount\n                        }\n                        tenantHkj{\n    "
                     "                        acctgSystemId\n                            taxpayerTypeEnum\n           "
                     "             }\n                    }\n                }\n            }\n        ",
            "variables": {}
        }
        headers = {
            'accesstoken': self.access_token
        }
        json_r = baseRequest.base_request('post', url, data=data, headers=headers).json()
        return json_r

    def login_3(self):
        url = '{}/mobile/cia/graphql?user_req_id=1566209018662_2'.format(self.host_addr)
        data = {
            "query": "\n            query getDefaultAccountBook {\n                accountBook: getDefaultAccountBook "
                     "{\n                    isDefault\n                    tenant{\n                        id\n     "
                     "                   name\n                        code\n                        domainName\n     "
                     "                   createdStamp\n                        isHidden\n                        "
                     "disabled\n                        enterpriseId\n                        tenantHkj{\n            "
                     "                acctgSystemId\n                            taxpayerTypeEnum\n                   "
                     "     }\n                        org{\n                            orgId\n                       "
                     "     orgName\n                            orgFullName\n                            orgAccount\n "
                     "                       }\n                    }\n                }\n            }\n        ",
            "variables": {}
        }
        headers = {
            'accesstoken': self.access_token
        }
        json_r = baseRequest.base_request('post', url, data=data, headers=headers).json()
        return json_r

    @property
    def _domain_and_orgaccount(self):
        """
        获取domain和orgaccount值
        :return: {'orgAccount': 'uruqysjoz6oz', 'domainName': 'edbtj1272l'}
        """
        parse_data = self.login_3().get('data').get('accountBook').get('tenant')
        domain_name = parse_data.get('domainName')
        org_account = parse_data.get('org').get('orgAccount')
        return {'orgAccount': org_account, 'domainName': domain_name}

    @property
    def url_with_domain_and_orgaccount(self):
        """
        获取url前缀
        :return: https://inte-cloud.chanjet.com/cc/ug3qc3gv0h7m/wcw78mp1n3
        """
        url = self.host_addr.replace('0000/0', '{}/{}'.format(self.domain_org.get('orgAccount'),
                                                              self.domain_org.get('domainName')))
        return url

    @property
    def auth(self):
        url = '{}/mobile/cia/graphql?user_req_id=1566209020090_4'.format(self.url)
        data = {
            "query": '\n            mutation CreatePassport {\n                passport: '
                     'createPassportWithAccessToken(accessToken: "%s", domainName: "%s")\n            }\n        ' % (
                         self.access_token, self.domain_org.get('orgAccount')),
            "mutation": '\n            mutation CreatePassport {\n                passport: '
                        'createPassportWithAccessToken(accessToken: "%s", domainName: "%s")\n            }\n        '
                        % (self.access_token, self.domain_org.get('orgAccount'))
        }
        headers = {
            'accesstoken': self.access_token
        }
        json_r = baseRequest.base_request('post', url, data=data, headers=headers).json()
        token = json_r.get('data').get('passport')
        return token

    @property
    def _headers(self):
        headers = {
            'authorization': 'Bearer %s' % self._auth,
            'accesstoken': self.access_token,
        }
        return headers

    def session_by_login(self):
        url = '{}/mobile/graphql?user_req_id=1566229590096_40'.format(self.url)
        data = {
            "query": "\n            query getAccountBookCount {\n                accountBooksCount: "
                     "getAccountBookCount {\n                    count\n                }\n            }\n        ",
            "variables": {}
        }
        s = baseRequest.session_('post', url, data=data, headers=self._headers)
        return s