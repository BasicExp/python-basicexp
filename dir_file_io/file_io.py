

def file_to_string(file_path):
    """Takes in a file path and returns the contents as a string"""
    with open(file_path) as file:
        js_string = file.read()
        file.close()
    return js_string




