
from PySide6.QtCore import *
from Controller.sepController import Sep
import time
from utils import *

class ThreadSep(QThread):

    signal_update = Signal(object, object)

    def __init__(self, index_thread, id_profile, type_browser, api_key):
        super(ThreadSep, self).__init__()
        self.index_thread = index_thread
        self.id_profile = id_profile
        self.type_browser = type_browser
        self.api_key = api_key
    def run(self):

        self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", "Đang khởi tạo trình duyệt..."])


        self.auto = Sep(
                type_browser=self.type_browser,
                position=self.index_thread, 
                api_key=self.api_key,
                path_folder_profile=r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data",
                id_profile=self.id_profile)
        success = 0
        # # max_attempts = 10000
        # # while success < max_attempts:
        # #     try:
        # self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", f"Đang tạo acc lần thứ {success + 1}..."])
        #         # Thực hiện đăng ký tài khoản
        # mail = self.auto.register()
                
        #         # Ghi thông tin tài khoản vào file
        # write_txt_a(path=r"C:\Users\Admin\Desktop\code tool\Buổi 567\accs\accs.txt", data=[mail])
                
        #         # Đăng xuất sau khi đăng ký thành công
        # self.auto.logout()
                
        #         # Tăng biến đếm thành công
        #         # success += 1

        #         # except Exception as e:
        #         # # Nếu có lỗi, ghi lại lỗi vào log hoặc in ra màn hình để biết thông tin
        #         # print(f"Lỗi xảy ra: {e}")
        #         # Có thể thêm logic để quyết định dừng vòng lặp hoặc tiếp tục

        #         # Thêm thời gian nghỉ để tránh làm quá tải hệ thống (nếu cần)
        # # time.sleep(0.5)
        # # print("đang thử lại qthread")  # nghỉ 0.5 giây giữa các lần thử
                
        while True:
            self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", f"Đang tạo acc lần thứ {success}..."])
            mail = self.auto.register()
            write_txt_a(path=r"C:\Users\Admin\Desktop\code tool\Buổi 567\accs\accs.txt", data=[mail])
            self.auto.logout()
            success += 1
    
    def stop(self):

        self.signal_update.emit(self.index_thread, [self.index_thread, "xxxx", "Đã dừng!"])

        try:
            self.auto.driver.close()
            self.auto.driver.quit()
        except:
            pass

        self.terminate()