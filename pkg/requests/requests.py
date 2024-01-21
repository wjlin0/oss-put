import requests
requests.packages.urllib3.disable_warnings()



class Requests:
    def __init__(self, proxy=None):
        self.proxy = proxy

    def get(self, url, **kwargs):
        return requests.get(url=url, proxies=self.proxy, verify=False, **kwargs)

    def post(self, url, **kwargs):
        return requests.post(url=url, proxies=self.proxy, verify=False, **kwargs)

    def put(self, url, **kwargs):
        return requests.put(url=url, proxies=self.proxy, verify=False, **kwargs)
