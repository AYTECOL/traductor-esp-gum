import pandas as pd
import re
 
# read by default 1st sheet of an excel file
df = pd.read_excel('spa-gum.xlsx')

# Clean special chars and move to nextline
SPL = "<SPL>"
trans_dict = {
             '-': '',
             '–': '',
             '—': '',
             '“': SPL,
             '”': SPL,
             '.': SPL,
             '!': SPL,
             '¡': SPL,
             '?': SPL,
             '¿': SPL,
             ';': SPL,
             '"': SPL,
             '«': SPL,
             '»': SPL,
             'ѳ': 'ø',
        }
lines = []
for ind in df.index:
        spa_text = df["spa_text"][ind]
        gum_text = df["gum_text"][ind]
        # spa_text = str(spa_text).translate(trans_dict)
        # gum_text = str(gum_text).translate(trans_dict)
        spa_text = re.sub(r'[-–—]', '', spa_text)
        spa_text = re.sub('[“”.:¡!¿?"«»‘’]', SPL, spa_text)
        gum_text = re.sub(r'[-–—]', '', gum_text)
        gum_text = re.sub('[ѳ]', 'ø', gum_text)
        gum_text = re.sub('[“”.:¡!¿?"«»‘’]', SPL, gum_text)
        # print(gum_text)

        # strip all phrases
        split_spa = [x.strip() for x in str(spa_text).split(SPL)]
        split_gum = [x.strip() for x in str(gum_text).split(SPL)]

        # remove empty strings
        split_spa = [i for i in split_spa if i]
        split_gum = [i for i in split_gum if i]
        #los tamaños que se deben comparar son los inetervalos no vacios
        if len(split_spa) == len(split_gum):
            # print("-----------")
            # print(split_spa)
            # print(split_gum)
            for idx in range(len(split_spa)):
                if not len(split_gum[idx]) == 0 and not len(split_spa[idx]) == 0:
                    lines.append(f'{split_spa[idx].replace(SPL,"").strip().lower()}\t{split_gum[idx].replace(SPL,"").strip().lower()}') 
        else:
            lines.append(f'{spa_text.replace(SPL,"").strip().lower()}\t{gum_text.replace(SPL,"").strip().lower()}')
        # break

# Save to TXT
with open('spa-gum.txt', 'w', encoding="utf-8") as f:
    for line in lines: 
        f.write(line)
        f.write('\n')