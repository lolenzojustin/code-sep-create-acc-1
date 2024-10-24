# Tạo profile trên app gologin => copy thư mục profile về máy => xóa profile trên app đi

import requests
import time
import shutil
import os
import subprocess

BASE_URL = "https://api.gologin.com"

class Gologin:
    def __init__(self, api_key, path_folder_profile, position) -> None:
        self.api_key = api_key
        self.path_folder_profile = path_folder_profile
        self.position = position

    def create_profile(self):
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }
        new_fingerprint = self.get_new_fingerprint()
        while True:
            try:
                response_create_profile = requests.post(url= BASE_URL + "/browser", headers=headers, json=new_fingerprint, timeout=100).json()
                id_profile = response_create_profile['id']
                return id_profile
            except:
                time.sleep(1)
    
    def open_profile(self, id_profile):
        data = {"profileId": id_profile,
                "sync": True}

        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url= "http://localhost:36912/browser/start-profile", json= data, headers=headers).json()

        print("response khi mở: ", response)

        port = response['wsUrl'].split("127.0.0.1:")[-1].split("/")[0]

        time.sleep(1)

        path_profile_old = os.path.join(r"C:\Users\Admin\AppData\Local\Temp\GoLogin\profiles", id_profile)
        path_profile_new = os.path.join(self.path_folder_profile, id_profile)
        try:
            shutil.copytree(path_profile_old, 
                            path_profile_new,
                            dirs_exist_ok=True)
        except:
            pass
        return port
    
    def stop_profile(self, id_profile):
        data = {"profileId": id_profile}

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(url= "http://localhost:36912/browser/stop-profile", json= data, headers=headers)

    def re_open_profile(self, path_profile):
        port = 8000 + int(self.position)
        parameters = [
                    r"C:\Users\Admin\.gologin\browser\orbita-browser-128\chrome.exe",
                    "--lang=vi-VN",
                    "--disable-encryption",
                    "--donut-pie=undefined --webrtc-ip-handling-policy=default_public_interface_only --font-masking-mode=2",
                    " --restore-last-session",
                    f"--user-data-dir={path_profile}",
                    "--flag-switches-begin --flag-switches-end",
                    f"--remote-debugging-port={port}"
                    ]
        subprocess.Popen(parameters)
        return port

    
    def delete_profile(self, id_profile):
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }
        requests.delete(url= BASE_URL + f"/browser/{id_profile}", headers=headers)

    def get_new_fingerprint(self):
        headers = {
            'Authorization': f"Bearer {self.api_key}",
            'Content-Type': 'application/json'
        }

        # Lấy vân tay mới
        fingerprint = requests.get(url= BASE_URL + "/browser/fingerprint?os=win", headers=headers, timeout=100).json()

        navigator_new = fingerprint['navigator']
        navigator_new['userAgent'] = navigator_new['userAgent'].replace("129", "128")

        # Tạo profile mới từ vân tay vừa lấy
        data = {
                "name": "test",
                "browserType": "chrome",
                "os": "win",
                "startUrl": "https://www.google.com/",
                "debugMode": True,
                "navigator": navigator_new,
                "proxy": {
                    "mode": "none",
                    "host": "string",
                    "port": 0,
                    "username": "string",
                    "password": "string"
                },
                "timezone": {
                    "enabled": True,
                    "fillBasedOnIp": True,
                    "timezone": ""
                },
                "audioContext": {
                    "mode": "noise"
                },
                "canvas": {
                    "mode": "noise"
                },
                "fonts": {
                    "families": [
                        "string"
                    ],
                    "enableMasking": True,
                    "enableDomRect": True
                },
                "mediaDevices": fingerprint['mediaDevices'],
                "webRTC": {
                    "mode": "alerted",
                    "enabled": True,
                    "customize": True,
                    "localIpMasking": False,
                    "fillBasedOnIp": True
                },
                "webGL": {
                    "mode": "noise"
                },
                "clientRects": {
                    "mode": "noise"
                },
                "webGLMetadata": {
                    "mode": "mask",
                    "vendor": fingerprint['webGLMetadata']['vendor'],
                    "renderer": fingerprint['webGLMetadata']['renderer']
                },
                "webglParams": fingerprint['webglParams'],
            }
        return data



if __name__ == "__main__":
    g = Gologin(api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjhhMTU0MzNkM2YyMzU0YTllNDg3OTQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NzAzOTlhNDUwYzQzNGFiNTVmODJhZjIifQ.UOqCUQ0MxT2R1qwsw_0ZOdfD1ovsynWixWlSEPJ9myM",
                path_folder_profile=r"C:\Users\Admin\Desktop\code tool\Buổi 4\profile",
                position=1)
    g.open_profile(id_profile="67039774eeb4c49553d84936")