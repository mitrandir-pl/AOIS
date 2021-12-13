from copy import deepcopy
from itertools import combinations
from functools import reduce


def init_table():
    table = []
    machine_input = [i%2 for i in range(16)]
    trigger_input,trigger_output, excitation_table = [], [], []
    for index, i in enumerate(machine_input):
        if index == 0:
            trigger_input.append([0,0,0])
            trigger_output.append([0,0,0])
            excitation_table.append([0,0,0])
        elif i == 0:
            trigger_input.append(trigger_output[index-1])
            trigger_output.append(trigger_input[index])
            excitation_table.append([0,0,0])
        elif i == 1:
            trigger_input.append(trigger_input[index-1])
            trigger_output.append(addition(trigger_input[index], [0,0,1]))
            excitation_table.append([int(first_signal != second_signal) for first_signal, second_signal in zip(trigger_input[index], trigger_output[index])])
    table.append(trigger_input)
    table.append(machine_input)
    table.append(trigger_output)
    table.append(excitation_table)
    return table


def addition(summand1, summand2):
    summand1 = deepcopy(summand1)
    summand2 = deepcopy(summand2)
    sum_value = []
    summand1.reverse()
    summand2.reverse()
    remnant = 0
    for i in range(len(summand2)):
        sum_in_place = summand1[i] + summand2[i] + remnant
        if sum_in_place == 0:
            sum_value.insert(0,0)
            remnant = 0
        elif sum_in_place == 1:
            sum_value.insert(0,1)
            remnant = 0
        elif sum_in_place == 2:
            sum_value.insert(0,0)
            remnant = 1
        elif sum_in_place == 3:
            sum_value.insert(0,1)
            remnant = 1
    return sum_value


def print_table(table):
    print("\n     #     | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 ")
    print("-------------------------------------------------------------------------------------------\n", "   q1*   ".ljust(10, " "), end="")
    for i in table[0]:
        print(f"| {i[0]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   q2*   ".ljust(10, " "), end="")
    for i in table[0]:
        print(f"| {i[1]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   q3*   ".ljust(10, " "), end="")
    for i in table[0]:
        print(f"| {i[2]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   V   ".ljust(10, " "), end="")
    for i in table[1]:
        print(f"| {i }  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   q1   ".ljust(10, " "), end="")
    for i in table[2]:
        print(f"| {i[0]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   q2   ".ljust(10, " "), end="")
    for i in table[2]:
        print(f"| {i[1]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   q3   ".ljust(10, " "), end="")
    for i in table[2]:
        print(f"| {i[2]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   h1   ".ljust(10, " "), end="")
    for i in table[3]:
        print(f"| {i[0]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   h2   ".ljust(10, " "), end="")
    for i in table[3]:
        print(f"| {i[1]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n", "   h3   ".ljust(10, " "), end="")
    for i in table[3]:
        print(f"| {i[2]}  ", end="")
    print("\n-------------------------------------------------------------------------------------------\n")
    

def to_SDNF(index, table):
    new_table = []
    for trigger_input_value, machine_input_value in zip(table[0], table[1]):
        new_table.append([i for i in trigger_input_value] + [machine_input_value])
    SDNF = ""
    for count, column in enumerate(new_table):
        if table[3][count][index] == 1:
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
            if column[3] == 1:
                SDNF += "*d"
            else:
                SDNF += "*!d"
    return SDNF[3:]


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


def calculation_tabular_method(nf, SNF, key=None):
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
    MDNF = calculation_tabular_method(SDNF_full, SDNF_4_variables, "sdnf")
    MDNF.sort(key=lambda x: len(x))
    dnf_output = ""
    for i in MDNF:
        dnf_output += f"{'*'.join(i)} + "
    return dnf_output[:-3]


def main():
    table = init_table()
    print_table(table)
    print("a = q1*, b = q2*, c = q3*, d = V")   
    SDNF_h1 = to_SDNF(0, table)
    print("SDNF (h1)", SDNF_h1)
    print("MDNF (h1)", minimization(SDNF_h1))
    SDNF_h2 = to_SDNF(1, table)
    print("SDNF (h2)", SDNF_h2)
    print("MDNF (h2)", minimization(SDNF_h2))
    SDNF_h3 = to_SDNF(2, table)
    print("SDNF (h3)", SDNF_h3)
    print("MDNF (h3)", minimization(SDNF_h3))


if __name__ == '__main__':
    main()