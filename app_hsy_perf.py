#!/usr/bin/env python

# @Author: songxiao
# @Time: 2019-08-26 19:57

from time import sleep
from common import baseRequest

ua = 'https://cloud.chanjet.com/hsy/uesuexdopqjy/h1pn5f969l'
# ua = 'https://hotfix-cloud.chanjet.com/hsy/usidiqxv8d56/tg08auxjqe'
headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI4N2E2NzBiZC1mNTQzLTQwOTctOTlkNC1jNWZjYTM1YzI4NDMiLCJpYXQiOjE1NjY4OTI4OTF9.obhsd7copxws2ONSQDwuALkUVqz3fKDY8lEklIW25cw'
    # 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMGQzZTM5ZC1mYzYxLTRlZmEtOTljMy05NzE4NjM1ODcwNDgiLCJpYXQiOjE1NjY4ODQ4Mzh9.NxUxItNqhGOOxkC05Dit9PiHito45ua9T58c0IhPKmY'
}


# 统计装饰器
def decorator(func):
    def bb():
        li = [func() for _ in range(10)]
        print(li)
        print('平均值：%s秒' % round(sum(li) / len(li), 2))
        for i in range(len(li)):
            # print('第%s次请求的响应时间为%s秒' % (i + 1, li[i]))
            print(li[i])

    return bb


# 今日日报首页
# @decorator
# def a1():
#     url = '{}/homepage/measureQuery?user_req_id=df8f71ac8x16cd0e0dc53'.format(ua)
#     data = [{
#         "measures": ["goodsIssueAmount", "goodsIssueCount", "firstTransCustAmount", "firstTransCustCount",
#                      "firstTransCustPrice", "oldTransCustCount", "oldTransCustAmount", "oldTransCustPrice",
#                      "grossMargin", "salesRevenue", "goodsReturnCount", "goodsReturnAmount", "stockoutAndReciptCount",
#                      "agoStockoutAndReciptCount", "replenishedStockoutCount", "replenishedReceiptCount",
#                      "stockoutUnreceiptCount", "receiptUnstockoutCount", "unstockoutUnreceiptCount",
#                      "totalPaymentApCount", "totalPaymentApAmount", "goodsReceiptAmount", "goodsReceiptCount",
#                      "prepaidPaymentArCount", "prepaidPaymentArAmount", "cashPaymentArCount", "cashPaymentArAmount",
#                      "arrearsPaymentArCount", "arrearsPaymentArAmount", "totalPaymentArAmount", "totalPaymentArCount",
#                      "revenueAmount", "revenueCount", "expenseAmount", "expenseCount", "stockOutAmount",
#                      "stockOutCount", "stockInAmount", "stockInCount", "stockTransferCount", "stockCountCount",
#                      "stockCountSubCount"],
#         "time": "20190827,20190827"
#     }]
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)


# 经营流水
@decorator
def jyls():
    url = '{}/mobile/graphql?user_req_id=1566893060082_60'.format(ua)
    data = {
        "query": "query ReportSalesJournal($ignoreMonth:Boolean = False,$ignoreYear:Boolean = False,$month:Object!,$year:Object!) { month:SummaryOperatingJournal(criteriaStr:\"DATE_FORMAT(date,'%Y%m')=:month\",bindVars:[{name:\"month\",value:$month}],sortBy:[{fieldName:\"date\",order:\"DESC\"}]) @skip(if:$ignoreMonth) { date firstCount:firstTransCustCount firstAmount:firstTransAmount oldCount:oldTransCustCount oldAmount:oldTransAmount count:goodsIssueCount amount:goodsIssueAmount } year:SummaryOperationByMonth(criteriaStr:\"dimMonthId.acctgYear=:year\",bindVars:[{name:\"year\",value:$year}],sortBy:[{fieldName:\"dimMonthId\",order:\"ASC\"}]) @skip(if:$ignoreYear) { date:dimMonthId { month:acctgMonth year:acctgYear } firstCount:firstTransCustCount firstAmount:firstTransAmount oldCount:oldTransCustCount oldAmount:oldTransAmount count:goodsIssueCount amount:goodsIssueAmount } }",
        "variables": {
            "ignoreMonth": False,
            "ignoreYear": True,
            "month": "201908",
            "year": 2019
        },
        "timeout": 60000
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 今日
# @decorator
# def today():
#     url = '{}/mobile/graphql?user_req_id=1566894119487_124'.format(ua)
#     data = {
#         "query": "query bossTodaySaleInfoAndSaleProfit { saleInfo:MBSaleInfoMeasures { count:goodsIssueCount(time:TODAY) amount:goodsIssueAmount(time:TODAY) returnCount:goodsReturnCount(time:TODAY) returnAmount:goodsReturnAmount(time:TODAY) } saleProfit:AggregateGoodsIssueDetail(criteriaStr:\"DATE_FORMAT(masterVoucherId.bizDate,'%Y%m%d') = DATE_FORMAT(NOW(),'%Y%m%d')\") { amount:baseNetAmountWithoutTax cost:vCostAmount } }",
#         "fetchPolicy": "network-only"
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)

