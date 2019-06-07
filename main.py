from dir_console_tools.pretty_formatter import print_symbol_rows, print_title, print_symbols
from dir_file_io.file_io import file_to_string
from dir_file_io.js_file_io import js_string_with_logging
from dir_exceptions.exception import try_executing
# from selenium import webdriver

"""\
This file script is used to run a demo of all of the tools present in
in this repository
"""

"""\
These variables can be used to turn on and off demonstrations
"""

_CONSOLE_TOOLS = False
_FILE_IO = True
_EXCEPTIONS = True

"""\
Formatting Variables
"""

symbol_count = 75
dividing_symbol = '-'
row_count = 1

if _CONSOLE_TOOLS:
    print_title("DEMO: pretty_formatter", symbol_count)
    print_symbols("~`*",  int(symbol_count / 3))
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

if _FILE_IO:
    print_title("DEMO: file_io", symbol_count)
    path = 'dir_file_io/sample.txt'
    f = file_to_string(path)
    print(f)
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

    print_title("DEMO js_file_io, ideal for use with Selenium", symbol_count)
    path = 'dir_file_io/sample.js'
    js = js_string_with_logging(path)
    print(js)
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

if _EXCEPTIONS:
    print_title("DEMO: exceptions", symbol_count)

    def divide_by_zero():
        return 1/0

    def catch(exp: Exception):
        print('ERROR: divide_by_zero caused exception')
        print('EXCEPTION TYPE: ' + str(exp))
        return None

    def always():
        print('ALWAYS PRINT')

    try_executing(divide_by_zero, catch)
    print()
    try_executing(divide_by_zero, catch, always)
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

