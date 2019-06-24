# -*- coding: utf-8 -*-
__author__ = 'yi.liu'


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        # 将所有的雇佣可能性找出来
        # 计算每一种可能性是否合理，工作质量与工资成正比，优先满足质量最高的工资，计算合理性
        # 计算最小花费

        # 期望工资与工作质量之间的比值，说明这个人的价值，越小表明这个人越应该雇佣，但不符合
        # 雇佣期望工资最少的

        # 先将质量值按从低到高排列
        # 计算所有其他人的质量值
        # 计算出所有其他人的倍数，计算出最低k个人需要的金钱
        {"result": 0, "msg": string, "data": [
            {
                "member_id": string, 会员ID
                "amount": number, 本次充值或消费金额
                "bonus": number, 充值时赠送金额
                "payment": string, 支付方式，现金：1，微信主扫：2，支付宝主扫：3，银联：4, 会员卡：5，微信客扫：6，支付宝客扫：7
                "date": date, 创建时间
                "balance": number, 会员当前账户余额
                "type": integer, 1 充值 2 消费
                "order_no": string, 订单号
            }
        ],
         "total":integer 记录总条数}


