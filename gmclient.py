# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *
def init(context):
    schedule(schedule_func=algo, date_rule='1d', time_rule='14:50:00')
def algo(context):
    # 购买200股浦发银行股票
    order_volume(symbol='SHSE.600000', volume=200, side=OrderSide_Buy,
                 order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0)
if __name__ == '__main__':
    run(strategy_id='your strategy_id', 
        filename='gmclient.py',  # 保持与此文件名一致
        mode=MODE_BACKTEST, 
        token='21ab3ffbdf89ee58ea9132e243d8164b3b53a47e',
        backtest_start_time='2016-06-17 13:00:00', 
        backtest_end_time='2017-08-21 15:00:00',
        serv_addr='192.168.0.100:7001')
        # users 下IP:PORT .goldminer3\.gmserv.json
