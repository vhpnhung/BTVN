begin_no = int(input("Nhap so bat dau: "))
end_no = int(input("Nhap so ket thuc: "))

while end_no <= begin_no:
    end_no = int(input("Nhap lai so ket thuc: "))

for so in range(begin_no, (end_no + 1)):
    if so%15 == 0:
        print("Fizz-Bizz", end = " ")
        continue
    if so%3 == 0:
        print("Fizz", end = " ")
    if so%5 == 0:
        print("Bizz", end = " ")
    if so%3 != 0 and so%5 != 0:
        print(so, end = " ")
    