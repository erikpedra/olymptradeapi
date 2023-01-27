"""Module for base Olymptrade http base resource."""


class Resource(object):
    """Class for base Olymptrade API http resource."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api):
        """
        :param api: The instance of :class:`Olymptrade
            <olymptradeapi.api.OlymptradeAPI>`.
        """
        self.api = api

    def send_http_request(self, method, data=None, params=None, headers=None):
        """Send http request to Olymptrade API.
        :param str method: The http request method.
        :param dict data: (optional) The http request data.
        :param dict params: (optional) The http request params.
        :param dict headers: (optional) The http request headers.
        :returns: The instance of :class:`requests.Response`.
        """
        return self.api.send_http_request(self, method, data=data, params=params, headers=headers)
