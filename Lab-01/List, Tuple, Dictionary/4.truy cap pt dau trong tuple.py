def truycap_ptdau(tuple_data):
    ptdau = tuple_data[0]
    ptcuoi = tuple_data[-1]
    return ptdau, ptcuoi

nhapTuple = eval(input('nhap tuple: '))
dau, cuoi = truycap_ptdau(nhapTuple)

print('pt dau: ', dau)
print('pt cuoi: ', cuoi)