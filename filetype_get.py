# When handed a list of (classification: [list of filetypes]), use a lambda
# function to return a dict of {filetype: classification} pairs for reading.

def file_type_getter(file_extension_tuples):
    extension_map = {}
    for item in file_extension_tuples:
        for datatype in item[1]:
            extension_map[datatype] = item[0]
    title = lambda name: extension_map.get(name, "Unknown")
    return title