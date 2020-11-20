# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *
def init(context):
    subscribe(symbols='SHSE.600000', frequency='1d', count=50)
def on_bar(context, bars):
    print(context.data(symbol='SHSE.600000', frequency='1d', count=50, fields='close,bob'))
if __name__ == '__main__':
    run(strategy_id='your strategy_id2',
        filename='main2.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2017-08-21 15:00:00',
        serv_addr='192.168.0.101:7001')


# 别忘了先改.gmserv.json中的hostAddr
