from dir_console_tools.pretty_formatter import print_symbol_rows, print_title_with_stars, print_symbols
from dir_file_io.file_io import file_to_string
from dir_file_io.js_file_io import js_string_with_logging
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

"""\
Formatting Variables
"""

symbol_count = 75
dividing_symbol = '-'
row_count = 1

if _CONSOLE_TOOLS:
    print_title_with_stars("DEMO: pretty_formatter", symbol_count)
    print_symbols("~`*",  int(symbol_count / 3))
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

if _FILE_IO:
    print_title_with_stars("DEMO: file_io", symbol_count)
    path = 'dir_file_io/sample.txt'
    f = file_to_string(path)
    print(f)
    print_symbol_rows(row_count, symbol_count, dividing_symbol)

    print_title_with_stars("DEMO js_file_io, ideal for use with Selenium", symbol_count)
    path = 'dir_file_io/sample.js'
    js = js_string_with_logging(path)
    print(js)
    print_symbol_rows(row_count, symbol_count,dividing_symbol)




