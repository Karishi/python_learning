# Find the number of lines in a document that contain a specific character sequence.
# This uses currying, taking a function that accepts several arguments and turns it
# into several functions that take one argument each.
def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length

        def with_length(doc):
            count = 0
            sequences = doc.split("\n")
            for item in sequences:
                if sequence in item:
                    count += 1
            return count

        return with_length

    return with_char
