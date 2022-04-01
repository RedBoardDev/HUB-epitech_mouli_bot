from aiohttp import request


import requests

def check_connected_with_relay():
    try:
        ret =requests.get("http://localhost:4634/epitest/me/2021")
        print(ret)
        return (True)
    except:
        return (False)
