# Sosial Media
Telegram : https://t.me/minsanztuy

# olymptradeapi
Olymptrade API  
Website    : https://autotradevip.com/en/  
Olmyptrade : https://youtu.be/zTZT7zDlmtU  
Binomo     : https://youtu.be/ww9rVMX5TK4  
IQ Option  : https://youtu.be/4i3YUEDRGWY  
Quotex     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  
Expert Option     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA
Alpari     : https://www.youtube.com/channel/UCCqnm8XHUoc0Ude78RJwmoA  

### Import
```python
from olymptradeapi.stable_api import Olymptrade
```
### Get Payment
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
print(account.get_payment())
```
### Get Asset Data
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
print(account.get_asset_data())
```
### Get Name Account
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
print(account.get_name())
```
### Change Account & Get Balance
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
_,r=account.connect()
account.change_balance('PRACTICE') #REAL
balance=account.get_balance()
print(balance)
```
### Change Account V2 & Get Balance
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
_,r=account.connect()
print(account.get_name()) # ['USD Account', 'Demo account', 'Akun IDR 1', 'Akun IDR 2']
account.change_balance_v2('Demo Account') 
balance=account.get_balance()
print(balance)
```
### Buy
![buy](https://user-images.githubusercontent.com/56580637/215087249-27e25540-5436-4c86-abc4-98b424555854.png)
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
_,r=account.connect()
account.change_balance('PRACTICE') #REAL
asset="EURUSD"
amount=12
dir="up"#"down"
pos=0
duration=60#sec
print(account.buy(asset,amount,dir,pos,duration))
```
### Check Win
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
_,r=account.connect()
account.change_balance('PRACTICE') #REAL
asset="EURUSD"
amount=12
dir="up"#"down"
pos=0
duration=60#sec
check,d=account.buy(asset,amount,dir,pos,duration)
order_id=d["id"]
profit=account.check_win(order_id)
print(profit)
 
```
### Get Candle
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
c,r=account.connect()
if c:
    pair="EURUSD"
    size=60
    print(account.get_candle(pair,size))
```
### Get Candle V2
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
c,r=account.connect()
if c:
    pair="EURUSD"
    size=60
    to=int(time.time())
    offset= 3600 - to
    print(account.get_candle_v2(pair,size,offset,to))
```
### Get Candle V2
```python
from olymptradeapi.stable_api import Olymptrade 
account=Olymptrade("email","password",set_ssid="1000869312323232143243243243234432")
c,r=account.connect()
if c:
    pair="EURUSD"
    size=60
    to=int(time.time())
    offset= 3600 - to
    print(account.get_candle_v2(pair,size,offset,to))
```
### REAL TIME CANDLE
```python
from olymptradeapi.stable_api import Olymptrade 
goal="EURUSD"
while True: 
    print(account.start_candles_stream(goal,1))
```
