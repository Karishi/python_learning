def map_keywords(document, document_map):
    map_copy = document_map.copy()
    if document in map_copy:
        return map_copy[document], map_copy
    found_keywords = find_keywords(document)
    map_copy[document] = found_keywords
    return found_keywords, map_copy


def find_keywords(document):
    keywords = [
    "functional",
    "immutable",
    "declarative",
    "higher-order",
    "lambda",
    "deterministic",
    "side-effects",
    "memoization",
    "referential transparency",
    ]
    present_keywords = filter(lambda x: x in document.lower(), keywords)
    return list(present_keywords)
