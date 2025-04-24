# Uses args and kwargs to convert a number of .md files to plaintext without knowing
# how many in advance.
def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        plaintext_list = list(map(convert_md_to_txt, args))
        
        plaintest_dict = dict(map(value_to_text, kwargs.items()))
        return func(*plaintext_list, **plaintest_dict)

    def value_to_text(tuple_item):
        key, value = tuple_item
        return (key, convert_md_to_txt(value))
    return wrapper



def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
