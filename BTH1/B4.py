import json

def load_employees():
    with open("Data/em.json", encoding='utf-8') as f:
        return json.load(f)

def add_employees(data, ma_nv, ten_nv):
    em = {
        "ma_nv":ma_nv,
        "ten_nv":ten_nv
    }
    data.append(em)
    with open("Data/em.json", mode="w",encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False, indent=4)

def del_employees(data, id):
    for idx, em in enumerate(data):
        if em["ma_nv"] == id:
            del data[idx]
    with open("Data/em.json",mode="w", encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False, indent=4)

def search_employees(data, kw):
    kq = []
    for em in data:
        if em["ten_nv"].find(kw) >= 0:
            kq.append(em)
    return kq

def search_employees2(data, kw):
    return [em for em in data if em["ten_nv"].find(kw) >= 0]

def display(data):
    for em in data:
        for k, v in em.items():
            if k.__eq__("ma_nv"):
                print(f"Ma nhan vien: {v}")
            elif k.__eq__("ten_nv"):
                print(f"Ten nhan vien: {v}")

if __name__ == '__main__':
    data = load_employees()
    add_employees(data, ma_nv=6,ten_nv="Trinh Gia Phuc")
    del_employees(data, 2)
    display(data)
    print("-"*20)
    kq = search_employees(data, "C")
    display(kq)