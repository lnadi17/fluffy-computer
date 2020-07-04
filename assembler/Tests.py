from unittest import TestCase
from os import listdir
from Assembler import assemble


class TestAssembler(TestCase):
    def setUp(self):
        self.asm_test_files = [i for i in listdir('tests') if '.asm' in i]

    def test_assemble(self):
        for input_file in self.asm_test_files:
            # Arrange
            test_file = 'tests/' + input_file.split('.')[0] + '.bin'
            output_file = 'tests/' + input_file.split('.')[0] + '_out.bin'
            # Act
            assemble('tests/' + input_file)
            # Assert
            with open(test_file, 'r') as f:
                test_str = f.read()
            with open(output_file, 'r') as f:
                out_str = f.read()
            self.assertMultiLineEqual(test_str, out_str)