# 昨日
# @decorator
# def yesterday():
#     url = '{}/mobile/graphql?user_req_id=1566894119487_124'.format(ua)
#     data = {
#         "query": "query bossYesterdaySaleInfoAndSaleProfit { saleInfo:MBSaleInfoMeasures { count:goodsIssueCount(time:YESTERDAY) amount:goodsIssueAmount(time:YESTERDAY) returnCount:goodsReturnCount(time:YESTERDAY) returnAmount:goodsReturnAmount(time:YESTERDAY) } saleProfit:AggregateGoodsIssueDetail(criteriaStr:\"DATE_FORMAT(masterVoucherId.bizDate,'%Y%m%d') = DATE_FORMAT(DATE_SUB(NOW(),INTERVAL 1 DAY),'%Y%m%d')\") { amount:baseNetAmountWithoutTax cost:vCostAmount } }",
#         "fetchPolicy": "network-only"
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)

# 客户情况
@decorator
def khqk():
    url = '{}/mobile/graphql?user_req_id=1566896098053_241'.format(ua)
    data = {
        "query": {
            "kind": "Document",
            "definitions": [{
                "kind": "OperationDefinition",
                "operation": "query",
                "variableDefinitions": [],
                "directives": [],
                "selectionSet": {
                    "kind": "SelectionSet",
                    "selections": [{
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "custVendor"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "MBCustVendorMeasures"
                        },
                        "arguments": [],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstCount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstAmount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustAmount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstPrice"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustPrice"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningCount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningAmount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustAmount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningPrice"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustPrice"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }]
                        }
                    }, {
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "revenue"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "MBPaymentMeasures"
                        },
                        "arguments": [],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "preCollect"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "prepaidPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearance"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "cashPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "reCollect"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "arrearsPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "THIS_MONTH"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }]
                        }
                    }, {
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "revenue_detail"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "AggregatePaymentDetailAR"
                        },
                        "arguments": [{
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "criteriaStr"
                            },
                            "value": {
                                "kind": "StringValue",
                                "value": "",
                                "block": False
                            }
                        }, {
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "sortBy"
                            },
                            "value": {
                                "kind": "ListValue",
                                "values": [{
                                    "kind": "ObjectValue",
                                    "fields": [{
                                        "kind": "ObjectField",
                                        "name": {
                                            "kind": "Name",
                                            "value": "fieldName"
                                        },
                                        "value": {
                                            "kind": "StringValue",
                                            "value": "amount",
                                            "block": False
                                        }
                                    }, {
                                        "kind": "ObjectField",
                                        "name": {
                                            "kind": "Name",
                                            "value": "order"
                                        },
                                        "value": {
                                            "kind": "StringValue",
                                            "value": "DESC",
                                            "block": False
                                        }
                                    }]
                                }]
                            }
                        }],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "name": {
                                    "kind": "Name",
                                    "value": "amount"
                                },
                                "arguments": [],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "paymentMethod"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "paymentMethodTypeId"
                                },
                                "arguments": [],
                                "directives": [],
                                "selectionSet": {
                                    "kind": "SelectionSet",
                                    "selections": [{
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "id"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }, {
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "code"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }, {
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "name"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }],
            "loc": {
                "start": 0,
                "end": 1627
            }
        }
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 钱货未清&钱货两清
@decorator
def qhlq():
    url = '{}/mobile/graphql?user_req_id=1566895644378_234'.format(ua)
    data = {
        "query": {
            "kind": "Document",
            "definitions": [{
                "kind": "OperationDefinition",
                "operation": "query",
                "variableDefinitions": [],
                "directives": [],
                "selectionSet": {
                    "kind": "SelectionSet",
                    "selections": [{
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "clearance"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "MBClearanceMeasures"
                        },
                        "arguments": [],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "unclearedTotal"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "totalUnstockoutOrUnreceiptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "unclearedExport"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "stockoutUnreceiptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "unclearedGain"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "receiptUnstockoutCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "unclearedNone"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "unstockoutUnreceiptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceTotal"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "totalStockoutAndReciptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceToday"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "stockoutAndReciptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceTotalAgo"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "totalAgoStockoutAndReciptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceResend"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "replenishedStockoutCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceRepay"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "replenishedReceiptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearanceAgo"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "agoStockoutAndReciptCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }]
                        }
                    }]
                }
            }],
            "loc": {
                "start": 0,
                "end": 1462
            }
        }
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


