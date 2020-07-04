import sys
from Parser import *
from Code import *


def assemble(file_name):
    parser = Parser(file_name)
    code = Code()

    with open(file_name.split('.')[0] + '_out.bin', 'w') as f:
        # Write header.
        f.write('v3.0 hex words plain\n')
        while parser.select_next():
            if parser.current_type() == 'A':
                out = code.a_code(parser.label())
            if parser.current_type() == 'C':
                out = code.c_code(parser.is_stack(),
                                  parser.push_pop(),
                                  parser.operator(),
                                  parser.is_memory(),
                                  parser.operands(),
                                  parser.destination(),
                                  parser.jump())
            if parser.current_type() == 'L':
                continue
            f.write(bin_to_hex(out) + '\n')


def bin_to_hex(binary_num):
    res = '' + hex(int(binary_num, 2))[2:]
    if len(res) < 4:
        for i in range(4 - len(res)):
            res = '0' + res
    return res


def main():
    file_name = sys.argv[1]
    assemble(file_name)


if __name__ == '__main__':
    main()
