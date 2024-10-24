<!-- Đa luồng -->

- có scripts để chạy mỗi luồng
- có một nơi để chứa đồng thời các luồng

<!-- Lấy danh sách thư viện đã cài -->

- pip freeze > requirments.txt

<!-- Giao diện -->

- pyqt6, pyside6

- pyside6-designer

- pyside6-uic gui.ui -o ui_main.py

- QtThread, Signal, Tabledwidget

<!-- Cách lưu lại config trên giao diện -->

- Mỗi lần nhấn chạy => lưu configs vào file configs.json
- Mỗi lần mở lại => mở file configs.jon => nhét các giá trị cũ vào các widget vừa tạo

<!-- Quy trình fix lỗi -->

- tìm hiểu xem báo lỗi gì
- tìm đến hàng lỗi
- google/chatgbt

<!-- Quy trình luồng -->

Biết index luồng
=> Tạo luồng thứ index đó
=> Luồng đó nhận 4 thông tin (index của luồng, id_profile cần mở, loại trình duyệt, api)
=> Luồng đó sẽ được khởi chạy: - có phương tiện để gửi tín hiệu (tạo bởi class Signal) tên là signal_update - luồng đó sẽ chạy hàm run() + hàm run gửi các tín hiệu bởi signal_update, gửi 2 thứ:
index của luồng để biết dữ liệu cần phải update vào hàng nào
data cần update + khởi tạo class Sep và chạy hàm login

=> Ở giao diện chính (luồng chính) sẽ nhận tín hiệu từ signal_update
=> Tín hiệu nhận được sẽ kết nối đến hàm update_row_table
=> Vì Tín hiệu gửi 2 thứ nên hàm update_row_table cũng nhận 2 thứ
=> Hàm update_row_table nhận được index_row (index luồng) và data cần update

<!-- Để đóng gói ra file exe: -->

pyinstaller -w --collect-data screeninfo --noconsole --distpath ./SepTool --name SepToolV0.1 ui_main.py
