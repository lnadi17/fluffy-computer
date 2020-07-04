class Parser:
    def __init__(self, file_name):
        self.file_name = file_name
        self.current_num = 0
        self.current_str = ''
        self.instruction_count = 0
        self.instructions = []
        self.symbol_table = {}
        self.var_count = 0

        with open(file_name, 'r') as f:
            lines = f.read().splitlines()
            for line in lines:
                parsed_line = ''.join(line.split()).split('/', 1)[0]
                if parsed_line != '':
                    self.instructions.append(parsed_line)

        self.update_symbol_table()
        self.instruction_count = len(self.instructions)

    # Returns True if successfully selected next instruction, False if limit reached.
    def select_next(self):
        if self.current_num == self.instruction_count:
            # print("Instruction limit reached.")
            return False
        self.current_str = self.instructions[self.current_num]
        self.current_num += 1
        return True

    # Returns 'A', 'C' or 'L' depending on current instruction type.
    def current_type(self):
        if self.current_str[0] == '@':
            return 'A'
        elif self.current_str[0] == '(':
            return 'L'
        else:
            return 'C'

    # Returns 'A', 'C' or 'L' depending on passed instruction type.
    @staticmethod
    def type(instruction):
        if instruction[0] == '@':
            return 'A'
        elif instruction[0] == '(':
            return 'L'
        else:
            return 'C'

    # Returns string after '@'. Used for A or L type instructions.
    def label(self):
        res = self.current_str[1::]
        # If not decimal, it must be a symbol.
        if not res.isdecimal():
            sym = self.symbol_table.get(res)
            # If not in table, then it must a variable declaration.
            if not sym:
                sym_value = str(23 + self.var_count)
                self.symbol_table.update({res: sym_value})
                self.var_count += 1
                # After adding variable in a symbol table, return it.
                return sym_value
            # If in table, then it is previously defined variable or label. return it.
            return sym
        # If label is decimal, return it.
        return res

    def is_stack(self):
        if 'S' in self.current_str:
            return True
        return False

    def push_pop(self):
        # If it isn't stack operation, push_pop doesn't matter, so it defaults to zero.
        if not self.is_stack():
            return '0'
        # If no equality sign, we know for sure that it isn't push.
        if self.current_str.count('=') == 0:
            return '1'
        else:
            left_side = self.current_str.split('=')[0]
            right_side = self.current_str.split('=')[1]
            if 'S' in left_side and 'S' in right_side:
                print('Push and pop at the same time is illegal! Defaulting to push.')
                return '0'
            if 'S' in left_side:
                return '0'
            if 'S' in right_side:
                return '1'

    def operator(self):
        possible_operators = {'+', '-', '*', ':', '!', '&', '|', '^'}
        operator = '+'  # Default operator is a plus sign.
        for op in possible_operators:
            if op in self.current_str:
                operator = op
        return operator

    def is_memory(self):
        # Stack operation implies that current operation isn't memory operation.
        if self.is_stack():
            return False
        compute = self.current_str
        if compute.count('=') > 0:
            compute = compute.split('=')[1]
        if compute.count(';') > 0:
            compute = compute.split(';')[0]
        if 'M' in compute:
            return True
        return False

    def operands(self):
        possible_operators = {'+', '-', '*', ':', '!', '&', '|', '^'}
        operands = self.current_str
        if operands.count('=') > 0:
            operands = operands.split('=')[1]
        if operands.count(';') > 0:
            operands = operands.split(';')[0]

        for op in possible_operators:
            operands = operands.replace(op, '*')
        for ams in ('A', 'M', 'S'):
            operands = operands.replace(ams, 'X')

        if operands.count('*') == 0:
            operands = '*' + operands

        return operands

    def destination(self):
        if self.current_str.count('=') == 0:
            # If no equality sign, destination is null.
            return 'null'
        else:
            res = self.current_str.split('=')[0].replace('S', '')
            if res == '':
                return 'null'
            return res

    def jump(self):
        if self.current_str.count(';') == 0:
            # If no semicolon sign, jump is null.
            return 'null'
        return self.current_str.split(';')[1]

    def update_symbol_table(self):
        # Add predefined symbols.
        self.symbol_table = {
            'DDR': '0',
            'PORT': '1',
            'PIN': '2',
            'MASK': '3',
            'PRESCALER': '4',
            'COUNTER': '5',
            'KEYBOARD': '6',
            'R0': '7',
            'R1': '8',
            'R2': '9',
            'R3': '10',
            'R4': '11',
            'R5': '12',
            'R6': '13',
            'R7': '14',
            'R8': '15',
            'R9': '16',
            'R10': '17',
            'R11': '18',
            'R12': '19',
            'R13': '20',
            'R14': '21',
            'R15': '22',
        }

        index = 0
        # Parse labels only first.
        for i in self.instructions:
            if self.type(i) == 'L':
                self.symbol_table.update({i[1:-1]: str(index)})
                index -= 1
            index += 1
