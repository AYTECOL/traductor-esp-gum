import os
import pandas as pd

inputfilename='palabras_clave_bib.txt'
outname = 'from_txt.xlsx'
outdir = './output'

targets = []
sources = []
with open(f"dirty/{inputfilename}", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        if 'class="k"' in line:
            # print(line)
            _split = line.split('<span class="k">')[1].split('</span>')
            targets.append(_split[1].replace('</div>','').strip())
            sources.append(_split[0].strip())

df = pd.DataFrame(list(zip(sources, targets, )),
               columns =['source', 'target'])
df['origin'] = inputfilename

if not os.path.exists(outdir):
    os.mkdir(outdir)

fullname = os.path.join(outdir, outname)   

df.to_excel(fullname)