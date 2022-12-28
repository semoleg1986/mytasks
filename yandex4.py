import re

def unknow(list):
    r = r'[а-яё]*[А-ЯЁ][а-яё]*'
    new_list=[s for s in list if re.fullmatch(r, s) is not None]
    return print(*new_list)
if __name__ == "__main__":
    list = ["Мама","авТо","гриБ",'Яблоко', 'яБлоко', 'ябЛоко', 'яблОко', 'яблоКо', 'яблокО',"агент007","стриж","ГТО","Три богатыря"]
    unknow(list)
