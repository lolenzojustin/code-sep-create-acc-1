from Controller.sepBrowserController import *
from utils import *
import random
import os
import gspread
# max_retries = 100  # Số lần thử tối đa
# attempt = 0  # Biến đếm số lần thử
# credentials = {
#             "type": "service_account",
#             "project_id": "septoolacc",
#             "private_key_id": "5c40c432dcd04ffe67aac3668d62b0e85c063d2c",
#             "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCUVHG5T2WaqXQj\nyup/AlA1bPTsEPHsjh+Q3rOoCB+2oXFN6xKXx9b60aIJrrUyBBppvl2FUKo1klKK\nXl184QFRMHs1f5aKStg8EbFe4frGuhY7H/Xp2UgECPBy0p7voawijNEDZLHaWWcf\n3gJr53kormy8LhanqHMsWvSBLyEihBmH+lUYSAfaZ5dpAIM3vGmbXEHNU3eX8f5/\nuTmKdU6me3VD0jVQdzpLb7jGqmonhxxhfMyvXF9K3xu/DkM0mjHI2Kom47gJtia5\nCTPdLX2292cLzIR2EjQzSMJIjsmwfNKroV4hUFzVA4d9/TesIJewud/+IucaSw5l\nKqLFlLfTAgMBAAECggEAFCbTeyaYmjDdZiN3mkvD0+OlSWZqnQXDWhjiIDkCU1CO\n+9QCUaaabrcI+aHHsi+Ghck8HBQ/xklxIfqnXtjpfJCb8e0PPw3jX2h+nXJmx0BE\nLEIvqavrBx6jyXsTPAvN6V+84bt4wj5qg+ookA+sO+T+ls5Ne6JSC2ZMA4+rQ8H+\nSDcm1lMr+EGIBWn2iJqif63sM/hjpplWUAVdbSGj8tCOCFmhRclDiQvmdAID1nMC\n8QaztYqWoqCa/x5AlkQL6UaVMFMp05HHHfChM9GdFY6kjnMqh4X4C9l+8CH1nig3\nV3gtRdPbUgjLpxT4Mr6aXdPeF6KgLhyljLJebF+dyQKBgQDPONrPXVvBzaX0DaNK\np8EMk2vBRI+khz0hDfffh+lizQaz8P4L7nB7Mxt3Ui0xeup2v9uoCaThqSkFCTL3\nHTNLLb6v71zU/rFiw2Sj7K6DWQmavc5NSPHqZe6g8aGu7PHHv55wQiI89hnClaJz\nPufRnR3iyl0UKCwWJLHrygsFDQKBgQC3PsKfXQmEBvtiPBd/lU5II2elHqSIp6fo\n71g2C7xbW0bmWXrvbPmgT8oHjP3h4I/XTfOfJNTNpwYFY+zEk7VQAwHepW1GHwgt\nRI5EAGa5OBbaWiw6rvJ4O4stkeZfxn1+4QXUu4/jJjSokjHw0ZUONovNy2kOOKBY\nXsJxCS84XwKBgAT5Q184yWwEaJhL/4BaOGr52ts/rwbu7AuwDyQBWhux+hg1j5Nv\nvKloV59sjIMkhR4mirokyR1VdxOU3fFKdSG3zlzgrOS73DwXnoHEu4eRioZ5SctX\nFd9fZPPd+Nh+/Wqi8cWWAMZfzcx61PRZLS09zSrVWpiSQkShytdy+QK9AoGBAKYG\n7CmeD0gbV1rrHVNQgQvlYDwAJo1WclEfwqm9Olz/t55vxm32K7pvcJokyccFQu6N\nx0UTBuiKA2+Q2O5G8olbIC+NbROSfEMfkVLVlj0NL8+I0fgdmL0NHg4c2kE+w2fZ\nFAJqKnVhoWZ2h18tVUL6cvLz8Oycq9NFkCEAdFM7AoGAFVa03UjgIzuO6gZ6oyeP\nCuW6JByu3rEEaNNIb2Al/l3jeHXrxHKcVuxtrsbCsSelQ+lgjjM44MhdBUotfZgy\n89dQ8atchhU1k70wkVk0qHz9TWEWlfn2qcpvADpE4TA6EPS8PHiha/V6P+ZEwyfj\na5+QW5pqIqP26zmGOm4mC+Q=\n-----END PRIVATE KEY-----\n",
#             "client_email": "septoolacc@septoolacc.iam.gserviceaccount.com",
#             "client_id": "107253161766531622071",
#             "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#             "token_uri": "https://oauth2.googleapis.com/token",
#             "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#             "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/septoolacc%40septoolacc.iam.gserviceaccount.com",
#             "universe_domain": "googleapis.com"
#             }
class Sep(SepBrowser):
    def __init__(self, type_browser, position, api_key, path_folder_profile, id_profile) -> None:
        super().__init__(type_browser = type_browser, position=position, api_key=api_key, path_folder_profile=path_folder_profile, id_profile=id_profile)

        # self.do_click(by_located=(By.XPATH,"//button[@data-at='hihi']"), timeout=99999)
    def append_row (self,ggsheet_name, tab_name, row_value):
        gs = gspread.service_account_from_dict(credentials)
        sheet = gs.open(ggsheet_name)
        worksheet = sheet.worksheet(tab_name)
        worksheet.append_row(row_value, table_range="A1:B1")
    
    def register(self):

        list_number = ['1','2','3','4','5','6','7','8','9','0']
        random_phone = (random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number)+ random.choice(list_number))
        list_day = ['1','2','3','4','5', '6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
        random_day = (random.choice(list_day))
        random_email = (
            random.choice(list_number)
            + random.choice(list_number)
            + random.choice(list_number)
            + random.choice(list_number)
            + "at11sep@lolenzo.top"
        )
        # self.driver.get("https://www.sephora.com/ca/en/")
        # time.sleep(2000)
        self.driver.get("https://www.sephora.com/profile/MyAccount/Orders")

        # time.sleep(2)
        # self.driver.refresh()
        # sleep_very_short()
        # self.driver.refresh()
        # while self.check_text(text="Access Denied", timeout=5):
        #     self.driver.refresh()
        #     time.sleep(2)
        # self.driver.refresh()
        # time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        # self.do_click(by_located=(By.XPATH,"//button[@data-comp='Icon StyledComponent']"), timeout=100)
        # self.do_click(by_located= (By.XPATH,"//button[@type = 'button']"), timeout= 100 )
        while self.do_click(by_located=(By.XPATH,"//button[@data-at='create_account_button']"), timeout=3) == False:
            time.sleep(3)
            print("bấm tạo tk")
        # time.sleep(1)
        # self.do_sendkeys(by_located=(By.XPATH,"//input[@autocomplete = 'email']"), timeout=100, text="sdasdasdsa@lolenzo.top")
        while self.do_sendkeys_slow(by_located=(By.ID, "email"), timeout=1000, text=random_email) == False:
            time.sleep(3)
        print("đã send mail ", random_email)
        # self.do_sendkeys_slow(by_located=(By.CLASS_NAME, "css-290f3n"), timeout=100, text=random_email)
        # self.do_sendkeys_slow(by_located=(By.ID, "email"), timeout=100, text=random_email)
        # sleep_very_short()
        # if self.check_text(text="Continue", timeout=100):
        #     self.do_click(by_located=(By.XPATH,"//button[@type = 'submit']"), timeout= 10 )
        #     self.do_click(by_located=(By.XPATH,"//button[@class = 'css-1eg024x eanm77i0']"), timeout= 100 )
        while self.do_click(by_located=(By.XPATH,"//button[@type = 'submit' and text()='Continue']"), timeout= 3 ) == False:
            time.sleep(3)
        # sleep_short()
        # self.do_click(by_located=(By.XPATH,"//button[@class = 'css-1eg024x eanm77i0']"), timeout= 100 )
        # if self.check_text(text="Create An Account", timeout=100):
        if self.check_element_exists(by_located=(By.ID, "firstName"), timeout=3):  
            print ("đã check đc element first name")
        while self.do_sendkeys_slow(by_located=(By.ID, "firstName"), timeout=10, text="sep") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "lastName"), timeout=10, text=random_day) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "register_password"), timeout=10, text="Thang@123") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "mobilePhone"), timeout=10, text=random_phone) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "zipCode"), timeout=10, text="V8W 2J8") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "biRegMonth"), timeout=10, text="o") == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_sendkeys_slow(by_located=(By.ID, "biRegDay"), timeout=10, text=random_day) == False:
            time.sleep(3)
        # sleep_very_short()
        while self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3) == False:
            time.sleep(3)
        # sleep_very_short()
        # self.do_click(by_located=(By.XPATH,"//select[@class='css-lbyitw Checkbox-box']"), timeout=3)
        while self.do_click(by_located=(By.XPATH,"//button[@data-at='join_now']"), timeout=3) == False:
            time.sleep(3)
        # self.driver.quit
           
        #    self.do_sendkeys(by_located=(By.ID, "firstName"), timeout=10, text="sep") 
        #    self.do_sendkeys(by_located=(By.ID, "lastName"), timeout=10, text="12312321") 
        #    self.do_sendkeys(by_located=(By.ID, "register_password"), timeout=10, text="Thang@1234") 
        #    self.do_sendkeys(by_located=(By.ID, "mobilePhone"), timeout=10, text="7788829648") 
        #    self.do_sendkeys(by_located=(By.ID, "zipCode"), timeout=10, text="V5W 2X9")
        #    self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3)
        #    self.do_sendkeys(by_located=(By.ID, "biRegMonth"), timeout=10, text="aa")
        #    self.do_click(by_located=(By.XPATH,"//select[@name='biRegMonth']"), timeout=3)
        #    self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3)
        #    self.do_sendkeys(by_located=(By.ID, "biRegDay"), timeout=10, text="5")
        #    self.do_click(by_located=(By.XPATH,"//select[@name='biRegDay']"), timeout=3) 
        #    self.do_click(by_located=(By.XPATH,"//button[@data-at='join_now']"), timeout=3)
        self.append_row(ggsheet_name="DataSep", tab_name="Tab1", row_value=[random_email])
        # if self.check_text(text="Looks like you are trying to access", timeout=6):
        #     print("đang check text Looks like you are trying to access lần 1 ")
        #     while self.do_click(by_located=(By.XPATH,"//button[@data-at='modal_close']"), timeout=2) == False:
        #         time.sleep(2)
        # Kiểm tra xem có text "Chọn tất cả" hay không để thay đổi giá trị timeout
        # Danh sách các từ cần kiểm tra