# 本月
# @decorator
# def a2():
#     url = '{}/mobile/graphql?user_req_id=1566893954419_117'.format(ua)
#     data = {
#         "query": "query bossMonthSaleInfoAndSaleProfit { saleInfo:MBSaleInfoMeasures { count:goodsIssueCount(time:THIS_MONTH) amount:goodsIssueAmount(time:THIS_MONTH) returnCount:goodsReturnCount(time:THIS_MONTH) returnAmount:goodsReturnAmount(time:THIS_MONTH) } saleProfit:AggregateGoodsIssueDetail(criteriaStr:\"DATE_FORMAT(masterVoucherId.bizDate,'%Y%m') = DATE_FORMAT(NOW(),'%Y%m')\") { amount:baseNetAmountWithoutTax cost:vCostAmount } }",
#         "fetchPolicy": "network-only"
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)

#
# 销售统计
@decorator
def xstj():
    url = '{}/mobile/graphql?user_req_id=1566895396812_229'.format(ua)
    data = {
        "query": {
            "kind": "Document",
            "definitions": [{
                "kind": "OperationDefinition",
                "operation": "query",
                "variableDefinitions": [{
                    "kind": "VariableDefinition",
                    "variable": {
                        "kind": "Variable",
                        "name": {
                            "kind": "Name",
                            "value": "schemeId"
                        }
                    },
                    "type": {
                        "kind": "NonNullType",
                        "type": {
                            "kind": "NamedType",
                            "name": {
                                "kind": "Name",
                                "value": "String"
                            }
                        }
                    }
                }, {
                    "kind": "VariableDefinition",
                    "variable": {
                        "kind": "Variable",
                        "name": {
                            "kind": "Name",
                            "value": "filters"
                        }
                    },
                    "type": {
                        "kind": "NonNullType",
                        "type": {
                            "kind": "NamedType",
                            "name": {
                                "kind": "Name",
                                "value": "GraphQLJSON"
                            }
                        }
                    }
                }, {
                    "kind": "VariableDefinition",
                    "variable": {
                        "kind": "Variable",
                        "name": {
                            "kind": "Name",
                            "value": "firstResult"
                        }
                    },
                    "type": {
                        "kind": "NamedType",
                        "name": {
                            "kind": "Name",
                            "value": "Long"
                        }
                    }
                }, {
                    "kind": "VariableDefinition",
                    "variable": {
                        "kind": "Variable",
                        "name": {
                            "kind": "Name",
                            "value": "maxResult"
                        }
                    },
                    "type": {
                        "kind": "NamedType",
                        "name": {
                            "kind": "Name",
                            "value": "Long"
                        }
                    }
                }],
                "directives": [],
                "selectionSet": {
                    "kind": "SelectionSet",
                    "selections": [{
                        "kind": "Field",
                        "name": {
                            "kind": "Name",
                            "value": "reportSearch"
                        },
                        "arguments": [{
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "schemeId"
                            },
                            "value": {
                                "kind": "Variable",
                                "name": {
                                    "kind": "Name",
                                    "value": "schemeId"
                                }
                            }
                        }, {
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "filters"
                            },
                            "value": {
                                "kind": "Variable",
                                "name": {
                                    "kind": "Name",
                                    "value": "filters"
                                }
                            }
                        }, {
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "firstResult"
                            },
                            "value": {
                                "kind": "Variable",
                                "name": {
                                    "kind": "Name",
                                    "value": "firstResult"
                                }
                            }
                        }, {
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "maxResult"
                            },
                            "value": {
                                "kind": "Variable",
                                "name": {
                                    "kind": "Name",
                                    "value": "maxResult"
                                }
                            }
                        }],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "name": {
                                    "kind": "Name",
                                    "value": "data"
                                },
                                "arguments": [],
                                "directives": []
                            }]
                        }
                    }]
                }
            }],
            "loc": {
                "start": 0,
                "end": 310
            }
        },
        "variables": {
            "schemeId": 501,
            "filters": {
                "criteriaStr": "masterVoucherId.bizDate >= FROM_UNIXTIME(:V0) AND masterVoucherId.bizDate <= FROM_UNIXTIME(:V1)",
                "havingStr": "",
                "bindVars": {
                    "V0": 1564588800,
                    "V1": 1567267199
                },
                "sortBy": [{
                    "fieldName": "netAmountWithTax",
                    "order": "desc"
                }]
            },
            "firstResult": 0,
            "maxResult": 15
        }
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=70)
    return round(r.elapsed.total_seconds(), 2)


