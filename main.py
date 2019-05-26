from dir_file_io.file_io import file_to_string
from dir_file_io.js_file_io import js_string_with_logging
from selenium import webdriver


"""\
This file script is used to run a demo of all of the tools present in
in this repository
"""

path = 'dir_file_io/sample.js'
print('DEMO dir_file_io')
f = file_to_string(path)
print(f)
print()

print("DEMO js_file_io with selenium")
chrome_driver = webdriver.Chrome(executable_path='C:\\WebDrivers\\chromedriver.exe')
chrome_driver.get('https://basicexp.ca')
result = chrome_driver.execute_script(js_string_with_logging(path))
print(f'JavaScript Ran: {result}')
print()




