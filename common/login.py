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
        self.access_token = self.__access_token
        self.domain_org = self.__domain_and_orgaccount
        self.url = self.url_with_domain_and_orgaccount
        self.auth = self.__auth
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

    @property
    def __access_token(self):
        if self.platform == 'APP':
            r = self.login_1()
            access_token = r.get('data').get('createToken').get('accessToken')
            return access_token
        else:
            return

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
    def __domain_and_orgaccount(self):
        """
        获取domain和orgaccount值
        :return: {'orgAccount': 'uruqysjoz6oz', 'domainName': 'edbtj1272l'}
        """
        if self.platform == 'APP':
            parse_data = self.login_3().get('data').get('accountBook').get('tenant')
            domain_name = parse_data.get('domainName')
            org_account = parse_data.get('org').get('orgAccount')
            return {'orgAccount': org_account, 'domainName': domain_name}
        else:
            return

    @property
    def url_with_domain_and_orgaccount(self):
        """
        获取url前缀
        :return: https://inte-cloud.chanjet.com/cc/ug3qc3gv0h7m/wcw78mp1n3
        """
        if self.platform == 'APP':
            url = self.host_addr.replace('0000/0', '{}/{}'.format(self.domain_org.get('orgAccount'),
                                                                  self.domain_org.get('domainName')))
        else:
            url = self.host_addr.replace('0000/0', get_conf_value.get_web_uid())
        return url

    @property
    def __auth(self):
        if self.platform == 'APP':
            url = '{}/mobile/cia/graphql?user_req_id=1566209020090_4'.format(self.url)
            data = {
                "query": '\n            mutation CreatePassport {\n                passport: '
                         'createPassportWithAccessToken(accessToken: "%s", domainName: "%s")\n            }\n        ' % (
                             self.access_token, self.domain_org.get('orgAccount')),
                "mutation": '\n            mutation CreatePassport {\n                passport: '
                            'createPassportWithAccessToken(accessToken: "%s", domainName: "%s")\n            }\n '
                            % (self.access_token, self.domain_org.get('orgAccount'))
            }
            headers = {
                'accesstoken': self.access_token
            }
            json_r = baseRequest.base_request('post', url, data=data, headers=headers).json()
            token = json_r.get('data').get('passport')
            return token
        else:
            return get_conf_value.get_web_auth()

    @property
    def __headers(self):
        if self.platform == 'APP':
            headers = {
                'authorization': 'Bearer %s' % self.auth,
                'accesstoken': self.access_token,
            }
        else:
            headers = {
                'authorization': self.auth,
                # 'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, '
                              'like Gecko) Version/12.1.2 Safari/605.1.15'
            }
        return headers

    def session_by_login(self):
        if self.platform == 'APP':
            url = '{}/mobile/graphql?user_req_id=1566229590096_40'.format(self.url)
            data = {
                "query": "\n            query getAccountBookCount {\n                accountBooksCount: "
                         "getAccountBookCount {\n                    count\n                }\n            }\n        ",
                "variables": {}
            }
        else:
            url = '{}/messageCenter/query?user_req_id=e33e804adx16cb21aec86'.format(self.url)
            data = {
                "moduleType": 1,
                "pageSize": 20,
                "take": 20,
                "skip": 0,
                "page": 1,
                "sort": [],
                "group": []
            }
        return baseRequest.session_('post', url, data=data, headers=self.__headers)
