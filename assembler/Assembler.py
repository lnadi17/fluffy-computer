import sys
import argparse
from Parser import *
from Code import *

INTERRUPT_VECTOR_CODE = '@MASK\nD=M\n@INTERRUPT_FUNCTION\nD&1;JGT\nD=0\n'


def assemble(file_name, is_binary=False, has_hex_header=True, has_interrupt_header=False, suffix=''):
    if has_interrupt_header:
        parser = Parser(file_name, header=INTERRUPT_VECTOR_CODE)
    else:
        parser = Parser(file_name)
    code = Code()

    with open(file_name.split('.')[0] + suffix + '.bin', 'w') as f:
        # Write hex header.
        if has_hex_header:
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

            if is_binary:
                f.write(out + '\n')
            else:
                f.write(bin_to_hex(out) + '\n')


def bin_to_hex(binary_num):
    res = '' + hex(int(binary_num, 2))[2:]
    if len(res) < 4:
        for i in range(4 - len(res)):
            res = '0' + res
    return res


def main():
    # Create argument parser.
    arg_parser = argparse.ArgumentParser(description='Convert assembly (.asm) file to binary (.bin) file in order to '
                                                     'load it in fluffy computer\'s ROM and run it.')
    arg_parser.add_argument('file',
                            help='name of input assembly file')
    arg_parser.add_argument('-ih', '--interrupt_header', action='store_true',
                            help='write interrupt vector code in output file. if this is true, label '
                                 'with the name "INTERRUPT_FUNCTION" must also be added by the user')
    arg_parser.add_argument('-nxh', '--no-hex-header', action='store_false',
                            help='do not add hex header in output file, '
                                 'which is something like "hex v3.0 words plain"')
    arg_parser.add_argument('-b', '--binary', action='store_true',
                            help='write output in binary instead of hexadecimal')
    args = arg_parser.parse_args()

    assemble(args.file, args.binary, args.no_hex_header, args.interrupt_header)


if __name__ == '__main__':
    main()
