import random
import json
import time
from screeninfo import get_monitors
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def sleep_very_very_short():
    time.sleep(random.choice([0.05, 0.07, 0.08, 0.1, 0.2, 0.5]))

def sleep_very_short():
    time.sleep(random.choice([0.6, 0.7, 0.8, 0.9, 1, 1.5, 1.2]))

def sleep_short():
    time.sleep(random.choice([1, 1.8, 2, 2.1, 2.2]))

def read_txt(path):
    f = open(path, "r", encoding="utf-8")
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    f.close()
    return data

def gen_username_password():
    list_name = ['An','Anh','Ban','Binh','Bich','Bang','Bach','Bao','Bang','Boi','Ca','Cam','Chi','Chinh','Chieu','Chung','Chau','Cat','Cuc','Cuong','Cam','Cam','Dao','Di','Dien','Diem','Diep','Dieu','Du','Dung','Duy','Duyen','Dan','Da','Duong','Da','Gia','Giang','Giao','Giang','Hieu','Hien','Hieu','Hiep','Hoa','Hoan','Hoai','Hoan','Hoang','Hoa','Huyen','Hue','Huynh','Ha','Ham','Han','Hoa','Huong','Huong','Huong','Huong','Ha','Hac','Hanh','Hai','Hao','Hau','Hang','Hoa','Ho','Hong','Hop','Khai','Khanh','Khiet','Khuyen','Khue','Khanh','Khe','Khoi','Khuc','Kha','Khai','Kim','Kiet','Kieu','Ke','Ky','Lam','Lan','Linh','Lien','Lieu','Loan','Ly','Lam','Le','Ly','Lang','Luu','Le','Le','Loc','Loi','Luc','Mai','Mi','Minh','Mien','My','Man','Mau','Moc','Mong','My','Nga','Nghi','Nguyen','Nguyet','Nguyet','Nga','Ngan','Ngon','Ngoc','Nhan','Nhi','Nhien','Nhung','Nhan','Nhan','Nha','Nhon','Nhu','Nhan','Nhat','Nhat','Nuong','Nu','Oanh','Phi','Phong','Phuc','Phuong','Phuoc','Phuong','Phung','Quyen','Quan','Que','Quynh','Sa','San','Sao','Sinh','Song','Song','Son','Suong','Thanh','Thi','Thien','Thieu','Thieu','Thien','Thoa','Thoai','Thu','Thuan','Thuan','Thy','Thai','Theu','Thong','Thuy','Thuy','Tho','Thu','Thuong','Thuong','Thach','Thao','Tham','Thuc','Thuy','Thuy','Tinh','Tien','Tieu','Trang','Tranh','Trinh','Trieu','Trieu','Trung','Tra','Tram','Tran','Truc','Tram','Tuyen','Tuyet','Tuyen','Tue','Ty','Tam','Tung','Tuy','Tu','Tuy','Tuong','Tinh','To','Tu','Uyen','Uyen','Vi','Vinh','Viet','Vy','Vang','Vanh','Van','Vu','Vong','Vy','Xuyen','Xuan','Yen','Yen','xanh','Ai','Anh','An','Y','Dan','Dinh','Doan','Dai','Dao','Dong','Dang','Don','Duc']
    user = random.choice(list_name) + random.choice("._") + random.choice("zxcvbnmasdfghjklqwertyuiop") + random.choice("._") +str(random.choice(range(100,9999)))
    password = "@" + random.choice("ZXCVBNMASDFGHJKLQWERTYUIOP") + user
    return user, password

def write_txt(path, data):
    f = open(path, "w", encoding="utf-8")
    for x in data:
        f.write(x +"\n")
    f.close()
def write_txt_a(path, data):
    with open(path, "a", encoding="utf-8") as f:
        for x in data:
            if x is not None:  # Kiểm tra nếu x không phải là None
                f.write(x + "\n")
        f.close()
# def write_txt_a(path, data):
#     f = open(path, "a", encoding="utf-8")
#     for x in data:
#         f.write(x + "\n")
#     f.close()

def read_json(path):
    f = open(path, "r", encoding="utf-8")
    data = json.loads(f.read())
    return data

def write_json(path, data):
    f = open(path, "w", encoding="utf-8")
    json.dump(data, f)

def get_pos(position):
    for m in get_monitors():
        if m.is_primary == True:
            w = m.width
            h = m.height
            num_x = w//500
            num_y = h//500 + 1
            print("Số trình duyệt tối đa trên một hàng: ", num_x)
            x = position%num_x
            y = (position//num_x) if position//num_x < num_y else (position//num_x)//num_y
            return x*500, y*500
class MyAutomationClass:
    def __init__(self):
        # Khởi tạo WebDriver, ví dụ với Chrome
        self.driver = webdriver.Chrome()  # Đảm bảo đường dẫn tới ChromeDriver đã được thiết lập

    def check_element_exists(self, by_located, timeout):
        try:
            # Kiểm tra sự xuất hiện của phần tử
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_located))
            return True
        except TimeoutException:
            return False