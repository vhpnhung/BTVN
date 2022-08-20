age = int(input("Nhap tuoi: "))

if age >= 20:
    h = float(input("Nhap chieu cao (m): "))
    w = float(input("Nhap can nang (kg): "))
    bmi = w/(h**2)
    if bmi < 16:
        print("Gay III")
    elif bmi < 17:
        print("Gay II")
    elif bmi < 18.5:
        print("Gay I")
    elif bmi < 25:
        print("Binh thuong")
    elif bmi < 30:
        print("Thua can")
    elif bmi < 35:
        print("Beo I")
    elif bmi < 40:
        print("Beo II")
    else:
        print("Beo III")
else:
    print("He thong khong ho tro BMI cho lua tuoi cua ban")
