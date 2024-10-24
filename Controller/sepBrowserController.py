from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Controller.GologinController import Gologin
import time
import os
from utils import *
import subprocess
class SepBrowser:
    def __init__(self, type_browser, position, api_key, path_folder_profile, id_profile) -> None:
        # Điều khiển trình duyệt nào? ở đâu?
        options = webdriver.ChromeOptions()
        # options.add_argument("--window-size=600,600")
        # options.add_argument("--mute-audio")
        # options.add_argument("--disable-notifications")
        if type_browser == "Gologin":

            g = Gologin(api_key=api_key,
                    path_folder_profile=path_folder_profile,
                    position=position)
            # # Bước 1: Tạo
            # id = g.create_profile()
            # time.sleep(1)
            # # Bước 2: Mở để gologin tự tạo thư mục profile
            # # Bước 3: Copy thư mục vừa tạo về máy mình
            port = g.open_profile(id_profile=id_profile)
            time.sleep(1)

            # # Bước 4: Đóng trình duyệt
            # g.stop_profile(id_profile=id)

            # # Bước 5: Xóa profile trên sever gologin
            # g.delete_profile(id_profile=id)

            # # Bước 6: Mở lại trình duyệt từ đường dẫn profile vừa copy ở port xxx (subprocess)
            # path_profile_id = os.path.join(g.path_folder_profile,id)

            # port = g.re_open_profile(path_profile=path_profile_id )

            options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")

            # Chỉ định phiên bản chromedriver cần chạy

            service = Service(executable_path="./chromedriver/128.exe")

            # Lấy cái gì để điều khiển

            self.driver = webdriver.Chrome(options=options, service=service)

        elif type_browser == "Chrome":
            port = 8000 + int(position) + 5
            path_profile_id = os.path.join(path_folder_profile, id_profile)
            options.add_argument(f"--user-data-dir={path_profile_id}")
            options.add_argument(f"--remote-debugging-port={port}")

            self.driver = webdriver.Chrome(options=options)

        pos = get_pos(position=position)
        self.driver.set_window_size(500,900)
        self.driver.set_window_position(pos[0], pos[1])
    
    def do_click_js(self, by_located, timeout):
        try:
            e = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located))
            self.driver.execute_script("arguments[0].click();", e)
            return True
        except:
            return False

    def do_click(self, by_located, timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located)).click()
            return True
        except:
            return False

    def do_sendkeys(self, by_located, timeout, text):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located)).send_keys(text)
            return True
        except:
            return False
    
    def do_sendkeys_slow(self, by_located, timeout, text):
        try:
            for t in text:
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located)).send_keys(t)
                time.sleep(random.choice([0.01, 0.02, 0.03, 0.04, 0.05, 0.07, 0.2, 0.3, 0.5]))
            return True
        except:
            return False

    def check_text(self, text, timeout):
        for i in range(timeout):
            if text in self.driver.find_element(By.TAG_NAME, "body").text:
                return True
            else:
                time.sleep(1)
        return False
    def check_element_exists(self, by_located, timeout):
        try:
            # Kiểm tra sự xuất hiện của phần tử
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located))
            return True
        except TimeoutException:
            return False