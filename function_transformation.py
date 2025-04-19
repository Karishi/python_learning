# Above line 10 is my own work - an exercise to learn about transforming functions to handle
# different kinds of data or user needs.
def doc_format_checker_and_converter(conversion_function, valid_formats):
    def convert(filename, content):
        file_extension = filename.split(".")[-1]
        if file_extension in valid_formats:
            return conversion_function(content)
        raise ValueError("invalid file format")

    return convert



def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
