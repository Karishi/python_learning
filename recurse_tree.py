def list_files(parent_directory, current_filepath=""):
    paths = []
    for item in parent_directory.values():
        new_filepath = current_filepath + "/" + item
        
        if item == None:
            paths.append(current_filepath)
        else:
            paths.extend(list_files(item, current_filepath))
    return paths

test = {'Documents': {'Proposal.docx': None, 'Report': {'AnnualReport.pdf': None, 'Financials.xlsx': None}}, 'Downloads': {'picture1.jpg': None, 'picture2.jpg': None}}
print(list_files(test))