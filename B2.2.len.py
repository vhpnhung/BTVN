def length(chuoi):
    chuoi = chuoi + " "
    stt = 0
    kitu = chuoi[stt]
    while kitu != " ":
        stt += 1
        kitu = chuoi[stt]
    return stt

sokitu = length("74d87f1867gh16gnfhnh")
print("So ki tu:",sokitu)