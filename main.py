from dir_console_tools.pretty_formatter import print_stars_rows, print_title_with_stars
from dir_file_io.file_io import file_to_string
from dir_file_io.js_file_io import js_string_with_logging
from selenium import webdriver


"""\
This file script is used to run a demo of all of the tools present in
in this repository
"""
star_count = 75
row_count = 3

print_title_with_stars("DEMO: Print Out File", star_count)
path = 'dir_file_io/sample.js'
f = file_to_string(path)
print_stars_rows(row_count, star_count)

print("DEMO js_file_io with selenium")
chrome_driver = webdriver.Chrome(executable_path='C:\\WebDrivers\\chromedriver.exe')
chrome_driver.get('https://basicexp.ca')
js = js_string_with_logging(path)
result = chrome_driver.execute_script(js)
print(f'JavaScript Ran: {result}')
print()




