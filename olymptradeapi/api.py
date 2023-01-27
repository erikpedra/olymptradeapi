"""Module for Olymptrade API."""

class OlymptradeAPI(object):  
    """Class for communication with Olymptrade API."""
    def __init__(self, host, set_ssid, proxies=None):
        """
        :param str host: The hostname or ip address of a Olymptrade server.
        :param str set_ssid: The set_ssid of a Olymptrade server.
        :param dict proxies: (optional) The http request proxies.
        """
        self.https_url = "https://{host}/api".format(host=host)
        self.wss_url = "wss://{host}/echo/websocket".format(host=host)
        self.websocket_client = None
        self.set_ssid = set_ssid
        self.proxies = proxies
