words = {
    "Mobile":"Dien thoai",
    "Computer":"May tinh",
    "Iphone":"Lo",
    "Xiaomi":"Xin"
}
def add_word(word, mean):
    if word not in words:
        words[word] = mean

def find_word(word):
    print(words[word] if word in words else "Khong ton tai")

def del_word(word):
    del words[word]

def display():
    for k, v in words.items():
        print(f"{k} -> {v}")

if __name__ == '__main__':
    #add_word( word: "yellow", mean: "vang")
    add_word(mean="Hinh", word="Picture")
    display()
    print("-"*10)
    del_word(word="Iphone")
    display()
    find_word(word="Xiaomi")