class Code:
    def __init__(self):
        self.destination_dict = {
            'null':     '000',
            'M':        '010',
            'D':        '001',
            'MD':       '011',
            'A':        '100',
            'AM':       '110',
            'AD':       '101',
            'AMD':      '111',
        }

        self.operator_dict = {
            '+': '000',
            '-': '001',
            '*': '010',
            ':': '011',
            '!': '100',
            '&': '101',
            '|': '110',
            '^': '111',
        }

        # X may be A, M or S, depending on control bits.
        self.operand_dict = {
            '*0':   '000',
            'D*X':  '001',
            '*X':   '010',
            '*D':   '011',
            'X*D':  '100',
            '*1':   '101',
            'X*1':  '110',
            'D*1':  '111',
        }

        self.jump_dict = {
            'null':     '000',
            'JGT':      '001',
            'JEQ':      '010',
            'JGE':      '011',
            'JLT':      '100',
            'JNE':      '101',
            'JLE':      '110',
            'JMP':      '111',
        }

    def destination(self, destination):
        return self.destination_dict[destination]

    def operands(self, operands):
        return self.operand_dict[operands]

    def operator(self, operator):
        return self.operator_dict[operator]

    def jump(self, jump):
        return self.jump_dict[jump]

    # Argument 'label' should be decimal.
    @staticmethod
    def label(label):
        binary = bin(int(label))[2::]
        return '0' * (16 - len(binary)) + binary

    def c_code(self, is_stack, push_pop, operator, is_memory, operands, destination, jump):
        stack_bit = '0'
        push_pop_bit = '0'
        memory_bit = '0'

        if is_stack:
            stack_bit = '1'
            push_pop_bit = push_pop

        if is_memory and push_pop_bit == '0':
            memory_bit = '1'

        return ('1' +
                stack_bit +
                push_pop_bit +
                self.operator(operator) +
                memory_bit +
                self.operands(operands) +
                self.destination(destination) +
                self.jump(jump))

    def a_code(self, label):
        return self.label(label)
