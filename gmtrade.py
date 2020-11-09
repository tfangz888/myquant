# 接口查询和委托示例
# 本示例运行于python3.6及以上版本
from gmtrade.api import *
# token身份认证，掘金登录后可在仿真交易官网获取
set_token("填自己的token")
# 示例中为掘金官方仿真服务地址，如接入掘金终端，则填空
# set_endpoint("api.myquant.cn:9000")
set_endpoint("192.168.0.100:7001")
# 登录账户，账户ID由登录并申请仿真账户后，可复制获取；account_alias为账号别名，选填
a1 = account(account_id='bd551230-1f73-11eb-86b9-00163e0a4100', account_alias='')
login(a1)  # 注意，可以输入账户也可以输入账户组成的list
# 获取登录账户的资金，如登录多个账户需要指定账户ID
cash = get_cash()
print(f"get_cash cash={cash}")
# 获取登录账户的持仓，如登录多个账户需要指定账户ID
poses = get_positions()
print(f"get_positions poes={poses}")
# 限价、定量委托买入浦发银行股票 
data = order_volume(symbol='SHSE.600000', volume=10000, side=OrderSide_Buy, order_type=OrderType_Limit, position_effect=PositionEffect_Open, price=11) # 限价单
data= order_volume(symbol='SHSE.600000', volume=10000, side=OrderSide_Buy, order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0) # 市价单
data = order_volume(symbol='SZSE.000009', volume=10000, side=OrderSide_Buy, order_type=OrderType_Limit, position_effect=PositionEffect_Open, price=11)
data = order_volume(symbol='SZSE.000009', volume=10000, side=OrderSide_Buy, order_type=OrderType_Market, position_effect=PositionEffect_Open, price=0) # 市价单
