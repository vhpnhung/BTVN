spend = float(input("Nhap so tien da mua: "))

print("Tong hoa don:", end = "\t")

if spend < 75:
    print(spend)
elif spend < 100:
    discount = 15
    print(spend - 15)
elif spend >= 150:
    discount = 50
    print(spend - 50)
else:
    discount = 25
    print(spend - 25)