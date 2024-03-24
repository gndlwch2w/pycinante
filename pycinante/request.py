"""This module provides functionality for request an HTTP or HTTPS request.
"""
import requests
from requests import Response

# Whether enable the proxies when requesting any url
_is_global_proxy = False

def enable_global_proxy():
    _is_global_proxy = True

def disable_global_proxy():
    _is_global_proxy = False

# Global proxies configuration
_global_proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}

def set_global_proxy(protocol: str, url: str) -> None:
    global _global_proxies
    _global_proxies[protocol] = url

def get(url: str, params: dict = None, headers: dict = None, **kwargs) -> Response:
    is_global_proxy = kwargs.pop('enable_proxy', False) or _is_global_proxy
    return requests.get(
        url,
        params=params,
        headers=headers,
        proxies=_global_proxies if is_global_proxy else None)
