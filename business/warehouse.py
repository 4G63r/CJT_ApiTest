#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-20 09:32


class WarehouseBusiness:
    """仓库业务相关操作"""

    def __init__(self, url, session):
        self.url = url
        self.s = session

    def get_warehouse_token(self):
        """获取仓库token"""
        url = '{}/entities/Warehouse/blank?user_req_id=e33e804adx16cb238be2d'.format(self.url)
        json_r = self.s.get(url).json()
        token = json_r.get('txnToken')
        return token

    def get_warehouse_category(self):
        """
        获取仓库分类id
        :return: {分类名称: 分类id} - {'未分类': 691651268182016}
        """
        url = '{}/data/tree/WarehouseCategory?bindVars=&user_req_id=e33e804adx16cb22cd7aa'.format(self.url)
        json_r = self.s.get(url).json()
        return {i.get('name'): i.get('id') for i in json_r}

    def create_warehouse(self, warehouse_name, warehouse_category_id=None):
        if warehouse_category_id is None:
            warehouse_category_id = self.get_warehouse_category().get('未分类')

        url = '{}/entity/Warehouse?user_req_id=e33e804adx16cb22a0428'.format(self.url)
        data = {
            "name": warehouse_name,
            "warehouseCategoryId": warehouse_category_id,
            "comments": "备注是没有备注",
            "statusEnum": "A",
            "txnToken": self.get_warehouse_token()
        }
        text_r = self.s.post(url, json=data).text
        if '仓库名称重复' in text_r:
            raise Exception('仓库名称重复，请创建其他仓库')
        else:
            print('仓库<%s>创建成功，id为1' % warehouse_name)

    def get_warehouse_infos(self):
        """
        查询所有仓库信息
        :return: {仓库名称: 仓库id} - {'总仓': 691651268182017}
        """
        url = '{}/data/grid/Warehouse.list?user_req_id=e33e804adx16cb26d70ac'.format(self.url)
        data = {
            "pageSize": 50,
            "take": 50,
            "skip": 0,
            "page": 1,
            "sort": [],
            "bindVars": {},
            "group": [],
            "criteriaStr": "statusEnum != 'I'"
        }
        r = self.s.post(url, json=data).json().get('data')
        return {i.get('name'): i.get('id') for i in r}

    def get_warehouse_id_by_name(self, warehouse_name):
        """根据仓库名称查询仓库id"""
        warehouse_infos = self.get_warehouse_infos()
        if warehouse_name in warehouse_infos:
            id_ = self.get_warehouse_infos().get(warehouse_name)
        else:
            print('仓库名称<%s>不存在！' % warehouse_name)
            id_ = None
        return id_

    def delete_warehouse_by_name(self, warehouse_name):

        """
        删除仓库
        :param warehouse_name: 举例：总仓
        :return:
        """

        id_ = self.get_warehouse_id_by_name(warehouse_name)
        if id_:
            url = '{}/entity/Warehouse/{}?user_req_id=e33e804adx16cb2663b3e'.format(self.url, id_)
            r = self.s.delete(url)
            if r.status_code == 200:
                print('仓库<%s>删除成功' % warehouse_name)
            else:
                print('仓库<%s>没有成功删除！')
        else:
            raise Exception('仓库名称不存在')
