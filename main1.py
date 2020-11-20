
# coding=utf-8
from __future__ import print_function, absolute_import, unicode_literals
from gm.api import *
def init(context):
    subscribe(symbols='SHSE.600000', frequency='1d')
def on_bar(context, bars):
    # 打印当前获取的bar信息
    bar = bars[0]
    # 执行策略逻辑操作
    print(bar)
if __name__ == '__main__':
    run(strategy_id='aaaaaa',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='token_id',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2016-07-21 15:00:00',
        serv_addr='192.168.0.101:7001')
        
        
# 别忘了先改.gmserv.json中的hostAddr

