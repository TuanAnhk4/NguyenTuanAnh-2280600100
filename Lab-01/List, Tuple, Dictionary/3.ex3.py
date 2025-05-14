def tao_tuple(list):
    return tuple(list)

nhapds = input("Nhap ds: ")
nums = list(map(int, nhapds.split(',')))

print('list: ', nums)
print('list tuple: ', tao_tuple(nums))