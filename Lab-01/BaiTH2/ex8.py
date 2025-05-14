def chia_het_cho_5(so_np):
    so_tp = int(so_np, 2)
    if so_tp % 5 == 0:
        return True
    else:
        return False
    
chuoi_so = input('nhap chuoi so nhi phan')

so_np_list = chuoi_so.split(',')
chia_het_cho_5 = [so for so in so_np_list if chia_het_cho_5(so)]

if len(chia_het_cho_5) > 0:
    kq = ','.join(chia_het_cho_5)
    print('cac so nhi phan chia het cho 5 la: ', kq)
else:
    print("ko co so nao")