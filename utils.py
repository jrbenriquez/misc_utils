import pandas as pd
import os
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def compile_to_excel(folder_list, filetype):
    writer = pd.ExcelWriter('output.xlsx')

    ''' Read all files in folder_list and create a dataframe for it '''
    for folder in folder_list:
        os.chdir("%s/%s" % (DIR_PATH, folder))
        files = [
            f for f in os.listdir(
                '.'
            ) if os.path.isfile(f) and f.endswith('.%s' % (filetype))
        ]
        print files
        for file in files:
            print file
            df = pd.read_csv(file)
            ''' Add dataframe as a sheet in workbook '''
            df.to_excel(
                writer,
                file.replace(".%s" % (filetype), ""),
                index=False
            )
    ''' Go back to original directory and save excel '''
    os.chdir(DIR_PATH)
    writer.save()
