# Automatic convert from word to excel
# IN: input format is .docx with lines containing target and source 
# phrases separated by \t (TAB) characters
# OUT: output is a .xlsx (Excel) file
import os
import docx2txt
import re
import pandas as pd

inputdir = './dirty'
outname = 'from_word.xlsx'
outdir = './output'
df = pd.DataFrame(columns =['target', 'source', 'origin'])

for file in os.listdir(inputdir):
    # check only text files
    if file.endswith('.docx'):
        target_lines = []
        source_lines = []
        print(file)
        my_text = docx2txt.process(f'{inputdir}/{file}')
        for line in str(my_text).split('\n'):
            aux = re.sub('\t+','\t',line.strip())
            splited = aux.split("\t")
            if len(splited) > 1:
                print(splited)
                #TODO: clean symbols and trailing spaces close to commas, points
                target_lines.append(splited[0].strip())
                source_lines.append(splited[1].strip())
                # print(f'{splited[0].strip()}\t{splited[1].strip()}')
        file_df = pd.DataFrame(list(zip(target_lines, source_lines, )),
               columns =['target', 'source'])
        file_df['origin'] = file
        df = pd.concat([df, file_df])

if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)   

df.to_excel(fullname)
