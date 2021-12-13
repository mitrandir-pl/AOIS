from itertools import combinations
from functools import reduce


def gluing(SNF, amount):
    nf = []
    for i in range(len(SNF)):
        summand1 = SNF[i]
        for j in range(i+1, len(SNF)):
            summand2 = SNF[j]
            summand1_check = [i[-1] for i in summand1]
            summand2_check = [i[-1] for i in summand2]
            if summand1_check == summand2_check:
                implicant = []
                for k in summand2:
                    if k in summand1:
                        implicant.append(k)
                if len(implicant) == amount:
                    nf.append(implicant)
    return nf


def calculation_tabular_method(nf, SNF):
    mnf, table, filled_columns, verifiable_implicants = [], [], [], []
    for i in nf:
        table.append([len(set(i) & set(j)) == len(set(i)) for j in SNF])
    filled_columns = [False for _ in range(len(table[0]))]
    for i in range(len(table[0])):
        verifiable_column = [j[i] for j in table]
        if verifiable_column.count(True) == 1:
            implicant = nf[verifiable_column.index(True)]
            if implicant not in mnf:
                mnf.append(implicant) 
            filled_columns = list(map(
                lambda x: x[0] or x[1],
                zip(filled_columns, table[verifiable_column.index(True)])
            ))
    verifiable_implicants = [i for i in nf if i not in mnf]
    if False in filled_columns:
        min_amount = 256
        for amount in range(1, len(verifiable_implicants)+1):
            for subset in combinations(verifiable_implicants, amount):
                set_of_verifiable_implicants = [table[nf.index(i)] for i in subset]
                set_of_verifiable_implicants = reduce(
                    lambda x, y: [i or j for i, j in zip(x, y)],
                    set_of_verifiable_implicants
                )
                if False not in list(map(
                    lambda x: x[0] or x[1],
                    zip(set_of_verifiable_implicants, filled_columns)
                )) and len(set_of_verifiable_implicants) < min_amount:
                    min_amount = len(set_of_verifiable_implicants)
        mnf.extend(subset)
    return mnf


def summator():
    table = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
    for i in range (0,8):
        rezult = table[i][0] + table[i][1] + table[i][2]
        if rezult == 3:
            perenos = 1
            rezult -= 2
        elif rezult == 2:
            perenos = 1
            rezult -= 2
        elif rezult == 1:
            perenos = 0
        elif rezult == 0:
            perenos = 0
        table[i].append(rezult)
        table[i].append(perenos)
    return table


def preobrazovatel():
    table = [
        [0,0,0,0], [0,0,0,1], [0,0,1,0], [0,0,1,1],
        [0,1,0,0], [0,1,0,1], [0,1,1,0], [0,1,1,1],
        [1,0,0,0], [1,0,0,1], [1,0,1,0], [1,0,1,1],
        [1,1,0,0], [1,1,0,1], [1,1,1,0], [1,1,1,1]
    ]
    for i in range(0,16):
        if len(addition([0,1,0,1],table[i])) == 4:
            table[i] += addition([0,1,0,1],table[i])
        else:
            table[i] += ['-','-','-','-']
    return table


def addition(spis1,spis2):
    if len(spis1) == len(spis2):
        dop = 0
        rezult = []
        for i in range(len(spis1)-1,-1,-1):
            temp = spis1[i] + spis2[i] + dop
            if temp == 3:
                dop = 1
                rezult.append(1)
            elif temp == 2:
                dop = 1
                rezult.append(0)
            elif temp == 1:
                dop = 0
                rezult.append(1)
            elif temp == 0:
                dop = 0
                rezult.append(0)
        if dop != 0:
            rezult.append(dop)
        rezult.reverse()
        return rezult


def print_table(table):
    print("[x1,x2,x3,rezult,perenos]")  
    print("\n\n     #     |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8")
    print("----------------------------------------------------------------------------\n", "   x1   ".ljust(10, " "), end="")
    for i in table:
        print(f"|   {i[0]}   ", end="")
    print("\n---------------------------------------------------------------------------\n", "   x2   ".ljust(10, " "), end="")
    for i in table:
        print(f"|   {i[1]}   ", end="")
    print("\n---------------------------------------------------------------------------\n", "   x3   ".ljust(10, " "), end="")
    for i in table:
        print(f"|   {i[2]}   ", end="")
    print("\n---------------------------------------------------------------------------\n", "   f    ".ljust(10, " "), end="")
    for i in table:
        print(f"|   {i[3]}   ", end="")
    print("\n---------------------------------------------------------------------------\n", "   f+1    ".ljust(10, " "), end="")
    for i in table:
        print(f"|   {i[4]}   ", end="")
    print("\n---------------------------------------------------------------------------\n")
    print("3 1-in !\n1 4-in +\n1 3-in +\n4 3-in *\n3 2-in *\n\n")


