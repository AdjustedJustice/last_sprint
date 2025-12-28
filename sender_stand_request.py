from urllib.parse import urljoin
import configuration
import requests


def create_order(order):
    url = urljoin(configuration.SERVICE_URL, configuration.CREATE_ORDER_ENDPOINT)
    return requests.post(url, json=order, timeout=10.0)


def get_order_by_track(track):
    url = urljoin(configuration.SERVICE_URL, configuration.GET_TRACK_ENDPOINT)
    return requests.get(url, params={"t": track}, timeout=10.0)