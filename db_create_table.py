# import packages

import pandas as pd
import sys
from datetime import datetime
from pathlib import Path
from dateutil.parser import parse
from unidecode import unidecode


def is_date(string):
    try:
        parse(str(string))
        return True
    except ValueError:
        return False


def is_int_like(x):
    try:
        int(x)
        return True
    except (ValueError, TypeError):
        return False


def is_float_like(x):
    try:
        float(x)
        return True
    except (ValueError, TypeError):
        return False


def get_file():
    filename = input('Input the file path:')
    if filename == 'exit':
        sys.exit("Aborted by user...")
    elif not Path(filename).exists():
        print("Invalid path!")
        filename = get_file()
    elif not Path(filename).is_file():
        print("Not a file!")
        filename = get_file()
    elif not filename.lower().endswith(".csv"):
        print("Not a CSV file!")
        filename = get_file()
    return filename


def get_datatype(list_to_check: list, listnum: int):
    isdate = True
    isnum = True
    isfloat = True
    print(' '*30, end='\r')
    try:
        for i, value in enumerate(list_to_check):
            print('\rChecking data types: ' + str(i) +
                  ' field of column '+str(listnum+1), end='')
            if not is_int_like(value):
                isnum = False
            if not is_date(value):
                isdate = False
            if not is_float_like(value):
                isfloat = False
            if not (isdate | isnum | isfloat):
                return 'varchar(255)'
    except:
        return 'varchar(255)'

    if isnum:
        return 'int'
    elif isdate:
        return 'date'
    elif isfloat:
        return 'numeric'
    return 'varchar(255)'

### MAIN ###


filename = get_file()
tablename = input('Input the table name: ')
resfile = "C:\\temp\\res.sql"
basetable = pd.read_csv(filename, delimiter=';')

datatypes = list()
col_list = basetable.columns.tolist()
num_of_col = len(col_list)

for i in range(num_of_col):
    rowlist = list()
    for j in range(len(basetable)):
        rowlist.append(basetable.iloc[j, i])
    datatypes.append(get_datatype(rowlist, i))

final_file = open(resfile, 'w+')
final_file.write('CREATE TABLE '+tablename+'(\n')
for i, field in enumerate(col_list):
    itemend = '\n' if i == len(col_list)-1 else ', '
    final_file.write('\t'+unidecode(field)+' '+datatypes[i]+',\n')
final_file.write(');\n\n')
final_file.write('INSERT INTO '+tablename +
                 ' ('+unidecode(', '.join(col_list))+')\n')
final_file.write('VALUES\n')
print('')
for i, row in basetable.iterrows():
    final_file.write('\t(')
    for j, item in enumerate(row):
        v = '' if pd.isna(item) else item
        print('\rWriting: ' + str(i)+'/'+str(len(basetable)-1)+' record', end='')
        final_file.write('\''+str(v)+'\'')
        itemend = ')' if j == len(row)-1 else ', '
        final_file.write(itemend)
    endsign = ';' if i == len(basetable)-1 else ',\n'
    final_file.write(endsign)