# 销售日报
@decorator
def xsrb():
    url = '{}/mobile/graphql?user_req_id=1566895644380_235'.format(ua)
    data = {
        "query": {
            "kind": "Document",
            "definitions": [{
                "kind": "OperationDefinition",
                "operation": "query",
                "variableDefinitions": [],
                "directives": [],
                "selectionSet": {
                    "kind": "SelectionSet",
                    "selections": [{
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "custVendor"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "MBCustVendorMeasures"
                        },
                        "arguments": [],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstCount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstAmount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustAmount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "firstPrice"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "firstTransCustPrice"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningCount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningAmount"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustAmount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "returningPrice"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "oldTransCustPrice"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }]
                        }
                    }, {
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "revenue"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "MBPaymentMeasures"
                        },
                        "arguments": [],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "preCollect"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "prepaidPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "clearance"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "cashPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "reCollect"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "arrearsPaymentArCount"
                                },
                                "arguments": [{
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "time"
                                    },
                                    "value": {
                                        "kind": "EnumValue",
                                        "value": "TODAY"
                                    }
                                }, {
                                    "kind": "Argument",
                                    "name": {
                                        "kind": "Name",
                                        "value": "departmentIds"
                                    },
                                    "value": {
                                        "kind": "ListValue",
                                        "values": []
                                    }
                                }],
                                "directives": []
                            }]
                        }
                    }, {
                        "kind": "Field",
                        "alias": {
                            "kind": "Name",
                            "value": "revenue_detail"
                        },
                        "name": {
                            "kind": "Name",
                            "value": "AggregatePaymentDetailAR"
                        },
                        "arguments": [{
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "criteriaStr"
                            },
                            "value": {
                                "kind": "StringValue",
                                "value": "amount>0 and DATE_FORMAT(masterVoucherId.bizDate,'%Y%m%d') = DATE_FORMAT(NOW(),'%Y%m%d') AND paymentMethodTypeId is not NULL ",
                                "block": False
                            }
                        }, {
                            "kind": "Argument",
                            "name": {
                                "kind": "Name",
                                "value": "sortBy"
                            },
                            "value": {
                                "kind": "ListValue",
                                "values": [{
                                    "kind": "ObjectValue",
                                    "fields": [{
                                        "kind": "ObjectField",
                                        "name": {
                                            "kind": "Name",
                                            "value": "fieldName"
                                        },
                                        "value": {
                                            "kind": "StringValue",
                                            "value": "amount",
                                            "block": False
                                        }
                                    }, {
                                        "kind": "ObjectField",
                                        "name": {
                                            "kind": "Name",
                                            "value": "order"
                                        },
                                        "value": {
                                            "kind": "StringValue",
                                            "value": "DESC",
                                            "block": False
                                        }
                                    }]
                                }]
                            }
                        }],
                        "directives": [],
                        "selectionSet": {
                            "kind": "SelectionSet",
                            "selections": [{
                                "kind": "Field",
                                "name": {
                                    "kind": "Name",
                                    "value": "amount"
                                },
                                "arguments": [],
                                "directives": []
                            }, {
                                "kind": "Field",
                                "alias": {
                                    "kind": "Name",
                                    "value": "paymentMethod"
                                },
                                "name": {
                                    "kind": "Name",
                                    "value": "paymentMethodTypeId"
                                },
                                "arguments": [],
                                "directives": [],
                                "selectionSet": {
                                    "kind": "SelectionSet",
                                    "selections": [{
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "id"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }, {
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "code"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }, {
                                        "kind": "Field",
                                        "name": {
                                            "kind": "Name",
                                            "value": "name"
                                        },
                                        "arguments": [],
                                        "directives": []
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }],
            "loc": {
                "start": 0,
                "end": 1707
            }
        }
    }
    r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
    return round(r.elapsed.total_seconds(), 2)


#
#
# # 付款情况
# @decorator
# def a5():
#     url = '{}/data/grid/PaymentAP.voucher?user_req_id=df8f71ac8x16cd1293d3f'.format(ua)
#     data = {
#         "pageSize": 50,
#         "take": 50,
#         "skip": 0,
#         "page": 1,
#         "sort": [],
#         "bindVars": {},
#         "group": [],
#         "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
#         "havingStr": ""
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)
#
#
# # 日常收入
# @decorator
# def a6():
#     url = '{}/data/grid/Revenue.voucher?user_req_id=df8f71ac8x16cd12c392f'.format(ua)
#     data = {
#         "pageSize": 50,
#         "take": 50,
#         "skip": 0,
#         "page": 1,
#         "sort": [],
#         "bindVars": {},
#         "group": [],
#         "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
#         "havingStr": ""
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)
#
#
# # 日常支出
# @decorator
# def a7():
#     url = '{}/data/grid/Expense.voucher?user_req_id=df8f71ac8x16cd12e1a43'.format(ua)
#     data = {
#         "pageSize": 50,
#         "take": 50,
#         "skip": 0,
#         "page": 1,
#         "sort": [],
#         "bindVars": {},
#         "group": [],
#         "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY) AND bizTypeId <> 100332",
#         "havingStr": ""
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)
#
#
# # 其他入库
# @decorator
# def a8():
#     url = '{}/data/grid/StockIn.voucher?user_req_id=df8f71ac8x16cd12ff69c'.format(ua)
#     data = {
#         "pageSize": 50,
#         "take": 50,
#         "skip": 0,
#         "page": 1,
#         "sort": [],
#         "bindVars": {},
#         "group": [],
#         "criteriaStr": "bizDate >= DATE(20190101) AND bizDate < DATE_ADD(DATE('20191231'),INTERVAL 1 DAY)",
#         "havingStr": ""
#     }
#     r = baseRequest.base_request('post', url, headers=headers, data=data, timeout=60)
#     return round(r.elapsed.total_seconds(), 2)


if __name__ == '__main__':
    print('↓开始获取性能指标↓\n')

    khqk()

    print('\n↑性能指标获取完成↑')
