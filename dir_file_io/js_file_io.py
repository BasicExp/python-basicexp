import dir_file_io.file_io as file_io


def js_string_with_logging(file_path):
    """Takes in a file path and returns a JS file with
    additional logging to the browser console"""
    js = file_io.file_to_string(file_path)
    js = 'try {' + js + '} catch(err) { console.log(err); }'
    return js
