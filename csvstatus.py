from enum import Enum

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

# Mini-project that processes a data set in different ways
# depending on the status of the data sent to the system
# Pending converts the content to strings.
# Processing converts it into a string csv.
# Success assumes it's already in the format we want.
# Failure performs Pending then Processing.
def get_csv_status(status, data):
    match(status):
        case(CSVExportStatus.PENDING):
            stringlists = list(map(lambda x : list(map(str, x)), data))
            return ("Pending...", stringlists)
        case(CSVExportStatus.PROCESSING):
            stringlists = ""
            for lst in data:
                row = ""
                for string in lst:
                    row += string + ","
                row = row[:-1]
                stringlists += row + "\n"
            stringlists = stringlists[:-1]
            return ("Processing...", stringlists)
        case(CSVExportStatus.SUCCESS):
            return ("Success!", data)
        case(CSVExportStatus.FAILURE):
            return ("Unknown error, retrying...", get_csv_status(CSVExportStatus.PROCESSING, (get_csv_status(CSVExportStatus.PENDING, data))[1])[1])
        case _:
            raise Exception("unknown export status")
