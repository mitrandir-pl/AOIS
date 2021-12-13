DEFAULT_TABLE_RAW = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

class AsocMemory:
    __table = []
    __buff = []
    __buff_for_search = []
    __size = 16
    __converter = 3

    def __addition(self, first, second):
        res = []
        trans = False
        for i in range(len(first), 0, -1):
            if first[i-1] == 0 and second[i-1] == 0 and trans == False:
                res.insert(0, 0)
                trans = False
            elif first[i-1] == 0 and second[i-1] == 0 and trans == True:
                res.insert(0, 1)
                trans = False
            elif first[i-1] == 1 and second[i-1] == 0 and trans == False:
                res.insert(0, 1)
                trans = False
            elif first[i-1] == 1 and second[i-1] == 0 and trans == True:
                res.insert(0, 0)
                trans = True
            elif first[i-1] == 0 and second[i-1] == 1 and trans == False:
                res.insert(0, 1)
                trans = False
            elif first[i-1] == 0 and second[i-1] == 1 and trans == True:
                res.insert(0, 0)
                trans = True
            elif first[i-1] == 1 and second[i-1] == 1 and trans == False:
                res.insert(0, 0)
                trans = True
            elif first[i-1] == 1 and second[i-1] == 1 and trans == True:
                res.insert(0, 1)
                trans = True
        return res
            

    def __init__(self):
        for _ in range(self.__size):
            self.__table.append(DEFAULT_TABLE_RAW.copy())
            self.__buff.append(DEFAULT_TABLE_RAW.copy())

    def print_table(self):
        print(" \tASSOCIATIVE	MEMORY")
        print("\t____________________")
        for i in self.__table:
            print(f"\t| ", end="")
            for j in i:
                print(j, end="")
            print(f" |")
        print("\t____________________")

    def matching_case(self, wrd):
        best_matches = []
        best_match_num = []
        best_match_discharge = 0
        current_best_mutch_discharge = int()
        word = []
        for i in range(len(wrd)):
            if wrd[i] == "1":
                word.append(1)
            else:
                word.append(0)
        if word in self.__buff_for_search:
            for index, i in enumerate(self.__buff_for_search):
                if word == i:
                    print(f"[{index}] ", end="")
                    for j in i:
                        print(j, end="")
                    print()
                    return

        for each_word in range(len(self.__table)):
            if word != self.__table[each_word]:
                current_best_mutch_discharge = 0
                for each_letter in range(len(word)):
                    if word[each_letter] != self.__table[each_word][each_letter]:
                        current_best_mutch_discharge = each_letter + 1
                    else:
                        each_letter = len(self.__table[each_word]) + 1
                if current_best_mutch_discharge > best_match_discharge:
                    best_match_discharge = current_best_mutch_discharge
                    best_match_num = []
                    best_matches = []
                    best_match_num.append(each_word)
                    best_matches.append(self.__table[each_word])
                elif current_best_mutch_discharge == best_match_discharge:
                    best_match_num.append(each_word)
                    best_matches.append(self.__table[each_word])
        for i in range(len(best_matches)):
            print(f"[{best_match_num[i]}]", end="")
            for j in range(len(best_matches[i])):
                if best_match_discharge == 0:
                    print(best_matches[i][j])
                else:
                    print(word[j])
            break

    def add_element(self, word):
        bool_word = []
        # for i in range(len(word)):
        #     bool_word.insert(0, 0)
        for i in range(self.__size - len(word), self.__size):
            if bool(int(word[i - self.__size + len(word)])):
                bool_word.insert(i, 1)
            else:
                bool_word.insert(i, 0)
        self.__buff.insert(0, bool_word)
        self.__buff.pop(len(self.__buff)-1)
        self.__table = []
        self.__buff_for_search.append(bool_word)
        for _ in range(self.__size):
            self.__table.append(DEFAULT_TABLE_RAW.copy())
        offset = 0
        for i in range(self.__size):
            i_ = 0 - offset
            if i_ < 0:
                i_ += self.__size
            else:
                i_ = i
            for j in range(self.__size):
                self.__table[j][i] = self.__buff[i_][j]
                i_+=1
                if i_ > 15:
                    i_ = 0
            offset += 1
    
    def F0_ana_F15(self, i, j):
        one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        zero = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        res = []
        str_res= ""
        res = self.__addition(one, zero)
        for i in range(len(res)):
            str_res += str(res[i])
        self.add_element(str_res)
        

    def ariphmetics(self):
        for i in range(self.__size):
            if int(self.__table[i][0]) + int(self.__table[i][1]) + int(self.__table[i][2]) < 3:
                A = []
                A.append(self.__table[i][0])
                A.append(self.__table[i][1])
                A.append(self.__table[i][2])
                A.append(self.__table[i][3])
                B = []
                B.append(self.__table[i][4])
                B.append(self.__table[i][5])
                B.append(self.__table[i][6])
                B.append(self.__table[i][7])
                S = self.__addition(A, B)
                for _ in range(0, 5-len(S)):
                    S.append(0)
                new_list = []
                for j in range(self.__converter):
                    new_list.append(self.__table[i][j])
                for j in range(self.__converter+1):
                    new_list.append(A[j])
                for j in range(self.__converter+1):
                    new_list.append(B[j])
                for j in range(self.__converter+2):
                    new_list.append(S[j])
                self.__table[i] = new_list


def main():
    table = AsocMemory()
    table.print_table()
    table.add_element("1111111111111111")
    table.print_table()
    table.add_element("1010101011010101")
    table.print_table()
    table.ariphmetics()
    table.print_table()
    table.matching_case("1111111111111111")
    table.F0_ana_F15(0,1)
    table.print_table()


if __name__ == "__main__":
    main()