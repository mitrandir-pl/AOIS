class HeshTable:
    _hesh_table = []
    _dict_of_values = {
        "а" : 1, "б" : 2, "в" : 3, "г" : 4, "д" : 5,
        "е" : 6, "ё" : 7,  "ж" : 8, "з" : 9, "и" : 10,
        "й" : 11, "к" : 12, "л" : 13, "м" : 14, "н" : 15,
        "о" : 16, "п" : 17, "р" : 18, "с" : 19, "т" : 20,
        "у" : 21, "ф" : 22, "х" : 23, "ц" : 24, "ч" : 25,
        "ш" : 26, "щ" : 27, "ь" : 28, "ъ" : 29, "ы" : 30,
        "э" : 31, "ю" : 32, "я" : 33
    }

    def get_value(self, id):
        value = 0
        range_ = 3 if len(id) >= 3 else len(id)
        for i in id[:range_]:
            value += 33 * self._dict_of_values[i.lower()]
        return value

    def get_hesh(self, V, B):
        return V % 10 + B

    def add_element(self, id, data):
        value = self.get_value(id)
        hesh_value = self.get_hesh(value, len(self._hesh_table))
        simple_add = True
        for i in self._hesh_table:
            if i["hesh_code"] == hesh_value:
                temp = i
                while temp["next"]:
                    temp = temp["next"]
                temp["next"] = {
                    "ID" : id,
                    "value" : value,
                    "hesh_code" : hesh_value,
                    "next" : False,
                    "data" : data
                }
                simple_add = False
        if simple_add:
            self._hesh_table.append({
                "ID" : id,
                "value" : value,
                "hesh_code" : hesh_value,
                "next" : False,
                "data" : data
            })

    def del_element(self, id):
        for i in self._hesh_table:
            if i["next"]:
                if i["ID"] == id:
                    self._hesh_table[self._hesh_table.index(i)] = i["next"]
                    break
                temp = i
                while temp["next"]:
                    if temp["next"]["ID"] == id and temp["next"] == False:
                        temp["next"] = False
                    elif temp["next"]["ID"] == id and temp["next"] != False:
                        temp["next"] = temp["next"]["next"]
                    else:
                        temp = temp["next"]
            elif i["ID"] == id:
                self._hesh_table.remove(i)

    def search_element(self, id):
        for i in self._hesh_table:
            if i["next"]:
                temp = i
                while temp["ID"] != id and temp["next"]:
                    temp = temp["next"]
                if temp["ID"] == id:
                    print(i["data"])
            elif i["ID"] == id:
                print(i["data"])

    def print_hesh_table(self):
        print("     ID      \tvalue\t     hesh code         data   ")
        for i in self._hesh_table:
            print(f"{i['ID'].ljust(10)}\t{i['value']}\t\t{i['hesh_code']}\t\t{i['data']}")
            if i["next"]:
                print("------------------------Collisions--------------------------")
                temp = i["next"]
                while temp:
                    print(f"{temp['ID'].ljust(10)}\t{temp['value']}\t\t{temp['hesh_code']}\t\t{temp['data']}")
                    temp = temp["next"]
                print("------------------------------------------------------------")

def main():
    my_hesh_table = HeshTable()
    # my_hesh_table.add_element("Ампер", "Единица измерения силы электрического тока в системе СИ")
    # my_hesh_table.add_element("Литр", "Единица объёма в метрической системе единиц")
    # my_hesh_table.add_element("Молекула", "Наименьшая устойчивая частица данного вещества, обладающая его химическими свойствами")
    my_hesh_table.add_element("Трепонемы", "Бактерии")
    my_hesh_table.add_element("Рапс", "Растения")
    my_hesh_table.add_element("Аброзавр", "Животные")
    my_hesh_table.add_element("Агроцибе", "Грибы")
    my_hesh_table.add_element("Агами", "Животные")
    my_hesh_table.add_element("Мегавирус", "Вирусы")
    my_hesh_table.add_element("Кешью", "Растения")
    my_hesh_table.add_element("Гигроцибе", "Грибы")
    my_hesh_table.add_element("Зира", "Растения")
    my_hesh_table.add_element("Фаг T4", "Вирусы")
    my_hesh_table.add_element("Адский вампир", "Животные")
    my_hesh_table.add_element("Миовирусы", "Вирусы")
    my_hesh_table.add_element("Гафнии", "Бактерии")
    my_hesh_table.add_element("Вирофаги", "Вирусы")
    my_hesh_table.add_element("Колимовирусы", "Вирусы")
    my_hesh_table.add_element("Айолот", "Животные")
    my_hesh_table.add_element("Лакрица", "Растения")
    my_hesh_table.add_element("Галерина", "Грибы")
    my_hesh_table.add_element("Носток", "Бактерии")
    my_hesh_table.add_element("Блюдцевик", "Грибы")
    my_hesh_table.add_element("Ромашка римская", "Растения")
    my_hesh_table.add_element("Аглии", "Животные")
    my_hesh_table.add_element("Австрораптор", "Животные")
    my_hesh_table.add_element("Спирохеты", "Бактерии")
    my_hesh_table.print_hesh_table()
    my_hesh_table.del_element("Аглии")
    my_hesh_table.del_element("Рапс")
    print(end='\n\n\n')
    my_hesh_table.print_hesh_table()
    print()
    
    my_hesh_table.search_element("Айолот")


if __name__ == '__main__':
    main()