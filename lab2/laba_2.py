class LogicFunction:
    sdnf = ""
    sknf = ""
    bin_num_sdnf = ""
    bin_num_sknf = ""
    num_sdnf = ""
    num_sknf = ""
    index_form = 0
    table = (
        {"x1" : 0, "x2" : 0, "x3" : 0, "f" : None},
        {"x1" : 0, "x2" : 0, "x3" : 1, "f" : None},
        {"x1" : 0, "x2" : 1, "x3" : 0, "f" : None},
        {"x1" : 0, "x2" : 1, "x3" : 1, "f" : None},
        {"x1" : 1, "x2" : 0, "x3" : 0, "f" : None},
        {"x1" : 1, "x2" : 0, "x3" : 1, "f" : None},
        {"x1" : 1, "x2" : 1, "x3" : 0, "f" : None},
        {"x1" : 1, "x2" : 1, "x3" : 1, "f" : None},
    )
    priority = {
        "!" : 4,
        "*" : 3,
        "+" : 2,
        "(" : 1,
    }
    ops = {
        "!": (lambda a: not a),
        "+": (lambda a, b: a | b),
        "*": (lambda a, b: a & b),
        "a": 0,
        "b": 1,
        "c": 2,
    }

    def counting(self, expression, values):
        stack = []
        for token in expression:
            match token:
                case "!":
                    arg = self.ops[token](stack.pop())
                    stack.append(arg)
                case "*" | "+":
                    arg1 = stack.pop()
                    arg2 = stack.pop()
                    result = self.ops[token](arg1, arg2)
                    stack.append(result)
                case "a" | "b" | "c":
                    stack.append(values[self.ops[token]])
        return int(stack.pop())

    def convert(self, input_formula):
        output_formula = ""
        stack = []
        for token in input_formula:
            match token:
                case "(":
                    stack.append(token)
                case ")":
                    while stack[-1] != "(":
                        output_formula += stack.pop()
                    stack.pop()
                case "a" | "b" | "c":
                    output_formula += token
                case "+" | "*" | "!":
                    while stack and self.priority[stack[-1]] > self.priority[token]:
                        output_formula += stack.pop()
                    stack.append(token)
        while stack:
            output_formula += stack.pop()
        return output_formula

    def print_table(self):
        print("\n\n   #    |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8")
        print("------------------------------------------------------------------------\n   x1   ", end="")
        for i in self.table:
            print("|   {}   ".format(i["x1"]), end="")
        print("\n------------------------------------------------------------------------\n   x2   ", end="")
        for i in self.table:
            print("|   {}   ".format(i["x2"]), end="")
        print("\n------------------------------------------------------------------------\n   x3   ", end="")
        for i in self.table:
            print("|   {}   ".format(i["x3"]), end="")
        print("\n------------------------------------------------------------------------\n   f    ", end="")
        for i in self.table:
            print("|   {}   ".format(i["f"]), end="")
        print("\n------------------------------------------------------------------------\n")

    def print_sdnf(self):
        print("SDNF function:", self.sdnf)

    def print_sknf(self):
        print("\nSKNF function:", self.sknf)

    def print_bin_num_sdnf(self):
        print("\nBin SDNF function:", self.bin_num_sdnf)

    def print_bin_num_sknf(self):
        print("\nBin SKNF function:", self.bin_num_sknf)

    def from_bin_to_decimal(self, bin_num):
        result = 0
        for degree, i in enumerate(bin_num[::-1]):
            if i == '1':
                result += 2 ** degree
        return result

    def print_num_sdnf(self):
        num_sdnf_list = self.bin_num_sdnf.split('+')
        for i in num_sdnf_list:
            result = self.from_bin_to_decimal(i)
            self.num_sdnf += f"{result}V"
        self.num_sdnf = self.num_sdnf[:-1]
        print("\nNum SDNF function:", self.num_sdnf)

    def print_num_sknf(self):
        num_sknf_list = self.bin_num_sknf.split('*')
        for i in num_sknf_list:
            result = self.from_bin_to_decimal(i)
            self.num_sknf += f"{result}A"
        self.num_sknf = self.num_sknf[:-1]
        print("\nNum SKNF function:", self.num_sknf)

    def print_index_form(self):
        bin_index_form = ""
        for i in self.table:
            bin_index_form += str(i["f"])
        self.index_form = self.from_bin_to_decimal(bin_index_form)
        print("\nIndex form:", self.index_form)

    def __init__(self, formula):
        reverse_polish_notation = self.convert(formula)
        for dictionary in self.table:
            values = tuple(dictionary.values())[:3]
            dictionary["f"] = self.counting(reverse_polish_notation, values)
            if dictionary["f"] == 1:
                if dictionary["x1"] == 1:
                    self.sdnf += "a*"
                    self.bin_num_sdnf += '1'
                else:
                    self.sdnf += "!a*"
                    self.bin_num_sdnf += '0'
                if dictionary["x2"] == 1:
                    self.sdnf += "b*"
                    self.bin_num_sdnf += '1'
                else:
                    self.sdnf += "!b*"
                    self.bin_num_sdnf += '0'
                if dictionary["x3"] == 1:
                    self.sdnf += "c + "
                    self.bin_num_sdnf += '1+'
                else:
                    self.sdnf += "!c + "
                    self.bin_num_sdnf += '0+'
            else:
                if dictionary["x1"] == 1:
                    self.sknf += "(!a+"
                    self.bin_num_sknf += "0"
                else:
                    self.sknf += "(a+"
                    self.bin_num_sknf += "1"
                if dictionary["x2"] == 1:
                    self.sknf += "!b+"
                    self.bin_num_sknf += "0"
                else:
                    self.sknf += "b+"
                    self.bin_num_sknf += "1"
                if dictionary["x3"] == 1:
                    self.sknf += "!c) * "
                    self.bin_num_sknf += "0*"
                else:
                    self.sknf += "c) * "
                    self.bin_num_sknf += "1*"
        self.sdnf = self.sdnf[:-3]
        self.sknf = self.sknf[:-3]
        self.bin_num_sdnf = self.bin_num_sdnf[:-1]
        self.bin_num_sknf = self.bin_num_sknf[:-1]


def main():
    try:
        formula = "!((!a+b)*!(b*c))"
        if formula.count("(") == formula.count(")"):
            print("Formula:", formula)
            logic_function = LogicFunction(formula)
            logic_function.print_table()
            logic_function.print_sdnf()
            logic_function.print_sknf()
            logic_function.print_bin_num_sdnf()
            logic_function.print_bin_num_sknf()
            logic_function.print_num_sdnf()
            logic_function.print_num_sknf()
            logic_function.print_index_form()
        else:
            print("Wrong number of brackets")
    except IndexError:
        print("Wrong formula")


if __name__ == "__main__":
    main()