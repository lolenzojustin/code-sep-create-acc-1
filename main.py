from Controller.sepController import Sep
from threading import Thread
import time
from utils import *
from Controller.sepBrowserController import *
# from Controller.sepBrowserController import *
def scripts(pos, id_profile):
    auto = Sep(
                type_browser="Gologin",
                position=pos, 
                api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NjhhMTU0MzNkM2YyMzU0YTllNDg3OTQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NzAzOTlhNDUwYzQzNGFiNTVmODJhZjIifQ.UOqCUQ0MxT2R1qwsw_0ZOdfD1ovsynWixWlSEPJ9myM",
                path_folder_profile=r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data",
                id_profile=id_profile)
    # auto.register()
    # auto.logout()
    
    #     driver.refresh()
    #     time.sleep(1)
    #     auto.logout()
    while True:
        auto.register()
        auto.logout()


list_thread = []
list_profile= ["6703a0f52fbeb790e81e77c4", "6703a0f1b892eaa55c12e404","67140842d67810a0fb6537cc"]
# tại sao ở đây là list_profile và bên sepBrow... dòng 61 cũng có thể chạy
# id_profile= ["Profile 88", "Profile 89"]


for i in range(3):
    # print("Đây là i: ", i)
    # Tạo luồngo
    thread = Thread(target=scripts, args=(i,list_profile[i],))

    list_thread.append(thread)
# for i in range(2):
#     # Tạo luồng
#     thread = Thread(target=scripts, args=(i,))

#     list_thread.append(thread)
for i in range(3):
    # Cho khởi chạy từng luồng
    list_thread[i].start()
    time.sleep(2)

for i in range(3):
    list_thread[i].join()


