#xoa pt tu dictionary theo key da cho
def xoa_pt(dictionary, key):
    if(key in dictionary):
        del dictionary[key]
        return True
    else:
        return False
    
my_dict = {'a':1, 'b':2,'c':3,'d':4}
key_to_delete = 'b'
kq = xoa_pt(my_dict, key_to_delete)

if kq:
    print('pt da dc xoa: ', my_dict)
else:
    print('ko tim thay pt xoa')
