vb = "Hello, My name is Nhung"
tungtu = vb.split()

cidian = dict({})

for i in tungtu:
    if i not in cidian:
        cidian[i] = 1
    else:
        cidian[i] += 1

def dem(zi):
    if zi in cidian:
        return cidian[zi]
    else:
        a = "Khong co"
        return a
        
a = dem("Nhungg")
print(a)