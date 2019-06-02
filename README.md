# Python BasicExp
This is a collection of tools I am creating that I find useful across projects.

## File IO Tools

PATH: dir_file_io\file_io

```
file_to_string(file_path)
```

This function turns the entire contents of a file into a string

## JavaScript File Reader

PATH: ./dir_file_io/js-file-reader

```
js_string_with_logging(file_path)
```

This function gives you the ability to read in JavaScript files as
strings and wraps them in a try-catch block that logs errors to the 
browser console

## Pretty Formatter
This module has simple function calls that let you format console output
consistently and easily

PATH: ./dir_console_tools/pretty_formatter

```
print_title_with_stars(title, count= 100, symbol= "~`*")
```

This function prints out a title wrapped with two lines of symbols

```
print_symbol_rows(row_count, count, symbol = "~`*")
```

This function prints out a a number of rows of the specified symbol.
The count indicated the total number of characters to print and not
the number if times to print the symbol.

```
print_symbols(string, count)
```

This function prints out symbols a number times specified



