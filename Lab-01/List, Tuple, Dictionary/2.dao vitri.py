def dao_vt(list):
    return list[::-1]

nhap = input("nhap ds: ")
nums = list(map(int, nhap.split(',')))

print('ds sau khi dao: ', dao_vt(nums))