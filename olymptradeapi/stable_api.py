from alpariapi.api import alpariapi
from alpariapi.constants import constants as OP_code
from alpariapi.global_value import global_value
from datetime import datetime, timedelta
from collections import defaultdict
from collections import deque
import collections
import json
import threading
import requests
import urllib
import requests
import base64
import json
from urllib.parse import urlparse, parse_qs

class Alpari:
    __version__ = '0.4'
    def __init__(self, set_ssid, user_agent, proxies, auto_logout):
      self.SESSION_HEADER = { }
      self.stop_time = 0.5
      self.SESSION_COOKIE = { }
      self.proxies = proxies
      self.set_ssid = set_ssid
      self.auto_logout = auto_logout
      self._2FA_TOKEN = None
      self.server_timestamp = None
      self.websocket_candle_thread = { }
      self.user_agent = user_agent
      
    def report(self, limit, offset, polling = (1,)):
      pass
    
    def option_history(self, option_id):
      pass
    
    def get_account_data(self):
      pass
    
    def get_raw_asset(self):
      pass
    
    def get_profile(self):
      pass
    
    def get_dictionary_data(self):
      pass
    
    def _subscribe_trade_settings(self):
      pass
    
    def get_payment_asnyc(self):
      pass
    
    def buy(self, asset, amount, direction, option_type, time_frame):
      pass
    
    def buy_raw(self, win_percent, loss_percent, parity_percent, amount, asset_id, direction_id, option_type_id, time_frame):
      pass
    
    def check_win(self, order_id):
      pass
    
    def get_balance(self):
      _account_data = self.get_account_data()
      return _account_data['body']['equity']
      
    def get_candle(self, asset, bar_size, limit):
      pass
    
    def start_candles_stream(self, asset, bar_size):
      pass
    
    def get_realtime_candles(self, sid):
      pass
    
    def get_payment():
      pass
    
    def get_server_time():
      if self.server_timestamp == None:
            time.sleep(0.1)
            if not self.server_timestamp == None:
                return self.server_timestamp
    
    def stop_candles_stream(self, sid):
      pass
    

    def connect(self):
      pass
    
 
       
