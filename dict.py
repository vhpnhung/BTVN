hanyue = {
    "dui bu qi": "xin loi",
    "gen wo lai": "theo toi",
    "lai a": "nao",
    "suan le": "thoi bo di"
}

def search(zi):
    if zi in hanyue:
        print(zi, ":",hanyue[zi])
    else:
        print("Khong co trong tu dien")

search("dui bu ji")
