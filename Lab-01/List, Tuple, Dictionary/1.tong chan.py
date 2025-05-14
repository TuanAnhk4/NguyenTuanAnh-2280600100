def tong_chan(list):
    tong=0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong

nhapds = input("Nhap ds: ")
nums = list(map(int, nhapds.split(',')))

print('tong chan trong list: ', tong_chan(nums))