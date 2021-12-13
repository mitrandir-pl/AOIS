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

    def check(self, id):
        check_list = [True for i in id[:3].lower() if i in self._dict_of_values.keys()]
        return len(check_list) == 3

    def get_value(self, id):
        value = 0
        range_ = 3 if len(id) >= 3 else len(id)
        for i in id[:range_]:
            value += 33 * self._dict_of_values[i.lower()]
        return value

    def get_hesh(self, V, B):
        return V % 10 + B

    def add_element(self, id, data):
        if self.check(id):
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
            return True
        else:
            print("No such ID:", id)
            return False

    def del_element(self, id):
        if self.check(id):
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
            return True
        else:
            print("No such ID:", id)
            return False


    def search_element(self, id):
        if self.check(id):
            for i in self._hesh_table:
                if i["next"]:
                    temp = i
                    while temp["ID"] != id and temp["next"]:
                        temp = temp["next"]
                    if temp["ID"] == id:
                        print(i["data"])
                elif i["ID"] == id:
                    print(i["data"])
            return True
        else:
            print("No such ID:", id)
            return False

    def print_hesh_table(self):
        print("     ID      \tvalue\t     hesh code         data   ")
        for i in self._hesh_table:
            print(f"{i['ID'].ljust(10)}\t{i['value']}\t\t{i['hesh_code']}\t\t{temp['data'] if len(i['data']) < 20 else i['data'][:20]}...")
            if i["next"]:
                print("------------------------Collisions--------------------------")
                temp = i["next"]
                while temp:
                    print(f"{temp['ID'].ljust(10)}\t{temp['value']}\t\t{temp['hesh_code']}\t\t{temp['data'] if len(temp['data']) < 10 else temp['data'][:10]}")
                    temp = temp["next"]
                print("------------------------------------------------------------")


def main():
    my_hesh_table = HeshTable()
    my_hesh_table.add_element("Ампер", "Единица измерения силы электрического тока в системе СИ")
    my_hesh_table.add_element("Литр", "Единица объёма в метрической системе единиц")
    my_hesh_table.add_element("Молекула", "Наименьшая устойчивая частица данного вещества, обладающая его химическими свойствами")
    my_hesh_table.add_element("Электрон", "Квазичастица в твёрдом теле с зарядом электрона, но с отличной массой")
    my_hesh_table.add_element("Эффект Холла", "Возникновение поперечной разности потенциалов при протекании тока во внешнем магнитное поле")
    my_hesh_table.add_element("Галлий", "Элемент пятой группы периодической системы элементов")
    my_hesh_table.add_element("Валентная зона", "Зона валентных электронов, при нулевой температуре в собственном полупроводнике полностью заполнена")
    my_hesh_table.add_element("Затвор", "Управляющий электрод в полевом транзисторе")
    my_hesh_table.add_element("Сток", "Один из контактов в полевом транзисторе")
    my_hesh_table.add_element("Фотопроводимость", "Проводимость полупроводника при воздействии света. Даёт информацию о дефектах в полупроводниках")
    my_hesh_table.add_element("Волны", "Возмущения (изменение состояния среды или поля), распространяющиеся в пространстве с конечной скоростью")
    my_hesh_table.add_element("Сила тока", "Количественная характеристика электрического тока, определяемая величиной заряда, переносимого через рассматриваемую поверхность в единицу времени: I = dq/dt")
    my_hesh_table.add_element("Молярная масса", "Масса одного моля вещества")
    my_hesh_table.add_element("Кинетическая энергия", "Энергия движущегося тела, равная mv2/2")
    my_hesh_table.add_element("Теплопередача", "Процесс изменения внутренней энергии без совершения работы над телом или самим телом")
    my_hesh_table.add_element("Импульс тела", "Физическая величина, равная произведению массы тела на его скорость")
    my_hesh_table.add_element("Тело отсчета", "Тело, относительно которого наблюдается движение")
    my_hesh_table.add_element("Испарение", "Парообразование со свободной поверхности жидкости при любой температуре")
    my_hesh_table.add_element("Мгновенная скорость", "Векторная величина, характеризующая быстроту перемещения и равная отношению перемещения ко времени, за которое это перемещение произошло, при условии дельта t -> 0")
    my_hesh_table.add_element("Электромагнитная волна", "Взаимосвязанное распространение в пространстве изменяющихся электрического и магнитного поле")
    my_hesh_table.add_element("Закон Гука", "Относительное удлинение прямо пропорционально механическому напряжению")
    my_hesh_table.add_element("Твердые тела", "Агрегатное состояние вещества, характеризующееся стабильностью формы и объема при постоянной температуре")
    my_hesh_table.add_element("Длина волны", "Расстояние, на которое распространяется колебание за время одного периода (Т)")
    my_hesh_table.add_element("Невесомость", "Отсутствие давления на подставку тела, расположенного на ней, или на подвес")
    my_hesh_table.print_hesh_table()
    my_hesh_table.del_element("Теплопередача")
    my_hesh_table.del_element("Волны")
    print(end='\n\n\n')
    my_hesh_table.print_hesh_table()
    print()
    
    my_hesh_table.search_element("Невесомость")


if __name__ == '__main__':
    main()