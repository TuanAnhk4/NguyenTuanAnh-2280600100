def demso_lan_xuat_hien(list):
    dem = {}
    for item in list:
        if item in dem:
            dem[item] += 1
        else:
            dem[item] = 1
    return dem

nhapds = input('nhap ds các từ (cách dau cach)')
word_list = nhapds.split()

print('so lan xuat hien cac phan tử: ', demso_lan_xuat_hien(word_list))