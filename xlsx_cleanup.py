# Cleaner
# Limpia caracteres especiales para reducir la complejidad y guarda en 
# excel .xlsx y parejas tabuladas en .txt
import pandas as pd
 
# read by default 1st sheet of an excel file
filename = "spa-gum"
version = "cleaned" # change on every run
source_lang = filename.split('-')[0]
target_lang = filename.split('-')[1]
df = pd.read_excel(f'{filename}.xlsx')

# Clean special chars and move to nextline
trans_dict = {
             ord('-'): '',
             ord('–'): '',
             ord('—'): '',
             ord('“'): '"',
             ord('”'): '"',
            #  ord('.'): '.',
            #  ord('!'): '',
            #  ord('¡'): '',
            #  ord('?'): '',
            #  ord('¿'): '',
             ord('’'): '"',
             ord('‘'): '"',
             ord("'"): '"',
             ord('|'): '',
             ord('#'): '', 
             ord('$'): '',
             ord('%'): '', 
             ord('&'): '',
            #  ord(';'): ',',
            #  ord('"'): '',
             ord('«'): '"',
             ord('»'): '"',
             ord('ѳ'): 'ø',
        }
lines = []
for ind in df.index:
    source_text = df[f"{source_lang}_text"][ind]
    target_text = df[f"{target_lang}_text"][ind]
    source_text = str(source_text).strip().translate(trans_dict)
    target_text = str(target_text).strip().translate(trans_dict)
    df.at[ind, f"{target_lang}_text"] = target_text
    df.at[ind, f"{source_lang}_text"] = source_text
    # source_text = re.sub(r'[-–—]', '', source_text)
    # source_text = re.sub('[“”.:¡!¿?"«»‘’]', SPL, source_text)
    # target_text = re.sub(r'[-–—]', '', target_text)
    # target_text = re.sub('[ѳ]', 'ø', target_text)
    # target_text = re.sub('[“”.:¡!¿?"«»‘’]', SPL, target_text)
    # print(target_text)
    lines.append(f'{source_text}\t{target_text}')

# save Dataframe in Excel
df.to_excel(f'{filename}_{version}.xlsx')
# Save to TXT
with open(f'{filename}_{version}.txt', 'w', encoding="utf-8") as f:
    for line in lines: 
        f.write(line)
        f.write('\n')