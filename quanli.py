kho = {
    "my pham": {
        "phan": 100,
        "eyeliner": 200
    },
    "gia dung": {
        "noi": 30,
        "may say toc": 9
    },
    "dien thoai": {
        "xiaomi": {
            "note 10": 3000,
            "redmi note 10": 2
        },
        "iphone": {
            "14": 10,
            "14 pro max": 3
        }
    }
}

def xem(catergory):
    if catergory.lower() == "all":
        return kho
    elif catergory in kho:
        return kho[catergory]
    else:
        return "None"

def add(dm, sp, slg):
    if dm.lower() not in kho:
        kho[dm] = {
            sp: slg
        }
    else:
        kho[dm][sp] = slg
    
def edit(dm, cu, moi, slg):
    if dm.lower() not in kho:
        return "Khong co san pham do"
    else:
        if moi.lower() in kho[dm]:
            return "San pham da ton tai"
        if cu.lower() not in kho[dm]:
            return "Khong co san pham do"
        else:
            del kho[dm][cu]
            kho[dm][moi] = slg

def rm(dm, sp):
    if dm.lower() not in kho:
        return "Khong co san pham do"
    elif sp.lower() not in kho[dm]:
        return "Khong co san pham do"
    else:
        del kho[dm][sp]