# Kiểm tra xem có phần tử với id "recaptcha-audio-button" hay không
        timeout_value = 6  # Mặc định timeout là 6

# Kiểm tra sự tồn tại của phần tử có id = "recaptcha-audio-button"
        if self.check_element_exists(by_located=(By.ID, "recaptcha-verify-button"), timeout=3):  
            timeout_value = 30  # Nếu tồn tại, đặt timeout = 100
            print ("time = 30")

# Sử dụng giá trị timeout đã chọn trong phần tiếp theo
        if self.check_text(text="Looks like you are trying to access", timeout=timeout_value):
            print("time = 6 ")
            while not self.do_click(by_located=(By.XPATH, "//button[@data-at='modal_close']"), timeout=2):
                time.sleep(2)
    def logout(self):
        # max_retries = 12  # Số lần thử tối đa
        # attempt = 0  # Biến đếm số lần thử
        # time.sleep(1)
        # while attempt < max_retries:
        #     try:
        # # Thử nhấn nút
        #         if self.do_click(by_located=(By.XPATH, "//button[@data-at='account_btn']"), timeout=3):
        #             print("Đăng xuất thành công.")
        #             break  # Thoát khỏi vòng lặp nếu thành công
        #         else:
        #             print("Không thể nhấn nút, thử lại...")
        #     except Exception as e:
        # # Ghi lại lỗi nếu có
        #         print(f"Lỗi khi thực hiện do_click: {e}") 
        while self.do_click(by_located=(By.XPATH,"//button[@data-at='account_btn']"), timeout=3) == False:
            time.sleep(2)
            print("Thử logout tiếp ...")
        time.sleep(1)
        while self.do_click_js(by_located=(By.XPATH,"//button[@data-at='sign_out_button']"), timeout=3) == False:
            time.sleep(2)
            print("bấm logout")
        time.sleep(3)
    # def logout(self):
    #     max_retries = 10  # Số lần thử tối đa
    #     attempt = 0  # Biến đếm số lần thử
    #     while attempt < max_retries:
    #         try:
    #     # Thử nhấn nút
    #             if self.do_click(by_located=(By.XPATH, "//button[@data-at='account_btn']"), timeout=3):
    #                 print("Đăng xuất thành công.")
    #                 break  # Thoát khỏi vòng lặp nếu thành công
    #             else:
    #                 print("Không thể nhấn nút, thử lại...")
    #         except Exception as e:
    #     # Ghi lại lỗi nếu có
    #             print(f"Lỗi khi thực hiện do_click: {e}")

    # # Tăng biến đếm số lần thử và đợi trước khi thử lại
    #         attempt += 1
    #         time.sleep(3)
    #         print("Thử logout tiếp...")

    #     if attempt == max_retries:
    #         print("Đã đạt đến số lần thử tối đa, dừng lại.")
    #         return
           # Đặt lại biến đếm cho bước tiếp theo
        # attempt = 0
        # while attempt < max_retries:
        #     try:
        #         if self.do_click_js(by_located=(By.XPATH, "//button[@data-at='sign_out_button']"), timeout=None):
        #             print("Nhấn nút sign out thành công.")
        #             break  # Thoát khỏi vòng lặp nếu thành công
        #         else:
        #             print("Không thể nhấn nút sign out, thử lại...")
        #     except Exception as e:
        #         print(f"Lỗi khi thực hiện nhấn nút sign out: {e}")

        # # Tăng biến đếm số lần thử và đợi trước khi thử lại
        # attempt += 1
        # time.sleep(3)
        # print("Thử nhấn nút sign out tiếp...")

        # if attempt == max_retries:
        #     print("Đã đạt đến số lần thử tối đa cho nút sign out, dừng lại.")
        #     return
    # # def logout(self):
    # #     while self.do_click_js(by_located=(By.XPATH,"//button[@data-at='account_btn']"), timeout=1000) == False:
    # #         time.sleep(3)
    # #         print("Thử logout tiếp ...")
       

