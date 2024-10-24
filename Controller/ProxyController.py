import requests
import time

class Proxy:
    def __init__(self, proxy_provider, proxy_key) -> None:
        self.proxy_provider = proxy_provider
        self.proxy_key = proxy_key

    def get_new_proxy(self):
        while True:
            if self.proxy_provider == "Tmproxy":
                data = {
                        "api_key": self.proxy_key,
                        "sign": "string",
                        "id_location": 0
                        }
                response = requests.post(url="https://tmproxy.com/api/proxy/get-new-proxy", json=data).json()
                proxy = response["data"]["https"]
                if proxy != "":
                    return proxy
                else:
                    time_wait = int(response['message'].split(" ")[2])
                    if time_wait < 30:
                        time.sleep(time_wait + 1)
                        continue
                    else:
                        proxy = self.get_current_proxy()
                        return proxy
                    
            if self.proxy_provider == "wwproxy":
                pass

            elif self.proxy_provider == "fbproxy":
                pass


    def get_current_proxy(self):
        if self.proxy_provider == "Tmproxy":
            data = {
                        "api_key": self.proxy_key
                        }
            response = requests.post(url="https://tmproxy.com/api/proxy/get-current-proxy", json=data).json()
            proxy = response["data"]["https"]
            return proxy
        

if __name__ == "__main__":
    test = Proxy(proxy_key="325ba307b8964dd066ae517217a73d09", proxy_provider="Tmproxy")
    proxy = test.get_new_proxy()
    print(proxy)
    