def print_new_table(table):
    print("\n     #     | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 ")
    print("-------------------------------------------------------------------------------------------\n", "   x1   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[0]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   x2   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[1]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   x3   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[2]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   x4   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[3]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   y1   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[4]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   y2   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[5]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   y3   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[6]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   y4   ".ljust(10, " "), end="")
    for i in table:
        print(f"| {i[7]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n")


def to_SDNF(index, table, key=None):
    SDNF = ""
    for column in table:
        if column[index] == 1:
            SDNF += " + "
            if column[0] == 1:
                SDNF += "a*"
            else:
                SDNF += "!a*"
            if column[1] == 1:
                SDNF += "b*"
            else:
                SDNF += "!b*"
            if column[2] == 1:
                SDNF += "c"
            else:
                SDNF += "!c"
            if key == 4:
                if column[3] == 1:
                    SDNF += "*d"
                else:
                    SDNF += "*!d"
    return SDNF[3:]


def minimization(SDNF_4_variables):
    SDNF_4_variables = [i.split("*") for i in SDNF_4_variables.split(" + ")]
    SDNF_3_variables = gluing(SDNF_4_variables, 3)
    SDNF_2_variables = gluing(SDNF_3_variables, 2)
    SDNF_1_variables = gluing(SDNF_2_variables, 1)
    SDNF_full = SDNF_1_variables + SDNF_2_variables + SDNF_3_variables + SDNF_4_variables
    i = 0
    while i < len(SDNF_full):
        j = i + 1
        while j < len(SDNF_full):
            if len(SDNF_full[i]) == len(set(SDNF_full[i]) & set(SDNF_full[j])):
                SDNF_full.remove(SDNF_full[j])
                j -= 1
            j += 1
        i += 1
    MDNF = calculation_tabular_method(SDNF_full, SDNF_4_variables)
    MDNF.sort(key=lambda x: len(x))
    print_dnf(MDNF)

def print_dnf(dnf):
    dnf_output = ""
    for i in dnf:
        dnf_output += f"{'*'.join(i)} + "
    print(f"MDNF form: {dnf_output[:-3]}")


def main():
    print("Lab 4")
    while 1:
        print("First task - press 1")
        print("Second task - press 2")
        print("To exit - press 0")
        choose = input("Enter choise: ")
        match choose:
            case "1":
                table = summator()
                print_table(table)
                SDNF_out1 =  to_SDNF(3, table)
                print("SDNF form (f):", SDNF_out1)
                SDNF_out1 = [i.split("*") for i in SDNF_out1.split(" + ")]
                DNF_out1 = gluing(SDNF_out1, 2) if len(gluing(SDNF_out1, 2)) > 0 else SDNF_out1
                MDNF_out1 = calculation_tabular_method(DNF_out1, SDNF_out1)
                print_dnf(MDNF_out1)
                SDNF_out2 =  to_SDNF(4, table)
                print("SDNF form (f+1):", SDNF_out2)
                SDNF_out2 = [i.split("*") for i in SDNF_out2.split(" + ")]
                DNF_out2 = gluing(SDNF_out2, 2) if len(gluing(SDNF_out2, 2)) > 0 else SDNF_out1
                MDNF_out2 = calculation_tabular_method(DNF_out2, SDNF_out2)
                print_dnf(MDNF_out2)
            case "2":
                print("\nn = 5")
                table = preobrazovatel()
                print_new_table(table)
                SDNF_y1 = to_SDNF(4, table, 4)
                print("SDNF form (y1):", SDNF_y1)
                minimization(SDNF_y1)
                SDNF_y2 = to_SDNF(5, table, 4)
                print("SDNF form (y2):", SDNF_y2)
                minimization(SDNF_y2)
                SDNF_y3 = to_SDNF(6, table, 4)
                print("SDNF form (y3):", SDNF_y3)
                minimization(SDNF_y3)
                SDNF_y4 = to_SDNF(7, table, 4)
                print("SDNF form (y4):", SDNF_y4)
                minimization(SDNF_y4)
            case "0":
                break
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()