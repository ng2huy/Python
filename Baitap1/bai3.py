# bangdiem = [5, 7, 8]
# tong = 0
# for i in range(3):
#     tong += bangdiem[i]
#     print("Diem mon", i+1, "la:", bangdiem[i])
# print("Tong diem la:", tong)

nv1 = input("Nhap ten nhan vien 1: ")
nv2 = input("Nhap ten nhan vien 2: ")  
nv3 = input("Nhap ten nhan vien 3: ")
luong_nv1 = int(input("Nhap luong nhan vien 1: "))
luong_nv2 = int(input("Nhap luong nhan vien 2: "))
luong_nv3 = int(input("Nhap luong nhan vien 3: "))
cong1 = int(input("Nhap ngay cong nhan vien 1: "))
cong2 = int(input("Nhap ngay cong nhan vien 2: "))   
cong3 = int(input("Nhap ngay cong nhan vien 3: "))

luong = [luong_nv1, luong_nv2, luong_nv3]
ds_nv = [nv1, nv2, nv3]
cong = [cong1, cong2, cong3]    
for i in range(3):
    print("Luong cua ", ds_nv[i], "la:", luong[i] * cong[i])

print("Ket thuc chuong trinh")