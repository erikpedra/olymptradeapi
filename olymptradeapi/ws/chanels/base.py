"""Module for base Olymptrade base websocket chanel."""


class Base(object):
    """Class for base Binomo websocket chanel."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`OlymptradeAPI
            <olymptradeapi.api.OlymptradeAPI>`.
        """
        self.api = api

    def send_websocket_request(self, name):
        """Send request to Olymptrade server websocket.
        :param str name: The websocket chanel name.
        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_websocket_request(name)
