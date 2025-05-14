# Xây dựng một chương  trình  nhằm nhập số  giờ  làm việc  hàng tuần của nhân viên  và  mức  lương theo giờ  tiêu  chuẩn. Từ đó, thực hiện tính toán số tiền thực nhận của nhân viên. Cần lưu ý rằng số giờ tiêu chuẩn mỗi tuần là 44 giờ, và mỗi giờ làm thêm sẽ được trả 150% so với mức lương theo giờ tiêu chuẩn.
so_gio_lam = float(input('nhap so gio lam moi tuan: '))
luong_gio = float(input('nhap thu la tren moi gio tieu chuan: '))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio + 1.5

print(f'so tien thuc linh cua nv: {thuc_linh}')