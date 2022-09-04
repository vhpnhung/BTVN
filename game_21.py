import random

tong = 0

while tong < 21:
    play_1 = int(input("Nhap mot so 1/2/3: "))
    while play_1 > 3:
        play_1 = int(input("Vui long nhap lai so 1->3: "))
    tong += play_1
    if tong >= 21:
        print(f"Tong la {tong}. Nguoi choi 1 thua")
        break
    
    play_2 = random.randint(1,3)
    print(f"Nguoi choi 2 chon: {play_2}")
    tong += play_2
    if tong >= 21:
        print(f"Tong la {tong}. Nguoi choi 2 thua")
        break